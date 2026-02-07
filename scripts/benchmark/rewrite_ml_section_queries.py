from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def normalize_tool_id(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rewrite Machine Learning section benchmark queries to avoid tool-name leakage."
    )
    parser.add_argument(
        "--v1",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark v1 JSONL (in-place rewrite).",
    )
    parser.add_argument(
        "--tool-sections-file",
        type=Path,
        default=Path("data/tool_catalog/usegalaxy_org_all_by_section.json"),
        help="Tool panel section mapping JSON with 'by_section'.",
    )
    parser.add_argument(
        "--section",
        type=str,
        default="Machine Learning",
        help="Section name to target (default: Machine Learning).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes but do not write.",
    )
    return parser.parse_args()


def load_ml_bases(tool_sections_file: Path, section: str) -> set[str]:
    payload = json.loads(tool_sections_file.read_text(encoding="utf-8"))
    by_section = payload.get("by_section") if isinstance(payload, dict) else None
    if not isinstance(by_section, dict):
        raise ValueError(f"Expected 'by_section' dict in {tool_sections_file}")
    tools = by_section.get(section)
    if not isinstance(tools, list):
        raise ValueError(f"Section {section!r} not found in {tool_sections_file}")
    return {normalize_tool_id(t) for t in tools if isinstance(t, str) and t}


def build_action_map() -> Dict[str, str]:
    # Map base tool IDs to intent phrases (no tool names).
    return {
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical": (
            "convert integer class labels to one-hot/categorical format for machine learning"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config": (
            "define a neural network architecture (layers, activations, inputs/outputs) from a configuration"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder": (
            "build a neural network model from a model configuration"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval": (
            "train and evaluate a neural network model on labeled data"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction": (
            "run inference with a trained model to generate predictions on new data"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline": (
            "build a machine learning pipeline by chaining preprocessing steps and a model"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv": (
            "tune hyperparameters using cross-validation search"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot": (
            "visualize hyperparameter search results with a parallel coordinates plot"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble": (
            "train an ensemble model (e.g., random forest / boosted trees) for classification or regression"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier": (
            "train and evaluate a support vector machine classifier"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear": (
            "fit a generalized linear model for regression"
        ),
        "toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner": (
            "train and compare tabular machine learning models and select the best performer"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier": (
            "train and evaluate a k-nearest neighbors classifier"
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering": (
            "cluster samples based on numeric features (unsupervised learning)"
        ),
        "toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment": (
            "train a tabular deep learning model using a declarative configuration (e.g., classification/regression)"
        ),
        "toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2": (
            "train and evaluate a hyperdimensional computing model for classification"
        ),
    }


_BACKTICK_RE = re.compile(r"`[^`]+`")


def rewrite_query(query: str, action: str) -> str:
    # Always produce a tool-recommendation question without tool-name leakage.
    base = f"I need to {action}. Which Galaxy tool should I use?"
    # If the old query didn't look like a tool-recommendation question, still enforce it.
    # Strip any backticked content.
    if "`" in query:
        return base
    return base


def main() -> None:
    args = parse_args()
    ml_bases = load_ml_bases(args.tool_sections_file, args.section)
    action_map = build_action_map()

    items: List[dict] = []
    with args.v1.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))

    changed: List[Tuple[str, str, str]] = []
    for item in items:
        qid = item.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        tools = item.get("tools") or []
        tool_ids = [t for t in tools if isinstance(t, str)]
        bases = [normalize_tool_id(t) for t in tool_ids]
        if not any(b in ml_bases for b in bases):
            continue

        query = str(item.get("query") or "").strip()
        if "`" not in query:
            continue

        # Choose an action based on the first tool ID (most items are single-tool).
        base = normalize_tool_id(tool_ids[0]) if tool_ids else ""
        action = action_map.get(base)
        if not action:
            # Fallback: generic but still better than leaking a tool name.
            action = "perform this machine learning task"
        new_query = rewrite_query(query, action)
        if new_query != query:
            item["query"] = new_query
            changed.append((qid, query, new_query))

    if args.dry_run:
        print(f"Planned changes: {len(changed)}")
        for qid, old, new in changed[:50]:
            print("----", qid)
            print("OLD:", old)
            print("NEW:", new)
        return

    if changed:
        args.v1.write_text(
            "\n".join(json.dumps(it, ensure_ascii=False) for it in items) + "\n",
            encoding="utf-8",
        )
    print(f"Rewrote {len(changed)} queries in {args.v1}")


if __name__ == "__main__":
    main()

