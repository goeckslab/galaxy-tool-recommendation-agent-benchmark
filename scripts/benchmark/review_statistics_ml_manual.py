from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Create a human-readable manual-review report for statistics-topic machine-learning tutorials, "
            "linking benchmark items to GTN tutorial context and summarizing any manual ground-truth expansions."
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
        default=Path("reports/statistics_ml_manual_review.md"),
        help="Output Markdown file.",
    )
    return p.parse_args()


ML_TUTORIALS = {
    "topics/statistics/tutorials/CNN",
    "topics/statistics/tutorials/FNN",
    "topics/statistics/tutorials/RNN",
    "topics/statistics/tutorials/intro_deep_learning",
    "topics/statistics/tutorials/fruit_360",
    "topics/statistics/tutorials/age-prediction-with-ml",
    "topics/statistics/tutorials/classification_machinelearning",
    "topics/statistics/tutorials/classification_regression",
    "topics/statistics/tutorials/regression_machinelearning",
    "topics/statistics/tutorials/clustering_machinelearning",
    "topics/statistics/tutorials/hyperdimensional_computing",
    "topics/statistics/tutorials/galaxy-ludwig",
    "topics/statistics/tutorials/machinelearning",
}


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
    # toolshed ids are .../<tool>/<version> ; strip the final segment for matching tutorial markdown
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


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


def core_tool_hint(tool_id: str) -> Optional[str]:
    # Tutorials often refer to core tools by display name, not by id.
    if tool_id == "Remove beginning1":
        return "Remove beginning"
    if tool_id == "Filter1":
        return "Filter"
    if tool_id == "Cut1":
        return "Cut"
    if tool_id == "join1":
        return "Join two Datasets"
    if tool_id == "Show beginning1":
        return "Select first"
    return None


def main() -> None:
    args = parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    items = load_jsonl(args.v1)
    ml_items: List[dict] = []
    for it in items:
        md = it.get("metadata") or {}
        if md.get("topic") == "statistics" and it.get("tutorial_id") in ML_TUTORIALS:
            ml_items.append(it)

    ml_items.sort(key=lambda x: str(x.get("id") or ""))
    tutorial_counts = Counter(str(it.get("tutorial_id") or "") for it in ml_items)

    lines: List[str] = []
    lines.append("# Statistics ML manual review")
    lines.append("")
    lines.append(f"- Items: `{len(ml_items)}`")
    lines.append(f"- Tutorials: `{len(tutorial_counts)}`")
    lines.append(f"- GTN root: `{args.gtn_root}` (exists={args.gtn_root.exists()})")
    lines.append("")

    lines.append("## Tutorials in scope")
    lines.append("")
    for tid, n in tutorial_counts.most_common():
        if tid:
            lines.append(f"- `{tid}`: `{n}` items")
    lines.append("")

    lines.append("## Per-item notes")
    lines.append("")
    for it in ml_items:
        qid = str(it.get("id") or "")
        tutorial_id = str(it.get("tutorial_id") or "")
        q = str(it.get("query") or "").strip()
        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        md = it.get("metadata") or {}
        note = str(md.get("ground_truth_alternatives_note") or "").strip()
        has_alt = bool(md.get("ground_truth_alternatives"))

        lines.append(f"### `{qid}`")
        lines.append("")
        lines.append(f"- tutorial: `{tutorial_id}`")
        if q:
            lines.append(f"- query: {q}")
        if tools:
            lines.append(f"- gold tools: {tools}")
        lines.append(f"- alternatives added: `{has_alt}`")
        if note:
            lines.append(f"- note: {note}")
        if not has_alt:
            lines.append("- decision: keep single-tool gold (no safe alternative identified during manual review)")

        tutorial_md = args.gtn_root / tutorial_id / "tutorial.md"
        if not tutorial_md.exists():
            lines.append(f"- tutorial.md: missing (`{tutorial_md}`)")
            lines.append("")
            continue

        # Try to locate tool mentions in the tutorial.
        patterns: List[str] = []
        for t in tools:
            hint = core_tool_hint(t)
            if hint:
                patterns.append(hint)
            patterns.append(normalize_toolshed_base(t))
        # Also include the bare tool id for toolshed tools in case the tutorial uses the same version.
        patterns.extend([t for t in tools if t.startswith("toolshed.g2.bx.psu.edu/")])
        patterns = [p for p in patterns if p]

        hits = find_in_file(tutorial_md, patterns)
        if hits:
            lines.append(f"- tutorial.md hits: `{len(hits)}` (showing up to 3)")
            for ln, text in hits[:3]:
                short = text if len(text) <= 220 else text[:220] + "…"
                lines.append(f"  - `{tutorial_md}:{ln}`: {short}")
        else:
            lines.append("- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)")
        lines.append("")

    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
