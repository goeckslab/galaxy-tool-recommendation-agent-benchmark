from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Apply conservative, manually-justified ground-truth expansions for statistics-topic items "
            "and (optionally) bump a small set of tool versions to the latest installed on usegalaxy.org. "
            "Edits v1_items.jsonl in-place."
        )
    )
    p.add_argument(
        "--v1",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark v1 JSONL (in-place update).",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes but do not write.",
    )
    return p.parse_args()


# Keep these changes tiny and explicit (manual review only).
# We only bump a few text_processing tools where usegalaxy.org has a clear "latest" in the catalog.
VERSION_UPDATES: Dict[str, str] = {
    "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2": (
        "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3"
    ),
    "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2": (
        "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3"
    ),
    "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy2": (
        "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3"
    ),
    "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_replace_in_column/9.5+galaxy2": (
        "toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_replace_in_column/9.5+galaxy3"
    ),
}


# Manual expansions: id -> (additional_tools, note).
# Notes should reference why the alternative is equivalent (IO/intent), not just "similar".
EXPANSIONS: Dict[str, Tuple[List[str], str]] = {
    "statistics-flexynesis_classification-q016": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3"],
        (
            "Manual: both tools perform a key-based join of two tabular datasets into a single table. "
            "The text_processing EasyJoin variant is an acceptable alternative when you need more control over "
            "which columns are kept from each input."
        ),
    ),
    "statistics-flexynesis_classification-q017": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy3"],
        (
            "Manual: both tools output the first N lines of a dataset for quick inspection (head/select-first). "
            "Either is appropriate for sanity-checking a table before analysis."
        ),
    ),
    "statistics-gpu_jupyter_lab-q012": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_grep_tool/9.5+galaxy3"],
        (
            "Manual: for dropping rows based on a keyword/category in a column, a grep-style filter "
            "(keeping or excluding matching lines) is also valid in addition to the generic column filter tool."
        ),
    ),
    "statistics-gpu_jupyter_lab-q015": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3"],
        "Manual: selecting/reordering columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.",
    ),
    "statistics-gpu_jupyter_lab-q016": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3"],
        "Manual: selecting/reordering columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.",
    ),
    "statistics-gpu_jupyter_lab-q017": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3"],
        "Manual: selecting a contiguous block of columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.",
    ),
    "statistics-gpu_jupyter_lab-q018": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3"],
        "Manual: extracting the first few metadata columns is a column-selection task supported by both core Cut and text_processing Cut.",
    ),

    # ML tutorials: removing a header line can also be expressed as a simple sed transform.
    "statistics-classification_machinelearning-q018": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3"],
        (
            "Manual: this step removes the first line (header) from a tabular file. "
            "A sed-based text transformation can delete the first line (e.g., '1d'), "
            "so it is a valid alternative to the dedicated 'Remove beginning' tool."
        ),
    ),
    "statistics-regression_machinelearning-q016": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3"],
        (
            "Manual: this step removes the first line (header) from a tabular file. "
            "A sed-based text transformation can delete the first line (e.g., '1d'), "
            "so it is a valid alternative to the dedicated 'Remove beginning' tool."
        ),
    ),

    # ML tutorial: column extraction with Advanced Cut is equivalent to core Cut for selecting column 3.
    "statistics-fruit_360-q011": (
        ["Cut1"],
        (
            "Manual: the tutorial uses Advanced Cut to keep a specific column from a tabular dataset. "
            "Galaxy's core Cut tool can also select a specific column (e.g., column 3), so it is an acceptable alternative."
        ),
    ),

    # ML: SVM classifier can be trained via Tabular Learner by restricting the compared models to SVM.
    "statistics-classification_machinelearning-q014": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). "
            "If you restrict the compared models to SVM only, it can serve as an alternative way to train an SVM classifier "
            "on tabular data with reproducible splits via the random seed and (optionally) a sample ID column."
        ),
    ),
    "statistics-classification_regression-q011": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). "
            "Restricting the compared models to SVM only provides an SVM-classifier training path comparable in intent "
            "to the dedicated SVM classifier tool for tabular inputs."
        ),
    ),
    "statistics-machinelearning-q011": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). "
            "When configured to compare only SVM models, it can train an SVM and report evaluation metrics, making it "
            "an acceptable alternative for SVM-focused classification on tabular data."
        ),
    ),

    # ML: many sklearn_* algorithm-specific trainers can be replicated in Tabular Learner by restricting the model set.
    "statistics-classification_machinelearning-q011": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports classification on tabular data and includes a Logistic Regression option. "
            "If you restrict the compared models to Logistic Regression only, it matches this interpretable linear/logistic intent."
        ),
    ),
    "statistics-regression_machinelearning-q011": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports regression on tabular data and includes a Linear Regression option. "
            "Restricting the compared models to Linear Regression only matches this generalized linear model training intent."
        ),
    ),
    "statistics-classification_machinelearning-q013": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports classification and includes a K Neighbors Classifier option. "
            "Restricting the compared models to KNN only matches this k-nearest neighbors classification intent."
        ),
    ),
    "statistics-classification_machinelearning-q015": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner can evaluate multiple tabular ML models and includes several ensemble classifiers "
            "(e.g., Random Forest / Gradient Boosting / XGBoost / LightGBM / CatBoost). "
            "It is an acceptable alternative when the goal is to fit and evaluate an ensemble model (or compare methods) on tabular data."
        ),
    ),
    "statistics-classification_regression-q013": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports both classification and regression and includes multiple ensemble options "
            "(e.g., Random Forest / Gradient Boosting / XGBoost / LightGBM / CatBoost). "
            "When configured accordingly, it matches this ensemble training + evaluation intent on tabular data."
        ),
    ),
    "statistics-regression_machinelearning-q013": (
        ["toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"],
        (
            "Manual: Tabular Learner supports regression and includes several tree-based ensemble regressors "
            "(e.g., Random Forest / Gradient Boosting / XGBoost / LightGBM / CatBoost). "
            "Restricting to the desired ensemble family matches this tree-based regression intent."
        ),
    ),

    # Performance plots: Plotly performance plots ↔ ML visualization extension (both support ROC/PR style plots).
    "statistics-classification_machinelearning-q012": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0"],
        (
            "Manual: ML Visualization Extension outputs Plotly-based ML performance plots, including precision-recall and ROC curves. "
            "It is an acceptable alternative for interactive classification-performance summaries."
        ),
    ),
    "statistics-classification_regression-q012": (
        ["toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0"],
        (
            "Manual: ML Visualization Extension outputs Plotly-based ML performance plots, including precision-recall and ROC curves. "
            "It is an acceptable alternative when the goal is to visualize classification performance across metrics."
        ),
    ),
}


def update_tools_list(tools: List[str]) -> Tuple[List[str], bool]:
    changed = False
    out: List[str] = []
    for t in tools:
        if t in VERSION_UPDATES:
            out.append(VERSION_UPDATES[t])
            changed = True
        else:
            out.append(t)
    return out, changed


def main() -> None:
    args = parse_args()
    items: List[dict] = []
    with args.v1.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))

    rewrites = 0
    expansions = 0
    for it in items:
        md = it.get("metadata") or {}
        if md.get("topic") != "statistics":
            continue

        tools = [t for t in (it.get("tools") or []) if isinstance(t, str)]
        new_tools, bumped = update_tools_list(tools)
        if bumped:
            it["tools"] = new_tools
            tools = new_tools
            rewrites += 1

        qid = str(it.get("id") or "")
        if qid not in EXPANSIONS:
            continue

        add_tools, note = EXPANSIONS[qid]
        added_any = False
        for t in add_tools:
            if t not in tools:
                tools.append(t)
                added_any = True
        if not added_any:
            continue

        it["tools"] = tools
        md = dict(md)
        md["ground_truth_alternatives"] = True
        md["ground_truth_alternatives_note"] = note
        it["metadata"] = md
        expansions += 1

    if args.dry_run:
        print(f"Would bump tool versions in {rewrites} statistics items and add expansions to {expansions} items.")
        return

    with args.v1.open("w", encoding="utf-8") as handle:
        for it in items:
            handle.write(json.dumps(it, ensure_ascii=False) + "\n")

    print(f"Updated {args.v1}: version-bumped={rewrites}, expanded={expansions}")


if __name__ == "__main__":
    main()
