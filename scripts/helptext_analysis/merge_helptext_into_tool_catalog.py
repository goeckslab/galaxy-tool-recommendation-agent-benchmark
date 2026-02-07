from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, Optional


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Merge tool help text (TSV) into a tool catalog JSONL by tool_id (exact match). "
            "Writes a new JSONL file with an added tool_help_text field."
        )
    )
    p.add_argument(
        "--helptext-tsv",
        type=Path,
        default=Path("scripts/helptext_analysis/data/tools_helptext.tsv"),
        help="TSV with columns: tool_id, help_text.",
    )
    p.add_argument(
        "--catalog-jsonl",
        type=Path,
        required=True,
        help="Input tool catalog JSONL (each line is a tool dict with tool_id).",
    )
    p.add_argument(
        "--output-jsonl",
        type=Path,
        required=True,
        help="Output JSONL with merged tool_help_text field.",
    )
    p.add_argument(
        "--field",
        type=str,
        default="tool_help_text",
        help="Field name to store the merged help text (default: tool_help_text).",
    )
    p.add_argument(
        "--by-section-json",
        type=Path,
        default=None,
        help=(
            "Optional JSON file with a 'by_section' mapping (e.g. data/tool_catalog/usegalaxy_org_all_by_section.json). "
            "If provided, the output JSONL will also be enriched with panel section metadata."
        ),
    )
    p.add_argument(
        "--section-field",
        type=str,
        default="panel_section_name",
        help="Field name to store the tool panel section name when --by-section-json is used (default: panel_section_name).",
    )
    p.add_argument(
        "--also-set-category-and-section",
        action="store_true",
        default=True,
        help=(
            "When enriching with panel sections, also set 'category' and 'section' aliases to the same value "
            "(enabled by default)."
        ),
    )
    p.add_argument(
        "--no-also-set-category-and-section",
        action="store_false",
        dest="also_set_category_and_section",
        help="Disable setting 'category' and 'section' aliases when enriching with panel sections.",
    )
    p.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output if it already exists.",
    )
    return p.parse_args()


def load_helptext_map(path: Path) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if not reader.fieldnames or "tool_id" not in reader.fieldnames or "help_text" not in reader.fieldnames:
            raise ValueError(f"Unexpected TSV header in {path} (need: tool_id, help_text)")
        for row in reader:
            tool_id = (row.get("tool_id") or "").strip()
            help_text = row.get("help_text") or ""
            if not tool_id:
                continue
            if help_text and help_text.strip():
                mapping[tool_id] = help_text
    return mapping


def iter_jsonl(path: Path) -> Iterable[dict]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict):
                yield obj


def load_tool_section_map(path: Path) -> Dict[str, str]:
    """
    Load a mapping of tool_id -> panel section name from a by-section JSON payload.
    Expected shape: {"by_section": {"Section Name": ["tool_id", ...], ...}, ...}
    """
    payload = json.loads(path.read_text(encoding="utf-8"))
    by_section = payload.get("by_section") if isinstance(payload, dict) else None
    if not isinstance(by_section, dict):
        raise ValueError(f"Unexpected by-section JSON format in {path} (missing 'by_section' dict)")
    tool_to_section: Dict[str, str] = {}
    for section_name, tool_ids in by_section.items():
        if not isinstance(section_name, str) or not section_name:
            continue
        if not isinstance(tool_ids, list):
            continue
        for tid in tool_ids:
            if isinstance(tid, str) and tid and tid not in tool_to_section:
                tool_to_section[tid] = section_name
    return tool_to_section


def main() -> None:
    args = parse_args()
    if args.output_jsonl.exists() and not args.overwrite:
        raise SystemExit(f"Refusing to overwrite existing file: {args.output_jsonl} (pass --overwrite)")

    help_map = load_helptext_map(args.helptext_tsv)
    section_map: Optional[Dict[str, str]] = None
    if args.by_section_json is not None:
        section_map = load_tool_section_map(args.by_section_json)

    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    matched = 0
    total = 0
    section_enriched = 0
    with args.output_jsonl.open("w", encoding="utf-8") as out:
        for tool in iter_jsonl(args.catalog_jsonl):
            total += 1
            tool_id = str(tool.get("tool_id") or "")
            ht: Optional[str] = help_map.get(tool_id)
            if ht is not None:
                tool[args.field] = ht
                matched += 1
            else:
                # Keep the output schema stable: always include the helptext field
                # even if we don't have non-empty helptext for this tool.
                tool.setdefault(args.field, "")
            if section_map is not None and tool_id:
                sec = section_map.get(tool_id)
                if sec:
                    tool[args.section_field] = sec
                    if args.also_set_category_and_section:
                        tool.setdefault("category", sec)
                        tool.setdefault("section", sec)
                    section_enriched += 1
            out.write(json.dumps(tool, ensure_ascii=False) + "\n")

    print(
        json.dumps(
            {
                "catalog": str(args.catalog_jsonl),
                "output": str(args.output_jsonl),
                "total_tools": total,
                "matched_helptext": matched,
                "helptext_rows": len(help_map),
                "field": args.field,
                "section_rows": len(section_map) if section_map is not None else 0,
                "section_enriched": section_enriched,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
