from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Audit statistics-topic benchmark items for query rewrite needs and ground-truth expansion candidates. "
            "Writes a human-readable Markdown report."
        )
    )
    p.add_argument(
        "--v1",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark v1 JSONL.",
    )
    p.add_argument(
        "--tool-catalog",
        type=Path,
        default=Path("data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl"),
        help="Tool catalog JSONL (prefer the helptext-enriched file).",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=Path("reports/statistics_topic_review.md"),
        help="Output Markdown file.",
    )
    p.add_argument(
        "--max-items",
        type=int,
        default=50,
        help="Max items to list per section.",
    )
    p.add_argument(
        "--expand-samples",
        type=int,
        default=15,
        help="How many expansion candidate items to sample (heuristic).",
    )
    return p.parse_args()


def load_jsonl(path: Path) -> List[dict]:
    items: List[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict):
                items.append(obj)
    return items


def normalize_tool_id(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def is_stable_toolshed_id(tool_id: str) -> bool:
    return tool_id.startswith("toolshed.g2.bx.psu.edu/repos/")


def is_internal_like(tool_id: str) -> bool:
    # Heuristic: Galaxy core tools often look like "Filter1", "Cut1", "join1", etc.
    # We still allow __...__ tools and interactive_tool_* as stable "special IDs".
    if tool_id.startswith("__") and tool_id.endswith("__"):
        return False
    if tool_id.startswith("interactive_tool_"):
        return False
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        return False
    return bool(re.match(r"^[A-Za-z]+\d+$", tool_id))


_PAT_DATASET = re.compile(
    r"\\b(SRR|ERR|DRR|GSE|GSM|PRJ|ENCSR|E\\-MTAB|PXD|ZENODO|http://|https://|"
    r"\\.fastq|\\.fq|\\.bam|\\.cram|\\.fasta|\\.fa|\\.vcf|\\.tsv|\\.csv|\\.txt|\\.gz)\\b",
    re.IGNORECASE,
)


def tokenize(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\\s\\-]", " ", text)
    text = re.sub(r"\\s+", " ", text).strip()
    if not text:
        return []
    return [t for t in text.split(" ") if t]


def jaccard(a: Sequence[str], b: Sequence[str]) -> float:
    sa = set(a)
    sb = set(b)
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def tool_text(tool: dict) -> str:
    parts: List[str] = []
    for k in ("tool_id", "name", "description", "tool_help_text", "help_text"):
        v = tool.get(k)
        if isinstance(v, str) and v.strip():
            parts.append(v.strip())
    return " ".join(parts).strip()


def io_signature(tool: dict) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    input_types: List[str] = []
    output_exts: List[str] = []

    ipf = tool.get("input_params_flat")
    if isinstance(ipf, list):
        for x in ipf:
            if isinstance(x, dict):
                t = x.get("type")
                if isinstance(t, str) and t.strip():
                    input_types.append(t.strip().lower())

    outputs_raw = tool.get("outputs_raw")
    if isinstance(outputs_raw, list):
        for x in outputs_raw:
            if isinstance(x, dict):
                exts = x.get("extensions")
                if isinstance(exts, list):
                    for e in exts:
                        if isinstance(e, str) and e.strip():
                            output_exts.append(e.strip().lower())

    return (tuple(sorted(set(input_types))), tuple(sorted(set(output_exts))))


def main() -> None:
    args = parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    items = load_jsonl(args.v1)
    stats = [it for it in items if (it.get("metadata") or {}).get("topic") == "statistics"]
    tutorial_counts = Counter(str(it.get("tutorial_id") or "") for it in stats)

    # Tool catalog is optional (only needed for expansion suggestions).
    tools_catalog: List[dict] = []
    tools_by_id: Dict[str, dict] = {}
    if args.tool_catalog.exists():
        tools_catalog = load_jsonl(args.tool_catalog)
        for t in tools_catalog:
            tid = t.get("tool_id")
            if isinstance(tid, str) and tid:
                tools_by_id[tid] = t

    issues: Dict[str, List[str]] = defaultdict(list)
    for it in stats:
        qid = str(it.get("id") or "")
        q = str(it.get("query") or "")
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]

        if "`" in q or "perform `" in q or "run `" in q:
            issues["tool_leak_query"].append(qid)
        if "tutorial" in q.lower() or "gtn" in q.lower():
            issues["mentions_tutorial"].append(qid)
        if _PAT_DATASET.search(q):
            issues["dataset_leak_query"].append(qid)
        if q.strip().lower().startswith("which galaxy tool would you recommend"):
            issues["templated_recommend"].append(qid)
        if len(tools) == 0:
            issues["no_tools"].append(qid)
        if len(tools) > 1:
            issues["multi_tools"].append(qid)
        if tools and is_internal_like(tools[0]):
            issues["internal_like_tool_id"].append(qid)

    # Exact duplicates within the same first tool base.
    by_tool: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for it in stats:
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        if not tools:
            continue
        tb = normalize_tool_id(tools[0])
        by_tool[tb].append((str(it.get("id") or ""), str(it.get("query") or "").strip()))
    tools_with_dups: Dict[str, List[Tuple[str, List[str]]]] = {}
    for tb, qs in by_tool.items():
        inv: Dict[str, List[str]] = defaultdict(list)
        for qid, q in qs:
            inv[q].append(qid)
        dups = [(q, ids) for q, ids in inv.items() if q and len(ids) > 1]
        if dups:
            tools_with_dups[tb] = [(q, ids) for q, ids in sorted(dups, key=lambda x: -len(x[1]))]

    # Near-duplicates (token-level) within the same tool base.
    near_dups: List[Tuple[float, str, str, str, str, str]] = []
    for tb, qs in by_tool.items():
        if len(qs) < 2:
            continue
        toks = [(qid, q, tokenize(q)) for qid, q in qs if q]
        for i in range(len(toks)):
            for j in range(i + 1, len(toks)):
                qid_a, qa, ta = toks[i]
                qid_b, qb, tb_tokens = toks[j]
                if qa == qb:
                    continue
                score = jaccard(ta, tb_tokens)
                if score >= 0.8:
                    near_dups.append((score, tb, qid_a, qid_b, qa, qb))
    near_dups.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))

    # Tool spotlight: include a small, explicit section in the report so it's easy to confirm
    # that common ML tools (e.g. SVM) were part of the review, even though this report is mostly summary-level.
    spotlight_bases = {
        "sklearn_svm_classifier": "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier",
    }
    spotlight: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    for it in stats:
        qid = str(it.get("id") or "")
        q = str(it.get("query") or "").strip()
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        for t in tools:
            tb = normalize_tool_id(t)
            for name, base in spotlight_bases.items():
                if tb.startswith(base):
                    spotlight[name].append((qid, t, q))

    # Expansion suggestions: sample items that are "single-tool" and have catalog entries with tool_help_text.
    expand_items: List[dict] = []
    for it in stats:
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        if len(tools) != 1:
            continue
        if it.get("metadata", {}).get("ground_truth_alternatives"):
            continue
        tool_id = tools[0]
        if not is_stable_toolshed_id(tool_id):
            continue
        tool_entry = tools_by_id.get(tool_id)
        if not tool_entry:
            continue
        ht = tool_entry.get("tool_help_text") or tool_entry.get("help_text")
        if not isinstance(ht, str) or not str(ht or "").strip():
            continue
        expand_items.append(it)

    # Deterministic sample (by id).
    expand_items.sort(key=lambda x: str(x.get("id") or ""))
    expand_items = expand_items[: max(0, int(args.expand_samples))]

    lines: List[str] = []
    lines.append("# Statistics topic review")
    lines.append("")
    lines.append(f"- Items scanned: `{len(stats)}`")
    lines.append(f"- Tool catalog used: `{args.tool_catalog}` (exists={args.tool_catalog.exists()})")
    lines.append(f"- Tutorials scanned: `{len(tutorial_counts)}`")
    lines.append("")

    lines.append("## Tutorials in scope")
    lines.append("")
    for tid, n in tutorial_counts.most_common():
        if not tid:
            continue
        lines.append(f"- `{tid}`: `{n}` items")
    lines.append("")

    lines.append("## Rewrite audit (rule-based signals)")
    lines.append("")
    for k, v in sorted(issues.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines.append(f"- `{k}`: `{len(v)}`")
    lines.append("")

    if spotlight:
        lines.append("## Tool spotlight (sanity-check)")
        lines.append("")
        for name in sorted(spotlight.keys()):
            rows = sorted(spotlight[name], key=lambda x: x[0])
            lines.append(f"### `{name}`")
            lines.append("")
            lines.append(f"- Items: `{len(rows)}`")
            for qid, tool_id, q in rows[: min(args.max_items, len(rows))]:
                q_short = q if len(q) <= 200 else q[:200] + "…"
                lines.append(f"- `{qid}`")
                lines.append(f"  - tool: `{tool_id}`")
                lines.append(f"  - query: {q_short}")
            lines.append("")

    lines.append("### Exact duplicate query texts under the same tool")
    lines.append("")
    lines.append(f"- Tools with duplicates: `{len(tools_with_dups)}`")
    for tb, dups in list(tools_with_dups.items())[: min(args.max_items, len(tools_with_dups))]:
        lines.append(f"- `{tb}`")
        for q, ids in dups[:3]:
            lines.append(f"  - ({len(ids)} items) ids={ids}")
            lines.append(f"    - query: {q}")
    lines.append("")

    lines.append("### Near-duplicate query texts under the same tool (token Jaccard)")
    lines.append("")
    lines.append(f"- Pairs (>=0.80): `{len(near_dups)}`")
    for score, tb, a, b, qa, qb in near_dups[: min(args.max_items, len(near_dups))]:
        qa_short = qa if len(qa) <= 200 else qa[:200] + "…"
        qb_short = qb if len(qb) <= 200 else qb[:200] + "…"
        lines.append(f"- `{tb}` score={score:.2f} ids=(`{a}`, `{b}`)")
        lines.append(f"  - A: {qa_short}")
        lines.append(f"  - B: {qb_short}")
    lines.append("")

    def list_ids(title: str, key: str) -> None:
        ids = issues.get(key, [])
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"- Count: `{len(ids)}`")
        for qid in ids[: min(args.max_items, len(ids))]:
            lines.append(f"- `{qid}`")
        lines.append("")

    list_ids("Needs rewrite: tool leakage in query", "tool_leak_query")
    list_ids("Needs rewrite: templated phrasing", "templated_recommend")
    list_ids("Check: internal-like tool IDs", "internal_like_tool_id")
    list_ids("Check: multi-tool ground truth (manual review)", "multi_tools")

    expanded = [it for it in stats if (it.get("metadata") or {}).get("ground_truth_alternatives")]
    if expanded:
        lines.append("## Ground truth: manual alternatives present")
        lines.append("")
        lines.append(f"- Count: `{len(expanded)}`")
        lines.append("")
        for it in sorted(expanded, key=lambda x: str(x.get('id') or ''))[: min(args.max_items, len(expanded))]:
            qid = str(it.get("id") or "")
            q = str(it.get("query") or "").strip()
            tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
            note = str((it.get("metadata") or {}).get("ground_truth_alternatives_note") or "").strip()
            lines.append(f"- `{qid}`")
            lines.append(f"  - tools: {tools}")
            if q:
                lines.append(f"  - query: {q}")
            if note:
                lines.append(f"  - note: {note}")
        lines.append("")

    lines.append("## Ground-truth expansion (needs manual review)")
    lines.append("")
    lines.append(
        "This project’s expansion skill is intentionally conservative: **do not auto-expand** based on loose similarity."
    )
    lines.append("Use IO details + help text to manually justify any alternative.")
    lines.append("")
    if not tools_catalog:
        lines.append("- Tool catalog not found; build a helptext-enriched catalog first.")
    elif not expand_items:
        lines.append("- No sampled items found with tool_help_text available in the catalog.")
    else:
        lines.append(
            "Sample items that look eligible for manual expansion review (single-tool gold, toolshed tool, tool_help_text present):"
        )
        lines.append("")
        for it in expand_items:
            qid = str(it.get("id") or "")
            q = str(it.get("query") or "").strip()
            tool_id = str((it.get("tools") or [""])[0])
            lines.append(f"- `{qid}`")
            lines.append(f"  - query: {q}")
            lines.append(f"  - gold: `{tool_id}`")
            gold_entry = tools_by_id.get(tool_id)
            if gold_entry:
                sig_in, sig_out = io_signature(gold_entry)
                lines.append(f"  - io: inputs={list(sig_in)[:8]} outputs={list(sig_out)[:8]}")
                ht = gold_entry.get("tool_help_text") or gold_entry.get("help_text") or ""
                lines.append(f"  - tool_help_text: present (len={len(str(ht))})")
            else:
                lines.append("  - catalog entry: missing")
        lines.append("")

    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
