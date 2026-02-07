#!/usr/bin/env python3
"""
Expand ground truth for statistics topic queries.
- Add tabular_learner to ML classification/regression queries
- Add ludwig_experiment to deep learning training queries
"""

import json
from pathlib import Path

BENCHMARK_FILE = Path("data/benchmark/v1_items.jsonl")

# Tool IDs
TABULAR_LEARNER = "toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4"
LUDWIG_EXPERIMENT = "toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3"

# Queries to expand with tabular_learner
EXPAND_TABULAR_LEARNER = [
    "statistics-age-prediction-with-ml-q014",      # sklearn_ensemble (tree-based ensemble)
    "statistics-classification_machinelearning-q011",  # sklearn_generalized_linear (linear/logistic)
    "statistics-classification_machinelearning-q015",  # sklearn_ensemble (ensemble model)
    "statistics-classification_regression-q013",   # sklearn_ensemble (ensemble approach)
    "statistics-regression_machinelearning-q011",  # sklearn_generalized_linear (GLM)
    "statistics-regression_machinelearning-q013",  # sklearn_ensemble (tree-based ensemble)
]

# Queries to expand with ludwig_experiment
EXPAND_LUDWIG = [
    "statistics-CNN-q014",              # keras_train_and_eval (train neural network)
    "statistics-FNN-q013",              # keras_train_and_eval (end-to-end training)
    "statistics-RNN-q013",              # keras_train_and_eval (fits model, reports performance)
    "statistics-fruit_360-q015",        # keras_train_and_eval (end-to-end training)
    "statistics-intro_deep_learning-q013",  # keras_train_and_eval (fits model)
    "statistics-intro_deep_learning-q016",  # keras_train_and_eval (end-to-end training)
]

def main():
    # Read all items
    items = []
    with open(BENCHMARK_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    
    # Track changes
    changes = []
    
    # Expand ground truth
    for item in items:
        item_id = item["id"]
        modified = False
        
        # Expand with tabular_learner
        if item_id in EXPAND_TABULAR_LEARNER:
            if TABULAR_LEARNER not in item["tools"]:
                item["tools"].append(TABULAR_LEARNER)
                item["metadata"]["ground_truth_alternatives"] = True
                item["metadata"]["ground_truth_alternatives_note"] = (
                    "Manual: tabular_learner is a versatile AutoML tool that supports "
                    "various ML algorithms including linear models, tree-based ensembles, "
                    "and can produce interpretable results with feature importance."
                )
                modified = True
                changes.append(f"  - {item_id}: added tabular_learner")
        
        # Expand with ludwig_experiment
        if item_id in EXPAND_LUDWIG:
            if LUDWIG_EXPERIMENT not in item["tools"]:
                item["tools"].append(LUDWIG_EXPERIMENT)
                item["metadata"]["ground_truth_alternatives"] = True
                item["metadata"]["ground_truth_alternatives_note"] = (
                    "Manual: ludwig_experiment is a declarative deep learning tool that "
                    "can train and evaluate neural networks end-to-end from a YAML/JSON config, "
                    "supporting the same train-and-evaluate workflow."
                )
                modified = True
                changes.append(f"  - {item_id}: added ludwig_experiment")
    
    # Write back
    with open(BENCHMARK_FILE, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    print("Expanded ground truth for statistics topic:")
    print("\n".join(changes))
    print(f"\nTotal: {len(changes)} items updated")

if __name__ == "__main__":
    main()
