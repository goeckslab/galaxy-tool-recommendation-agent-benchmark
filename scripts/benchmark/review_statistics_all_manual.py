from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Generate a per-item manual review report for ALL statistics-topic benchmark items, "
            "including rewrite signals and ground-truth expansion status, and linking each item "
            "to GTN tutorial context in the local training-material clone."
        )
    )
    p.add_argument(
        "--v1",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark v1 JSONL.",
    )
    p.add_argument(
        "--gtn-root",
        type=Path,
        default=Path("training-material"),
        help="Local clone of galaxyproject/training-material.",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=Path("reports/statistics_all_manual_review.md"),
        help="Output Markdown file.",
    )
    p.add_argument(
        "--max-hits",
        type=int,
        default=3,
        help="Max tutorial.md hits to display per item.",
    )
    return p.parse_args()


_PAT_DATASET = re.compile(
    r"\\b(SRR|ERR|DRR|GSE|GSM|PRJ|ENCSR|E\\-MTAB|PXD|ZENODO|http://|https://|"
    r"\\.fastq|\\.fq|\\.bam|\\.cram|\\.fasta|\\.fa|\\.vcf|\\.tsv|\\.csv|\\.txt|\\.gz)\\b",
    re.IGNORECASE,
)


def load_jsonl(path: Path) -> List[dict]:
    items: List[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def normalize_toolshed_base(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def core_tool_hint(tool_id: str) -> Optional[str]:
    # GTN tutorials often mention core tools by display name rather than tool_id.
    return {
        "Remove beginning1": "Remove beginning",
        "Filter1": "Filter",
        "Cut1": "Cut",
        "join1": "Join two Datasets",
        "Show beginning1": "Select first",
    }.get(tool_id)


def find_in_file(path: Path, patterns: Iterable[str]) -> List[Tuple[int, str]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    hits: List[Tuple[int, str]] = []
    for idx, line in enumerate(lines, start=1):
        for pat in patterns:
            if pat and pat in line:
                hits.append((idx, line.strip()))
                break
    return hits


def rewrite_signals(query: str) -> Dict[str, bool]:
    q = query or ""
    ql = q.lower()
    return {
        "tool_leak_backticks": ("`" in q) or ("perform `" in q) or ("run `" in q),
        "templated_recommend": ql.startswith("which galaxy tool would you recommend"),
        "mentions_tutorial": ("tutorial" in ql) or ("gtn" in ql),
        "mentions_specific_dataset": bool(_PAT_DATASET.search(q)),
    }


def is_internal_like(tool_id: str) -> bool:
    if tool_id.startswith("__") and tool_id.endswith("__"):
        return False
    if tool_id.startswith("interactive_tool_"):
        return False
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        return False
    return bool(re.match(r"^[A-Za-z]+\d+$", tool_id))


def main() -> None:
    args = parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    items = load_jsonl(args.v1)
    stats = [it for it in items if (it.get("metadata") or {}).get("topic") == "statistics"]
    stats.sort(key=lambda x: str(x.get("id") or ""))

    tutorial_counts = Counter(str(it.get("tutorial_id") or "") for it in stats)
    signal_counts = Counter()
    internal_like_ids: List[str] = []
    expanded_ids: List[str] = []

    # Precompute signals for summary
    signals_by_id: Dict[str, Dict[str, bool]] = {}
    for it in stats:
        qid = str(it.get("id") or "")
        sig = rewrite_signals(str(it.get("query") or ""))
        signals_by_id[qid] = sig
        for k, v in sig.items():
            if v:
                signal_counts[k] += 1
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        if tools and is_internal_like(tools[0]):
            internal_like_ids.append(qid)
        if (it.get("metadata") or {}).get("ground_truth_alternatives"):
            expanded_ids.append(qid)

    lines: List[str] = []
    lines.append("# Statistics topic manual review (all tutorials)")
    lines.append("")
    lines.append(f"- Items: `{len(stats)}`")
    lines.append(f"- Tutorials: `{len(tutorial_counts)}`")
    lines.append(f"- GTN root: `{args.gtn_root}` (exists={args.gtn_root.exists()})")
    lines.append("")

    lines.append("## Tutorials in scope")
    lines.append("")
    for tid, n in tutorial_counts.most_common():
        if tid:
            lines.append(f"- `{tid}`: `{n}` items")
    lines.append("")

    lines.append("## Rewrite signals (should be 0 for a clean benchmark)")
    lines.append("")
    for k in sorted(["tool_leak_backticks", "templated_recommend", "mentions_tutorial", "mentions_specific_dataset"]):
        lines.append(f"- `{k}`: `{signal_counts.get(k, 0)}`")
    lines.append("")
    lines.append(f"- internal-like core tool IDs (first tool): `{len(internal_like_ids)}`")
    lines.append(f"- items with manual ground-truth alternatives: `{len(expanded_ids)}`")
    lines.append("")

    lines.append("## Per-item review")
    lines.append("")

    for it in stats:
        qid = str(it.get("id") or "")
        tutorial_id = str(it.get("tutorial_id") or "")
        query = str(it.get("query") or "").strip()
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        md = it.get("metadata") or {}
        has_alt = bool(md.get("ground_truth_alternatives"))
        alt_note = str(md.get("ground_truth_alternatives_note") or "").strip()
        sig = signals_by_id.get(qid, {})

        lines.append(f"### `{qid}`")
        lines.append("")
        lines.append(f"- tutorial: `{tutorial_id}`")
        if query:
            lines.append(f"- query: {query}")
        lines.append(f"- tools: {tools}")
        lines.append(f"- rewrite_needed: `{any(sig.values())}`")
        if any(sig.values()):
            flagged = [k for k, v in sig.items() if v]
            lines.append(f"- rewrite_flags: {flagged}")
        lines.append(f"- ground_truth_alternatives: `{has_alt}`")
        if alt_note:
            lines.append(f"- alternatives_note: {alt_note}")

        # Tutorial context hits
        tutorial_md = args.gtn_root / tutorial_id / "tutorial.md"
        if tutorial_md.exists():
            patterns: List[str] = []
            for t in tools:
                patterns.append(t)
                patterns.append(normalize_toolshed_base(t))
                hint = core_tool_hint(t)
                if hint:
                    patterns.append(hint)
            patterns = [p for p in patterns if p]
            hits = find_in_file(tutorial_md, patterns)
            if hits:
                lines.append(f"- tutorial.md hits: `{len(hits)}` (showing up to {args.max_hits})")
                for ln, text in hits[: max(0, int(args.max_hits))]:
                    short = text if len(text) <= 220 else text[:220] + "…"
                    lines.append(f"  - `{tutorial_md}:{ln}`: {short}")
            else:
                lines.append("- tutorial.md hits: `0` (tool may be referenced by display name or older version)")
        else:
            lines.append(f"- tutorial.md: missing (`{tutorial_md}`)")
        lines.append("")

    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
