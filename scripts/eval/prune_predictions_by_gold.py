from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Prune a predictions JSONL file to only include IDs present in the gold JSONL file. "
            "This is useful when the benchmark file has been filtered but an older run's "
            "predictions.jsonl still contains extra query IDs."
        )
    )
    p.add_argument(
        "--gold",
        type=Path,
        required=True,
        help="Gold benchmark JSONL (each line contains an 'id').",
    )
    p.add_argument(
        "--predictions",
        type=Path,
        required=True,
        help="Predictions JSONL to prune (each line contains an 'id').",
    )
    p.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite --predictions in place (default: write to --output).",
    )
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output path (required unless --in-place is set).",
    )
    p.add_argument(
        "--backup",
        action="store_true",
        help="When using --in-place, write a .bak copy next to the original first.",
    )
    return p.parse_args()


def _iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict):
                yield obj


def _load_gold_ids(path: Path) -> Set[str]:
    ids: Set[str] = set()
    for obj in _iter_jsonl(path):
        qid = obj.get("id")
        if isinstance(qid, str) and qid:
            ids.add(qid)
    return ids


def main() -> None:
    args = parse_args()
    gold_ids = _load_gold_ids(args.gold)
    if not gold_ids:
        raise SystemExit(f"No gold IDs found in {args.gold}")

    if args.in_place:
        out_path = args.predictions
        if args.backup:
            bak = args.predictions.with_suffix(args.predictions.suffix + ".bak")
            bak.write_text(args.predictions.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        if args.output is None:
            raise SystemExit("--output is required unless --in-place is set")
        out_path = args.output

    kept: List[Dict[str, Any]] = []
    total = 0
    missing_id = 0
    for obj in _iter_jsonl(args.predictions):
        total += 1
        qid = obj.get("id")
        if not isinstance(qid, str) or not qid:
            missing_id += 1
            continue
        if qid in gold_ids:
            kept.append(obj)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        "\n".join(json.dumps(o, ensure_ascii=False) for o in kept) + ("\n" if kept else ""),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "gold": str(args.gold),
                "predictions": str(args.predictions),
                "output": str(out_path),
                "gold_ids": len(gold_ids),
                "total_records": total,
                "kept_records": len(kept),
                "dropped_records": total - len(kept),
                "records_missing_id": missing_id,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

