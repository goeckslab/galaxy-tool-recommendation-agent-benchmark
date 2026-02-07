from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple

from scripts.eval.evaluate_recommendations import normalize_tool_id, unique_in_order


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Analyze a run predictions.jsonl with a focus on error patterns and, when present, "
            "standalone agent usage (requests/tool_calls/tokens)."
        )
    )
    p.add_argument("--gold", type=Path, required=True, help="Gold JSONL (id/tools/query).")
    p.add_argument("--predictions", type=Path, required=True, help="Run predictions.jsonl.")
    p.add_argument("--output-md", type=Path, required=True, help="Write Markdown diagnostics here.")
    p.add_argument("--k", type=str, default="1,3,5,10", help="Cutoffs for Hit@k summary.")
    p.add_argument("--top-n", type=int, default=15, help="How many examples to show per section.")
    p.add_argument("--normalize-tools", action="store_true", help="Drop toolshed version when comparing tool IDs.")
    return p.parse_args()


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict):
                out.append(obj)
    return out


def _norm_list(values: List[str], do_normalize: bool) -> List[str]:
    if not do_normalize:
        return unique_in_order(values)
    return unique_in_order(normalize_tool_id(v) for v in values)


def _hit_at_k(preds: List[str], gold: set[str], k: int) -> float:
    if not gold:
        return 0.0
    return 1.0 if any(p in gold for p in preds[:k]) else 0.0


def _tool_family(tool_id: str) -> str:
    if not isinstance(tool_id, str) or not tool_id:
        return "unknown"
    if tool_id.startswith("toolshed.g2.bx.psu.edu/repos/"):
        parts = tool_id.split("/")
        if len(parts) >= 6:
            owner = parts[3]
            repo = parts[4]
            return f"{owner}/{repo}"
    # Keep non-toolshed IDs visible as their raw ID prefix.
    return tool_id.split("/")[0]


def _short(text: str, n: int = 140) -> str:
    t = (text or "").strip().replace("\n", " ")
    return (t[: n - 1] + "…") if len(t) > n else t


def _pct(values: List[int], p: float) -> int:
    if not values:
        return 0
    v = sorted(values)
    return v[int((len(v) - 1) * p)]


def main() -> None:
    args = parse_args()
    ks = [int(k.strip()) for k in args.k.split(",") if k.strip()]

    gold_raw = load_jsonl(args.gold)
    pred_raw = load_jsonl(args.predictions)

    gold_by_id: Dict[str, Dict[str, Any]] = {}
    for it in gold_raw:
        qid = it.get("id")
        if isinstance(qid, str) and qid:
            gold_by_id[qid] = it

    # Collapse predictions: keep the last record per id (append-style files).
    pred_by_id: Dict[str, Dict[str, Any]] = {}
    for it in pred_raw:
        qid = it.get("id")
        if isinstance(qid, str) and qid:
            pred_by_id[qid] = it

    common_ids = [qid for qid in gold_by_id.keys() if qid in pred_by_id]
    n = len(common_ids)

    hit = {k: 0.0 for k in ks}
    empty = 0
    top1_wrong = 0
    miss_all10 = 0
    qiime2_top10_misses = 0

    reqs: List[int] = []
    tool_calls: List[int] = []
    total_tokens: List[int] = []

    pred_family = Counter()
    gold_family = Counter()
    wrong_family = Counter()

    hardest: List[Tuple[int, int, str]] = []  # (requests, tool_calls, qid)
    token_heavy: List[Tuple[int, int, str]] = []  # (total_tokens, requests, qid)
    examples_empty: List[str] = []
    examples_top10_miss: List[str] = []

    for qid in common_ids:
        gold_tools_raw = [t for t in (gold_by_id[qid].get("tools") or []) if isinstance(t, str)]
        pred_tools_raw = [p for p in (pred_by_id[qid].get("predictions") or []) if isinstance(p, str)]

        gold_tools = _norm_list(gold_tools_raw, args.normalize_tools)
        pred_tools = _norm_list(pred_tools_raw, args.normalize_tools)
        gold_set = set(gold_tools)

        if not pred_tools:
            empty += 1
            examples_empty.append(qid)
            continue

        for k in ks:
            hit[k] += _hit_at_k(pred_tools, gold_set, k)

        pred1 = pred_tools[0]
        if pred1 not in gold_set:
            top1_wrong += 1
            wrong_family[f"{_tool_family(pred1)} -> {_tool_family(gold_tools[0]) if gold_tools else 'unknown'}"] += 1

        if not any(p in gold_set for p in pred_tools[:10]):
            miss_all10 += 1
            examples_top10_miss.append(qid)
            if any(("qiime2__" in p) or ("/q2d2/" in p) for p in pred_tools_raw):
                qiime2_top10_misses += 1

        for p in pred_tools[:10]:
            pred_family[_tool_family(p)] += 1
        for g in gold_tools:
            gold_family[_tool_family(g)] += 1

        u = pred_by_id[qid].get("standalone_usage")
        if isinstance(u, dict):
            r = u.get("requests")
            tc = u.get("tool_calls")
            tt = u.get("total_tokens")
            if isinstance(r, int):
                reqs.append(r)
            if isinstance(tc, int):
                tool_calls.append(tc)
            if isinstance(tt, int):
                total_tokens.append(tt)
            if isinstance(r, int) and isinstance(tc, int):
                hardest.append((r, tc, qid))
            if isinstance(tt, int) and isinstance(r, int):
                token_heavy.append((tt, r, qid))

    hardest.sort(reverse=True)
    token_heavy.sort(reverse=True)

    hit_rates = {str(k): (hit[k] / n if n else 0.0) for k in ks}

    lines: List[str] = []
    lines.append("# Run diagnostics")
    lines.append("")
    lines.append("## Files")
    lines.append(f"- gold: `{args.gold}`")
    lines.append(f"- predictions: `{args.predictions}`")
    lines.append("")

    lines.append("## Hit@k")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps({"hit": hit_rates, "queries": n, "empty_predictions": empty}, ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")

    if reqs:
        lines.append("## Standalone usage distribution")
        lines.append("")
        lines.append(f"- requests p50/p90/max: {_pct(reqs, 0.5)}/{_pct(reqs, 0.9)}/{max(reqs)}")
        lines.append(
            f"- tool_calls p50/p90/max: {_pct(tool_calls, 0.5)}/{_pct(tool_calls, 0.9)}/{max(tool_calls)}"
        )
        lines.append(
            f"- total_tokens p50/p90/max: {_pct(total_tokens, 0.5)}/{_pct(total_tokens, 0.9)}/{max(total_tokens)}"
        )
        lines.append("")

    lines.append("## Error patterns")
    lines.append("")
    lines.append(f"- top1_wrong: {top1_wrong}/{n}")
    lines.append(f"- miss_all10: {miss_all10}/{n}")
    lines.append(
        f"- miss_all10_with_qiime2_predictions: {qiime2_top10_misses}/{miss_all10 if miss_all10 else 1}"
    )
    lines.append("")

    lines.append("### Most common predicted families (top10)")
    lines.append("")
    for fam, c in pred_family.most_common(args.top_n):
        lines.append(f"- `{fam}`: {c}")
    lines.append("")

    lines.append("### Most common gold families")
    lines.append("")
    for fam, c in gold_family.most_common(args.top_n):
        lines.append(f"- `{fam}`: {c}")
    lines.append("")

    lines.append("### Common top1 confusions (pred -> gold)")
    lines.append("")
    for k, c in wrong_family.most_common(args.top_n):
        lines.append(f"- `{k}`: {c}")
    lines.append("")

    lines.append("## Worst cases by requests/tool_calls")
    lines.append("")
    for r, tc, qid in hardest[: args.top_n]:
        q = _short(str(gold_by_id[qid].get("query") or ""))
        pred1_raw = (pred_by_id[qid].get("predictions") or [None])[0]
        gold_tools_raw = gold_by_id[qid].get("tools") or []
        gold0 = gold_tools_raw[0] if gold_tools_raw else ""
        lines.append(f"- `{qid}` requests={r} tool_calls={tc} pred1=`{pred1_raw}` gold0=`{gold0}`")
        lines.append(f"  - {q}")
    lines.append("")

    lines.append("## Worst cases by total_tokens")
    lines.append("")
    for tt, r, qid in token_heavy[: args.top_n]:
        q = _short(str(gold_by_id[qid].get("query") or ""))
        pred1_raw = (pred_by_id[qid].get("predictions") or [None])[0]
        gold_tools_raw = gold_by_id[qid].get("tools") or []
        gold0 = gold_tools_raw[0] if gold_tools_raw else ""
        lines.append(f"- `{qid}` total_tokens={tt} requests={r} pred1=`{pred1_raw}` gold0=`{gold0}`")
        lines.append(f"  - {q}")
    lines.append("")

    if examples_empty:
        lines.append("## Empty predictions (IDs)")
        lines.append("")
        for qid in examples_empty[: args.top_n]:
            q = _short(str(gold_by_id[qid].get("query") or ""))
            lines.append(f"- `{qid}` - {q}")
        lines.append("")

    if examples_top10_miss:
        lines.append("## Top10 misses (sample IDs)")
        lines.append("")
        for qid in examples_top10_miss[: args.top_n]:
            q = _short(str(gold_by_id[qid].get("query") or ""))
            lines.append(f"- `{qid}` - {q}")
        lines.append("")

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

