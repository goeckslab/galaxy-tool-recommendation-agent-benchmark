from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Suggest (do not apply) conservative ground-truth expansion candidates for statistics-topic items.\n"
            "Uses tool_help_text + IO details to *discover* plausible alternatives, then outputs a manual-review report."
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
        help="Tool catalog JSONL (must include IO details; helptext-enriched recommended).",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=Path("reports/statistics_expansion_suggestions.md"),
        help="Output Markdown report.",
    )
    p.add_argument(
        "--max-items",
        type=int,
        default=60,
        help="Max items to include in the report.",
    )
    p.add_argument(
        "--top-n",
        type=int,
        default=6,
        help="Top-N alternative tools to suggest per item.",
    )
    p.add_argument(
        "--min-score",
        type=float,
        default=0.25,
        help="Minimum combined score to include a suggestion (0-1).",
    )
    return p.parse_args()


def load_jsonl(path: Path) -> List[dict]:
    out: List[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def normalize_toolshed_base(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def tokenize(text: str) -> List[str]:
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9\\s\\-_/]", " ", text)
    text = re.sub(r"\\s+", " ", text).strip()
    if not text:
        return []
    toks = [t for t in text.split(" ") if t]
    # tiny stoplist, keep it conservative (don't over-normalize)
    stop = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "to",
        "of",
        "in",
        "on",
        "for",
        "with",
        "using",
        "which",
        "what",
        "when",
        "where",
        "why",
        "how",
        "want",
        "need",
        "have",
        "has",
        "had",
        "this",
        "that",
        "these",
        "those",
        "also",
        "then",
        "than",
        "after",
        "before",
        "into",
        "from",
        "across",
        "many",
        "more",
        "most",
        "only",
        "same",
        "new",
        "now",
        "already",
        "working",
        "project",
        "are",
        "can",
        "but",
        "data",
        "dataset",
        "tabular",
        "file",
        "galaxy",
        "tool",
        "model",
        "models",
        "train",
        "training",
        "evaluation",
        "evaluate",
        "predict",
        "prediction",
        "plot",
        "plots",
        "toolshed",
        "psu",
        "edu",
        "repos",
    }
    cleaned: List[str] = []
    for t in toks:
        if t in stop or len(t) < 3:
            continue
        # Drop path-y / id-y tokens; they create lots of false overlap.
        if "/" in t or t.count("_") >= 4:
            continue
        if t.startswith("http") or t.startswith("www"):
            continue
        cleaned.append(t)
    return cleaned


SPECIAL_QUERY_TOKENS = {
    "svm",
    "cnn",
    "rnn",
    "fnn",
    "keras",
    "one-hot",
    "onehot",
    "roc",
    "auc",
    "f1",
    "rmse",
    "r2",
    "xgboost",
    "lightgbm",
    "catboost",
    "grid",
    "cv",
    "cross-validation",
}


def parse_toolshed_id(tool_id: str) -> Optional[Tuple[str, str, str]]:
    # toolshed.g2.bx.psu.edu/repos/<owner>/<repo>/<tool>/<version>
    if not tool_id.startswith("toolshed.g2.bx.psu.edu/repos/"):
        return None
    parts = tool_id.split("/")
    # ['toolshed.g2.bx.psu.edu', 'repos', owner, repo, tool, version]
    if len(parts) < 6:
        return None
    return (parts[2], parts[3], parts[4])


def jaccard(a: Sequence[str], b: Sequence[str]) -> float:
    sa = set(a)
    sb = set(b)
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def io_signature(tool: dict) -> Tuple[Tuple[str, ...], Tuple[str, ...], bool, bool]:
    """
    Return:
      - input param types (from input_params_flat)
      - output extensions (from outputs_raw)
      - has_tabular_input (heuristic: any DataToolParameter with tabular/csv extensions)
      - has_target_column (heuristic: any data_column param)
    """
    input_types: List[str] = []
    output_exts: List[str] = []
    has_tabular_input = False
    has_target_column = False

    ipf = tool.get("input_params_flat")
    if isinstance(ipf, list):
        for x in ipf:
            if not isinstance(x, dict):
                continue
            t = x.get("type")
            if isinstance(t, str) and t.strip():
                input_types.append(t.strip().lower())
            if t == "data_column":
                has_target_column = True

    inputs_raw = tool.get("inputs_raw")
    if isinstance(inputs_raw, list):
        for x in inputs_raw:
            if not isinstance(x, dict):
                continue
            if x.get("type") == "data":
                exts = x.get("extensions")
                if isinstance(exts, list) and any(e in {"tabular", "csv"} for e in exts if isinstance(e, str)):
                    has_tabular_input = True

    outputs_raw = tool.get("outputs_raw")
    if isinstance(outputs_raw, list):
        for x in outputs_raw:
            if not isinstance(x, dict):
                continue
            exts = x.get("extensions")
            if isinstance(exts, list):
                for e in exts:
                    if isinstance(e, str) and e.strip():
                        output_exts.append(e.strip().lower())

    return (tuple(sorted(set(input_types))), tuple(sorted(set(output_exts))), has_tabular_input, has_target_column)


def tool_text(tool: dict) -> str:
    parts: List[str] = []
    # Do NOT include tool_id: it pollutes similarity with path-like tokens.
    for k in ("name", "description", "tool_help_text"):
        v = tool.get(k)
        if isinstance(v, str) and v.strip():
            parts.append(v.strip())

    # Include a limited amount of select-option labels from inputs_raw.
    # This is important for "discovering" alternatives like Tabular Learner -> SVM, where SVM appears as an option label.
    inputs_raw = tool.get("inputs_raw")
    option_labels: List[str] = []

    def walk(node: object) -> None:
        if isinstance(node, dict):
            mc = node.get("model_class")
            if mc == "SelectToolParameter":
                opts = node.get("options")
                if isinstance(opts, list) and 1 <= len(opts) <= 80:
                    for opt in opts:
                        if isinstance(opt, list) and opt:
                            lbl = opt[0]
                            if isinstance(lbl, str) and lbl.strip():
                                option_labels.append(lbl.strip())
            # Conditional blocks
            if node.get("model_class") == "Conditional":
                for c in node.get("cases") or []:
                    walk(c)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(inputs_raw)
    if option_labels:
        # Bound size to keep report stable.
        parts.append(" ".join(option_labels[:120]))

    return " ".join(parts)


@dataclass(frozen=True)
class Suggestion:
    score: float
    tool_id: str
    name: str
    reason: str


def main() -> None:
    args = parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    items = load_jsonl(args.v1)
    stats = [it for it in items if (it.get("metadata") or {}).get("topic") == "statistics"]
    stats.sort(key=lambda x: str(x.get("id") or ""))

    if not args.tool_catalog.exists():
        raise SystemExit(f"Tool catalog not found: {args.tool_catalog}")

    tools = load_jsonl(args.tool_catalog)
    by_id: Dict[str, dict] = {}
    by_base: Dict[str, List[dict]] = defaultdict(list)
    for t in tools:
        tid = t.get("tool_id")
        if isinstance(tid, str) and tid:
            by_id[tid] = t
            by_base[normalize_toolshed_base(tid)].append(t)

    # Precompute tool vectors/signatures and token frequencies (for "rare token" gating),
    # plus an inverted index to avoid scanning the full catalog for every item.
    tool_cache: Dict[str, Tuple[List[str], Tuple[Tuple[str, ...], Tuple[str, ...], bool, bool]]] = {}
    token_freq: Counter[str] = Counter()
    token_to_tools: Dict[str, List[str]] = defaultdict(list)
    for tid, t in by_id.items():
        toks = tokenize(tool_text(t))
        sig = io_signature(t)
        tool_cache[tid] = (toks, sig)
        uniq = sorted(set(toks))
        token_freq.update(uniq)
        for tok in uniq:
            token_to_tools[tok].append(tid)

    # Consider only items without alternatives and with a toolshed gold tool (where alternatives matter).
    candidates = [
        it
        for it in stats
        if not (it.get("metadata") or {}).get("ground_truth_alternatives")
        and len([t for t in (it.get("tools") or []) if isinstance(t, str)]) == 1
        and str((it.get("tools") or [""])[0]).startswith("toolshed.g2.bx.psu.edu/")
    ]

    # Cap report size for practicality (manual review still required).
    candidates = candidates[: max(0, int(args.max_items))]

    lines: List[str] = []
    lines.append("# Statistics expansion suggestions (manual review required)")
    lines.append("")
    lines.append(f"- Items considered: `{len(candidates)}` (subset of statistics items without current alternatives)")
    lines.append(f"- Tool catalog: `{args.tool_catalog}`")
    lines.append(f"- top_n: `{args.top_n}` min_score: `{args.min_score}`")
    lines.append("")
    lines.append(
        "These are *suggestions only*. Do not add alternatives unless you can justify them with IO compatibility + tool_help_text."
    )
    lines.append("")

    for it in candidates:
        qid = str(it.get("id") or "")
        q = str(it.get("query") or "").strip()
        gold = str((it.get("tools") or [""])[0])

        gold_entry = by_id.get(gold)
        if not gold_entry:
            continue

        gold_tokens, gold_sig = tool_cache.get(gold, ([], ((), (), False, False)))
        gold_in_types, gold_out_exts, gold_tabular, gold_target = gold_sig
        query_tokens = tokenize(q)
        gold_parts = parse_toolshed_id(gold)
        gold_owner = gold_parts[0] if gold_parts else None
        gold_repo = gold_parts[1] if gold_parts else None
        gold_family = None
        if gold_repo and "_" in gold_repo:
            gold_family = gold_repo.split("_", 1)[0]

        # Pick a small set of "rare" tokens from the gold tool to gate suggestions.
        # This prevents IO-only matches to unrelated tools.
        generic_rare_stop = {"arguments", "chained", "outputted", "portions", "default", "contains", "expected"}
        rare = []
        for t in set(gold_tokens):
            if not t.isalpha() or len(t) < 4:
                continue
            if t in generic_rare_stop:
                continue
            f = token_freq.get(t, 0)
            if 1 <= f <= 60:
                rare.append(t)
        rare = sorted(rare, key=lambda x: (token_freq.get(x, 0), x))[:12]
        rare_set = set(rare)

        # Query signal tokens: avoid generic question words; keep tokens that are either special
        # (algorithm keywords) or not too common in the tool universe.
        signal_query = [
            t
            for t in query_tokens
            if (t in SPECIAL_QUERY_TOKENS) or (t.isalpha() and len(t) >= 4 and token_freq.get(t, 10_000) <= 300)
        ]
        signal_query_set = set(signal_query)

        # Search space: tools that share at least one rare token with the gold tool.
        # This keeps the suggester fast and reduces IO-only false matches.
        candidate_ids: List[str] = []
        for tok in rare:
            candidate_ids.extend(token_to_tools.get(tok, []))
        candidate_ids = sorted(set(candidate_ids))

        suggestions: List[Suggestion] = []
        for tid in candidate_ids:
            if tid == gold:
                continue
            # Only consider toolshed tools as expansion targets (stable IDs).
            if not tid.startswith("toolshed.g2.bx.psu.edu/"):
                continue
            toks, sig = tool_cache.get(tid, ([], ((), (), False, False)))
            cand_parts = parse_toolshed_id(tid)
            cand_owner = cand_parts[0] if cand_parts else None
            cand_repo = cand_parts[1] if cand_parts else None
            cand_family = None
            if cand_repo and "_" in cand_repo:
                cand_family = cand_repo.split("_", 1)[0]

            in_types, out_exts, has_tabular, has_target = sig

            # Hard filters: keep conservative
            if gold_tabular and not has_tabular:
                continue
            if gold_target and not has_target:
                continue

            # Family filter: prevents most cross-domain noise.
            # Allow cross-owner alternatives only with strong algorithm signal in the query.
            if gold_owner and cand_owner and gold_owner != cand_owner:
                if not (signal_query_set & SPECIAL_QUERY_TOKENS):
                    continue
            if gold_family and cand_family and gold_family != cand_family:
                # allow tabular_learner as an SVM alternative (special case)
                if not (("svm" in signal_query_set) and (cand_repo == "tabular_learner")):
                    continue

            # IO type similarity (coarse)
            io_sim = jaccard(list(gold_in_types), list(in_types))
            if io_sim < 0.2:
                continue

            # Text similarity (semantic hints)
            txt_sim = jaccard(gold_tokens, toks)
            shared_rare = sorted(rare_set & set(toks))
            if rare_set and not shared_rare:
                continue

            # Query relevance gate: at least one meaningful query token must appear in candidate text.
            shared_signal_query = sorted(signal_query_set & set(toks))
            if signal_query_set and not shared_signal_query:
                continue

            # Weighted score (favor IO; text is secondary)
            bonus = min(1.0, len(shared_rare) / 3.0) if shared_rare else 0.0
            score = 0.60 * io_sim + 0.30 * txt_sim + 0.10 * bonus
            if score < float(args.min_score):
                continue

            t = by_id.get(tid, {})
            reason_bits = [
                f"io_sim={io_sim:.2f}",
                f"txt_sim={txt_sim:.2f}",
            ]
            if gold_target:
                reason_bits.append("target_column=yes")
            if gold_tabular:
                reason_bits.append("tabular_input=yes")
            if shared_rare:
                reason_bits.append(f"shared_rare={shared_rare[:8]}")
            if shared_signal_query:
                reason_bits.append(f"shared_query={shared_signal_query[:6]}")
            suggestions.append(
                Suggestion(
                    score=score,
                    tool_id=tid,
                    name=str(t.get("name") or ""),
                    reason=", ".join(reason_bits),
                )
            )

        suggestions.sort(key=lambda s: (-s.score, s.tool_id))
        suggestions = suggestions[: max(0, int(args.top_n))]

        lines.append(f"## `{qid}`")
        lines.append("")
        lines.append(f"- query: {q}")
        lines.append(f"- gold: `{gold}`")
        lines.append(f"- suggestions: `{len(suggestions)}`")
        for s in suggestions:
            lines.append(f"  - `{s.tool_id}` ({s.name}) score={s.score:.2f}")
            lines.append(f"    - why: {s.reason}")
        lines.append("")

    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
