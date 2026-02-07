from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Tuple


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Apply manual, non-templated rewrites for statistics-topic queries that leak tool names/IDs "
            "(e.g., backticks) or are template-like. Updates v1_items.jsonl in-place."
        )
    )
    p.add_argument(
        "--v1",
        type=Path,
        default=Path("data/benchmark/v1_items.jsonl"),
        help="Benchmark v1 JSONL (in-place rewrite).",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes but do not write.",
    )
    return p.parse_args()


# NOTE: These are intentionally handwritten (not generated from a template).
# They avoid tool/tutorial/dataset leakage and aim to sound like real user queries.
REWRITES: Dict[str, str] = {
    # PAPAA / pan-cancer pathway activity (interactive Python)
    "statistics-aberrant_pi3k_pathway_analysis-q011": (
        "I have gene expression data together with mutation and copy-number status across many cancer types. "
        "I want to train a classifier that predicts aberrant PI3K-pathway activity and evaluate it with AUROC/AUPR. "
        "Which Galaxy tool should I use if I want to do this interactively in Python?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q012": (
        "I trained a pan-cancer model and now want to assess how well it works within a single cancer type "
        "(and compare performance across cohorts). Which Galaxy tool should I use for an interactive Python workflow?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q013": (
        "I built several related models (different gene sets and cohort selections) and want to compare their "
        "performance curves and key features side-by-side. Which Galaxy tool should I use to explore this in Python?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q014": (
        "I have a trained model and need to score a new cohort to produce per-sample pathway-activity predictions "
        "(including decision scores). What Galaxy tool should I use if I want to run this in a notebook?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q015": (
        "After training a classifier, I want to understand why it makes certain calls (feature weights/ranks) "
        "and generate a few diagnostic plots. Which Galaxy tool should I use for interactive Python analysis?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q016": (
        "I have a table of mutations per sample and need to standardize/annotate mutations into classes that can be "
        "used as labels or covariates in downstream modeling. Which Galaxy tool should I use if I want to do this in Python?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q017": (
        "I want to explore which alternative genes in a pathway might explain a phenotype, and I need to inspect "
        "pathway-level summaries and candidate gene lists interactively. Which Galaxy tool should I use in Galaxy?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q018": (
        "I want to make heatmaps summarizing pathway-related signals across cohorts and iterate on the visualization "
        "until it looks right. Which Galaxy tool should I use for interactive Python plotting?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q019": (
        "I want compact summary figures for a set of target genes (e.g., comparing groups and highlighting top signals) "
        "as part of a classifier interpretation workflow. Which Galaxy tool should I use to do this interactively?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q020": (
        "I want to apply a trained pathway-activity model to cell line data to get predicted statuses and then compare "
        "those predictions with drug response measurements. Which Galaxy tool should I use for an interactive Python workflow?"
    ),
    "statistics-aberrant_pi3k_pathway_analysis-q021": (
        "I have an external cohort and want to run the same trained classifier to assign pathway-activity status, "
        "then inspect the distribution of predictions. Which Galaxy tool should I use in Galaxy for this kind of notebook analysis?"
    ),

    # Simple data wrangling / plotting steps (avoid tool-name leakage)
    "statistics-classification_machinelearning-q018": (
        "I want to drop the first few lines of a text/tabular file as a quick cleanup step before importing it into downstream tools. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-regression_machinelearning-q016": (
        "I have a text/tabular file where the first lines are metadata or a header block, and I need to remove them before analysis. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-fruit_360-q011": (
        "I have a tabular file with many columns and need to keep only a specific subset of columns to create a cleaner feature table "
        "for downstream machine learning. Which Galaxy tool should I use?"
    ),
    "statistics-clustering_machinelearning-q012": (
        "I have a table of x/y values (and optionally a group column) and want a simple scatter plot for quick exploratory data analysis. "
        "Which Galaxy tool should I use?"
    ),

    # Flexynesis (interactive R / Bioconductor) + surrounding table prep
    "statistics-flexynesis_cbio_import-q011": (
        "I need to pull multi-omics data and clinical labels from a cancer portal and organize them into analysis-ready tables in R. "
        "Which Galaxy tool should I use for an interactive R/Bioconductor session?"
    ),
    "statistics-flexynesis_cbio_import-q012": (
        "I have a dataset inside a collection/history that I need to extract as a standalone dataset so I can reuse it in multiple steps. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_cbio_import-q013": (
        "I need to derive a new column in a tabular file from existing columns (basic expressions/arithmetic) to prepare metadata for modeling. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_cbio_import-q014": (
        "I need to keep only specific columns from a tabular dataset (like selecting an ID column plus a small set of features) before merging tables. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_cbio_import-q015": (
        "I need to sort a tabular dataset by one or more columns while keeping the header intact, so downstream merges behave predictably. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_cbio_import-q016": (
        "I want to run a short R script to reshape/clean a set of omics tables (renaming columns, harmonizing sample IDs) and inspect the results. "
        "Which Galaxy tool should I use for an interactive R session?"
    ),
    "statistics-flexynesis_cbio_import-q017": (
        "I need to do a bit of custom data preparation in R (sanity checks, small transformations, and quick plots) before training a model. "
        "Which Galaxy tool should I use in Galaxy?"
    ),
    "statistics-flexynesis_classification-q011": (
        "I want to train a classifier on multi-omics data in R and then inspect feature importance/embeddings to understand what the model learned. "
        "Which Galaxy tool should I use for an interactive R/Bioconductor workflow?"
    ),
    "statistics-flexynesis_classification-q012": (
        "I need to extract one dataset from a larger history/collection so I can feed it into an R-based modeling step. Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q013": (
        "I have a tabular file with a header and want to sort the rows by a key column without breaking the header line. Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q014": (
        "I have model outputs (predictions/embeddings) and want to generate a few publication-style plots in R and tweak them interactively. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q015": (
        "I need to compute a derived column in a tabular dataset (for example, create a label column from existing metadata fields) before modeling. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q016": (
        "I have two tabular datasets that share a sample identifier column and I need to merge them into a single table for downstream analysis. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q017": (
        "Before analysis, I want to quickly take the first N rows of a table to sanity-check formatting and sample IDs. Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q018": (
        "I have a wide table and need to select a specific set of columns (including a few feature columns plus an ID). Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q019": (
        "I need to join two tabular datasets on a shared key, but I also want control over which columns are kept from each side. Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_classification-q020": (
        "I need to transpose a tabular matrix (swap rows and columns) so that samples are rows and features are columns (or vice versa). "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_survival-q011": (
        "I want to build a model in R that relates omics features to survival outcomes and then produce standard survival plots and summaries. "
        "Which Galaxy tool should I use for an interactive R/Bioconductor session?"
    ),
    "statistics-flexynesis_survival-q012": (
        "I have a dataset embedded in a collection and need to pull it out as a standalone dataset for downstream joining and modeling. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_survival-q013": (
        "I need to summarize a tabular dataset by applying simple operations across columns/rows (e.g., min/max/mean or group-wise summaries). "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_survival-q014": (
        "I have a tabular dataset and want to create a new column by combining or transforming existing columns (e.g., derive a time-to-event label). "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_survival-q015": (
        "I need to clean up values in a specific column (e.g., replace strings, normalize identifiers) before merging with clinical metadata. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_survival-q016": (
        "I want to generate survival-related figures in R (Kaplan–Meier curves and risk tables) and iterate on the plot styling interactively. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_unsupervised-q011": (
        "I want to do unsupervised analysis in R on multi-omics data (learn latent representations and visualize clusters/UMAP). "
        "Which Galaxy tool should I use for an interactive R/Bioconductor workflow?"
    ),
    "statistics-flexynesis_unsupervised-q012": (
        "I need to extract a dataset from a collection/history so I can reuse it across multiple analysis branches. Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_unsupervised-q013": (
        "I need to do a few small but custom data transformations in R (reshaping tables, checking sample alignment) before running unsupervised modeling. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-flexynesis_unsupervised-q014": (
        "I have an embedding/latent-space output and want to make exploratory plots (UMAP/cluster plots) in R and adjust parameters interactively. "
        "Which Galaxy tool should I use?"
    ),

    # GPU Jupyter lab tutorial: avoid core tool leakage (Filter/Cut)
    "statistics-gpu_jupyter_lab-q011": (
        "I have a tabular dataset with a numeric score column and only want to keep records above a cutoff (e.g., score >= 0.8). "
        "Which Galaxy tool should I use to filter the rows?"
    ),
    "statistics-gpu_jupyter_lab-q012": (
        "I have a sample metadata table and want to drop all rows where a column contains a specific keyword (e.g., remove samples labeled as \"control\"). "
        "Which Galaxy tool should I use?"
    ),
    "statistics-gpu_jupyter_lab-q013": (
        "I have a clinical table and want to keep only the rows that satisfy multiple criteria at once "
        "(for example: tumor_stage is III/IV AND age_at_diagnosis > 50). Which Galaxy tool should I use?"
    ),
    "statistics-gpu_jupyter_lab-q014": (
        "Before running a heavy downstream step, I want to exclude rows with missing values in a key column "
        "(e.g., drop rows where the label column is empty/NA). Which Galaxy tool should I use?"
    ),
    "statistics-gpu_jupyter_lab-q015": (
        "I have a wide feature table and need to keep only an ID column plus a small set of feature columns to create a compact training matrix. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-gpu_jupyter_lab-q016": (
        "I need to drop some columns from a tabular file and reorder the remaining columns to match the column order of another dataset. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-gpu_jupyter_lab-q017": (
        "I have a tabular file where I only need a contiguous block of columns (e.g., columns 5–200) and I want to discard everything else. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-gpu_jupyter_lab-q018": (
        "I have a table with metadata columns up front and many feature columns after that. "
        "I want to split out only the metadata columns (e.g., the first 4 columns) into a separate table. Which Galaxy tool should I use?"
    ),

    # iwtomics: interval/omics signal windows (toolshed tools, but label leakage in query)
    "statistics-iwtomics-q011": (
        "I have multiple omics signals along genomic coordinates and want to load them, apply smoothing, and generate exploratory plots of signal profiles. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-iwtomics-q012": (
        "I want to test for differences in genomic signal profiles between groups and then visualize the test results in a plot. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-iwtomics-q013": (
        "I have statistical test results and want to plot the signal profiles while highlighting regions that pass a chosen significance threshold. "
        "Which Galaxy tool should I use?"
    ),

    # SimText / PubMed workflow (interactive Python)
    "statistics-text-mining_simtext-q011": (
        "I want to programmatically query PubMed from Galaxy, retrieve a set of matching papers, and keep the results for downstream text mining. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-text-mining_simtext-q012": (
        "I have a list of PubMed IDs and want to fetch biomedical entity annotations for them (for example, using PubTator-style output) for text mining. "
        "Which Galaxy tool should I use?"
    ),
    "statistics-text-mining_simtext-q013": (
        "I want to explore document similarity for a set of papers and interactively inspect the results (clusters/nearest neighbors) in a Python app or notebook. "
        "Which Galaxy tool should I use?"
    ),
}


def main() -> None:
    args = parse_args()
    items = []
    with args.v1.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))

    changed: List[Tuple[str, str, str]] = []
    for it in items:
        meta = it.get("metadata") or {}
        if meta.get("topic") != "statistics":
            continue
        qid = it.get("id")
        if not isinstance(qid, str) or qid not in REWRITES:
            continue
        old = str(it.get("query") or "").strip()
        new = REWRITES[qid].strip()
        if new and new != old:
            it["query"] = new
            changed.append((qid, old, new))

    if args.dry_run:
        print(f"Planned changes: {len(changed)}")
        for qid, old, new in changed:
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
