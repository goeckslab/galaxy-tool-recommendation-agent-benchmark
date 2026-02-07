from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple


GTN_RAW_BASE = "https://raw.githubusercontent.com/galaxyproject/training-material/main"

# A small allowlist of ML-adjacent tools that may not be listed under the Galaxy
# "Machine Learning" tool panel section in our exported mapping, but that we still
# want to rewrite (avoid template-like questions and enforce within-tool diversity).
EXTRA_REWRITE_TOOL_BASES = {
    "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots",
    "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots",
    "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot",
    "toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex",
}


def normalize_tool_id(tool_id: str) -> str:
    if tool_id.startswith("toolshed.g2.bx.psu.edu/"):
        parts = tool_id.split("/")
        if len(parts) >= 2:
            return "/".join(parts[:-1])
    return tool_id


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rewrite ML-section benchmark queries using GTN tutorial context (title/abstract), "
            "removing tool-name leakage and avoiding template-like repetition."
        )
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
        "--cache-dir",
        type=Path,
        default=Path("runs/tutorial_cache"),
        help="Where to cache downloaded GTN tutorial.md files.",
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


def fetch_tutorial_md(tutorial_id: str, cache_dir: Path) -> Optional[str]:
    rel = f"{tutorial_id}/tutorial.md"
    url = f"{GTN_RAW_BASE}/{rel}"
    out_path = cache_dir / rel
    if out_path.exists():
        return out_path.read_text(encoding="utf-8", errors="replace")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        content = subprocess.check_output(
            ["curl", "-fsSL", url],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return None
    out_path.write_text(content, encoding="utf-8")
    return content


def split_frontmatter(md: str) -> Tuple[Dict[str, object], str]:
    if not md.startswith("---\n"):
        return {}, md
    end = md.find("\n---", 4)
    if end == -1:
        return {}, md
    fm_text = md[4:end]
    rest = md[end + 4 :]

    payload: Dict[str, object] = {}
    current_list_key: Optional[str] = None
    for raw in fm_text.splitlines():
        if not raw.strip():
            continue

        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", raw)
        if m and not raw.startswith(" "):
            key = m.group(1).strip()
            value = m.group(2).strip()
            if value == "":
                payload[key] = []
                current_list_key = key
            else:
                payload[key] = value.strip().strip('"').strip("'")
                current_list_key = None
            continue

        if current_list_key and isinstance(payload.get(current_list_key), list):
            m2 = re.match(r"^\s*-\s+(.*)$", raw)
            if m2:
                payload[current_list_key].append(m2.group(1).strip())
                continue
            if payload[current_list_key]:
                payload[current_list_key][-1] = (
                    str(payload[current_list_key][-1]) + " " + raw.strip()
                ).strip()

    return payload, rest


def strip_liquid_and_md(text: str) -> str:
    text = re.sub(r"\{\%.*?\%\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_abstract(md_rest: str) -> str:
    lines = md_rest.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    para: List[str] = []
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            break
        if line.lstrip().startswith(">"):
            i += 1
            continue
        para.append(line.strip())
        i += 1
    return strip_liquid_and_md(" ".join(para))


def extract_title(frontmatter: Dict[str, object], md: str) -> Optional[str]:
    title = frontmatter.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or None
    return None


def infer_domain(md: str, tutorial_id: str, title: str, abstract: str) -> str:
    text = f"{title}\n{abstract}\n{md}".lower()
    tid = tutorial_id.lower()
    if "fruit" in tid or "fruit" in text:
        return "image classification"
    if "cnn" in tid or "convolution" in text:
        return "convolutional neural network image classification"
    if "rnn" in tid or "recurrent" in text:
        return "sequence or time-series classification"
    if "fnn" in tid or "feedforward" in text or "feed forward" in text:
        return "tabular classification with a feed-forward neural network"
    if "age-prediction" in tid or "age prediction" in text:
        return "tabular regression (predicting a continuous target)"
    if "regression" in tid or "regression" in text:
        return "tabular regression"
    if "classification" in tid or "classification" in text:
        return "tabular classification"
    if "clustering" in tid or "cluster" in text:
        return "unsupervised clustering"
    if "ludwig" in tid or "ludwig" in text:
        return "tabular deep learning with declarative configuration"
    if "hyperdimensional" in tid or "hyperdimensional" in text:
        return "hyperdimensional computing classification"
    if "deep learning" in text:
        return "deep learning"
    return "machine learning"


def infer_scenario(title: str, abstract: str, tutorial_id: str) -> str:
    blob = f"{title}\n{abstract}".lower()
    tid = tutorial_id.lower()

    # Prefer tutorial_id-specific rules over fuzzy keyword matches.
    if tid.endswith("/cnn"):
        return "a labeled image dataset (handwritten digits) for multi-class classification"
    if tid.endswith("/fruit_360"):
        return "a labeled image dataset of fruits/vegetables for multi-class classification"
    if tid.endswith("/rnn"):
        return "a sequence/time-series dataset where order matters (e.g., for classification)"
    if tid.endswith("/fnn"):
        return "a tabular classification task with many numeric features"
    if tid.endswith("/classification_machinelearning"):
        return "a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style)"
    if tid.endswith("/age-prediction-with-ml"):
        return (
            "a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) "
            "to predict chronological age (regression)"
        )
    if tid.endswith("/flexynesis_classification"):
        return "a multi-omics dataset to predict breast cancer subtypes and interpret learned features"
    if tid.endswith("/clustering_machinelearning"):
        return "a numeric feature matrix where you want to discover groups (unsupervised clustering)"

    if "mnist" in blob:
        return "a labeled image dataset (handwritten digits) for multi-class classification"
    if "fruit" in tid or "fruit 360" in blob or "fruit" in blob:
        return "a labeled image dataset of fruits/vegetables for multi-class classification"
    if "qsar" in blob or "chemical" in blob or "molecular" in blob:
        return "a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style)"
    if (
        re.search(r"\bage\b", blob)
        or "age-prediction" in tid
        or "methylation" in blob
        or "rna-seq" in blob
    ):
        return (
            "a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) "
            "to predict chronological age (regression)"
        )
    if "brca" in blob or "breast cancer" in blob or "metabric" in blob:
        return "a multi-omics dataset to predict breast cancer subtypes and interpret learned features"
    if "clustering" in tid or "cluster" in blob:
        return "a numeric feature matrix where you want to discover groups (unsupervised clustering)"
    if "rnn" in tid:
        return "a sequence/time-series dataset where order matters (e.g., for classification)"
    if "cnn" in tid:
        return "an image classification task where spatial patterns matter"
    if "fnn" in tid:
        return "a tabular classification task with many numeric features"
    return "a machine learning dataset where you want to train and evaluate a predictive model"


@dataclasses.dataclass(frozen=True)
class TutorialContext:
    tutorial_id: str
    title: str
    abstract: str
    questions: Tuple[str, ...]
    objectives: Tuple[str, ...]
    domain: str
    scenario: str


def tutorial_context(tutorial_id: str, md: str) -> TutorialContext:
    fm, rest = split_frontmatter(md or "")
    title = extract_title(fm, md or "") or ""
    abstract = extract_abstract(rest)
    questions_raw = fm.get("questions")
    objectives_raw = fm.get("objectives")
    questions: Tuple[str, ...] = tuple(
        q.strip() for q in (questions_raw or []) if isinstance(q, str) and q.strip()
    )
    objectives: Tuple[str, ...] = tuple(
        o.strip() for o in (objectives_raw or []) if isinstance(o, str) and o.strip()
    )
    domain = infer_domain(md or "", tutorial_id, title=title, abstract=abstract)
    scenario = infer_scenario(title, abstract, tutorial_id)
    return TutorialContext(
        tutorial_id=tutorial_id,
        title=title,
        abstract=abstract,
        questions=questions,
        objectives=objectives,
        domain=domain,
        scenario=scenario,
    )


def stable_choice(key: str, options: List[str]) -> str:
    h = hashlib.sha256(key.encode("utf-8")).digest()
    idx = int.from_bytes(h[:2], "big") % len(options)
    return options[idx]


def question_ending(qid: str) -> str:
    endings = [
        "Which tool in Galaxy can do this?",
        "What Galaxy tool should I run for this step?",
        "Is there a Galaxy tool that can handle this?",
        "What’s the right Galaxy tool for this?",
    ]
    return stable_choice(qid + "\nending", endings)


def opener(qid: str, scenario: str) -> str:
    openers = [
        f"I'm working with {scenario}.",
        f"I have {scenario}.",
        f"In my project I’m using {scenario}.",
        f"I'm analyzing {scenario}.",
    ]
    return stable_choice(qid + "\nopener", openers)

def normalize_words(text: str) -> List[str]:
    # Normalize to a token list for simple similarity checks.
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return [t for t in text.split(" ") if t]


def jaccard_similarity(a: str, b: str) -> float:
    aw = set(normalize_words(a))
    bw = set(normalize_words(b))
    if not aw and not bw:
        return 1.0
    if not aw or not bw:
        return 0.0
    return len(aw & bw) / max(1, len(aw | bw))


def tool_diversifiers(tool_base: str, ctx: TutorialContext) -> List[str]:
    """
    Short, realistic constraints to reduce within-tool query similarity.
    These are intentionally generic and avoid tool names.
    """

    domain = ctx.domain.lower()
    common = [
        "Also, I want to keep the outputs easy to inspect and debug.",
        "Also, I’d like a quick run on a small subset first.",
        "Also, I want the result to be easy to plug into the next step.",
        "Also, I’d like the run to be reproducible (same results if I rerun it).",
    ]

    per_tool: Dict[str, List[str]] = {
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval": [
            "Also, I want to save training curves/metrics for later comparison.",
            "Also, I want early stopping if validation performance stops improving.",
            "Also, I need to control epochs and batch size.",
        ],
        "toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction": [
            "Also, I need predicted class probabilities (not just labels).",
            "Also, I want a simple table mapping each sample to its prediction.",
            "Also, I need the output in a format that’s easy to join back to sample metadata.",
        ],
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv": [
            "Also, I want to use cross-validation and keep a ranked summary of parameter settings.",
            "Also, I care about picking a scoring metric that matches my goal.",
            "Also, I want to compare a small set of parameter grids quickly.",
        ],
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline": [
            "Also, I want to avoid data leakage between preprocessing and evaluation.",
            "Also, I want preprocessing and modeling to be applied consistently in cross-validation.",
        ],
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering": [
            "Also, I want to visualize clusters to see if they make sense.",
            "Also, I want cluster assignments in a simple table I can summarize.",
        ],
    }

    extras = list(per_tool.get(tool_base, [])) + common
    if "regression" in domain:
        extras.append("Also, I want to inspect predicted vs true values to spot obvious issues.")
    if "classification" in domain:
        extras.append("Also, I want a quick way to see where the classifier is making mistakes.")
    if "clustering" in domain or "unsupervised" in domain:
        extras.append("Also, I want a quick check for whether clusters are well separated.")

    # Deduplicate while preserving order.
    seen: set[str] = set()
    out: List[str] = []
    for e in extras:
        e = re.sub(r"\s+", " ", e).strip()
        if not e or e in seen:
            continue
        seen.add(e)
        out.append(e)
    return out


def inject_extra_before_ending(text: str, extra: str) -> str:
    endings = [
        "Which tool in Galaxy can do this?",
        "What Galaxy tool should I run for this step?",
        "Is there a Galaxy tool that can handle this?",
        "What’s the right Galaxy tool for this?",
    ]
    extra = re.sub(r"\s+", " ", extra).strip()
    for e in endings:
        suffix = " " + e
        if text.endswith(suffix):
            return text[: -len(suffix)].rstrip() + " " + extra + " " + e
    return text + " " + extra


def add_unique_nugget(qid: str, ctx: TutorialContext) -> str:
    """
    Add a small, user-like extra constraint to diversify queries for the same tool.
    Avoid mentioning GTN/tutorials, avoid tool names, and keep it generic.
    """

    # Turn tutorial cues into *user constraints* (not tutorial questions/objectives verbatim).
    cues = " ".join(
        [ctx.title, ctx.abstract, " ".join(ctx.questions), " ".join(ctx.objectives)]
    ).lower()
    mapped: List[str] = []

    def add(sentence: str) -> None:
        s = re.sub(r"\s+", " ", sentence).strip()
        if s and s not in mapped:
            mapped.append(s)

    if "interpret" in cues or "explain" in cues:
        add("I want outputs that are easy to interpret and sanity-check.")
    if "cross-validation" in cues or "cross validation" in cues:
        add("I’d like to use cross-validation rather than a single split.")
    if (
        "hyperparameter" in cues
        or "optimis" in cues
        or "optimiz" in cues
        or "tuning" in cues
    ):
        add("I want to compare a few settings and keep a clear record of metrics.")
    if "feature selection" in cues:
        add("I’m worried about high-dimensional features and want something that works well without overfitting.")
    if "regression" in ctx.domain or "r2" in cues:
        add("I care about regression quality (e.g., R²) and want a plot to inspect predicted vs true.")
    if "classification" in ctx.domain or "accuracy" in cues:
        add("I want to evaluate classification performance and quickly spot obvious failure modes.")
    if "clustering" in ctx.domain or "unsupervised" in ctx.domain:
        add("I want to see cluster assignments and a quick visualization to judge separation.")

    # Always include safe generic constraints.
    add("I’d like to keep the output easy to plug into the next step of the workflow.")
    add("I need something that works well on a small test run first.")
    add("I’d like to keep runtime reasonable and avoid unnecessary complexity.")

    pick = stable_choice(qid + "\nnugget", mapped)
    return "Also: " + pick


def build_query(qid: str, tool_base: str, ctx: TutorialContext) -> str:
    scenario = ctx.scenario
    end = question_ending(qid)

    def pick(options: List[str]) -> str:
        return stable_choice(qid + "\n" + tool_base, options)

    def endings() -> List[str]:
        return [
            "Which tool in Galaxy can do this?",
            "What Galaxy tool should I run for this step?",
            "Is there a Galaxy tool that can handle this?",
            "What’s the right Galaxy tool for this?",
        ]

    def openers() -> List[str]:
        return [
            f"I'm working with {scenario}.",
            f"I have {scenario}.",
            f"In my project I’m using {scenario}.",
            f"I'm analyzing {scenario}.",
        ]

    def mix(action_variants: List[str]) -> List[str]:
        # Create more diverse variants by mixing opener + action + ending.
        out: List[str] = []
        for o in openers():
            for a in action_variants:
                for e in endings():
                    out.append(f"{o} {a} {e}")
        return out

    factories: Dict[str, Callable[[], List[str]]] = {
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical": lambda: mix(
            [
                "My labels are a single column of class IDs, but the model expects one-hot targets.",
                "I need to convert the class label column into a categorical/one-hot matrix before training.",
                "The target labels are categories; I want to one-hot encode them for model training.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config": lambda: mix(
            [
                "I want to specify the neural network architecture (layers/activations/input shape) in a config file.",
                "I’m prototyping a model and need a step that prepares a written architecture specification for building.",
                "I want to define a Keras-style model using a configuration so I can reuse it across runs.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder": lambda: mix(
            [
                "I already have a saved architecture/config and want to instantiate the actual model object.",
                "I’ve defined the network structure in a config; now I need the step that builds the runnable model.",
                "I want to create a trainable neural network from an architecture definition (without writing code).",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval": lambda: mix(
            [
                "I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data).",
                "I have training + validation splits and need the step that fits the model and reports performance.",
                "I need to run end-to-end training for a deep learning model and get evaluation metrics back.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction": lambda: mix(
            [
                "I’ve trained a model and now want predictions for a new dataset (labels or probabilities).",
                "After training, I need to apply the saved model to unseen samples to generate outputs.",
                "I want to run inference using a previously trained model and export the predicted classes.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline": lambda: mix(
            [
                "I want to bundle preprocessing (scaling/encoding) and the estimator into one pipeline for consistent CV.",
                "I have preprocessing steps and a model; I want to chain them into a single reusable pipeline.",
                "I’m preparing for cross-validation and need one object that includes preprocessing plus the model.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv": lambda: mix(
            [
                "I want to do cross-validated hyperparameter tuning (grid/random search) and pick the best settings.",
                "I need to compare hyperparameter combinations with CV and select the best-performing model.",
                "I want an automated hyperparameter search with CV and a ranked summary of results.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble": lambda: mix(
            [
                "I want to train a tree-based ensemble (random forest / boosting) and evaluate it.",
                "I’d like to fit an ensemble model for prediction and compare its performance to other methods.",
                "I need an ensemble approach for classification/regression and want metrics on held-out data.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier": lambda: mix(
            [
                "I want to train an SVM classifier and evaluate accuracy with a proper train/test split.",
                "I need a support vector machine classifier for my feature matrix and evaluation outputs.",
                "I want to fit an SVM for classification and inspect performance metrics.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear": lambda: mix(
            [
                "I want a simple, interpretable regression/classification model (linear/logistic) with evaluation.",
                "I’d like to fit a generalized linear model and examine coefficients plus prediction performance.",
                "I need a baseline linear/logistic model for prediction on tabular data.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner": lambda: mix(
            [
                "I want to try multiple models automatically on tabular data and see which performs best.",
                "I’m looking for an AutoML-style tool that trains several tabular models and compares them.",
                "I need to benchmark a few tabular predictors quickly and pick the top performer.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier": lambda: mix(
            [
                "I want to run k-nearest neighbors classification and evaluate it (e.g., with CV).",
                "I need a k-NN classifier tool that outputs predictions and basic performance metrics.",
                "I’d like to fit a nearest-neighbors classifier for my feature table and assess accuracy.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering": lambda: mix(
            [
                "I want to cluster samples based on numeric features and get cluster assignments.",
                "I need to run unsupervised clustering on a feature matrix (e.g., k-means) and inspect results.",
                "I want to group samples into clusters from numeric features and visualize/compare cluster structure.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots": lambda: mix(
            [
                "I want an interactive plot summarizing classification performance (ROC/PR/confusion-matrix style).",
                "I need to visualize classifier performance in an interactive report.",
                "I want performance plots to compare models across metrics.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots": lambda: mix(
            [
                "I want interactive plots to evaluate a regression model (predicted vs true, residuals).",
                "I need regression performance visualizations to check how good my predictions are.",
                "I want plots that summarize regression accuracy and error patterns.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot": lambda: mix(
            [
                "I ran hyperparameter tuning and want a parallel coordinates plot to see which settings correlate with performance.",
                "I need to visualize multi-parameter search results as a parallel coordinates plot.",
                "I want an interactive parallel coordinates plot to explore hyperparameter combinations.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex": lambda: mix(
            [
                "I want a quick visualization summary of my ML experiment outputs for inspection.",
                "I need a compact set of plots to sanity-check training/evaluation results.",
                "I want to visualize model performance and outputs to spot obvious issues.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment": lambda: mix(
            [
                "I want to train a deep learning model from a declarative config (features/targets specified in YAML/JSON).",
                "I have a config-driven experiment definition and want to run training + evaluation without writing code.",
                "I want a tool that consumes a model config and runs an end-to-end training experiment.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2": lambda: mix(
            [
                "I want to train and evaluate a hyperdimensional computing classifier.",
                "I’m experimenting with hyperdimensional computing for classification and need a Galaxy tool for it.",
                "I want to fit a hyperdimensional computing model and compare performance with standard classifiers.",
            ]
        ),
    }

    if tool_base in factories:
        return pick(factories[tool_base]())

    generic = [
        f"{opener(qid, scenario)} I need to run a machine learning step and want to pick the right tool. {end}",
        f"{opener(qid, scenario)} Which Galaxy tool should I use next for this ML workflow? {add_unique_nugget(qid, ctx)}",
        f"{opener(qid, scenario)} I'm not sure which tool matches this task. {end} {add_unique_nugget(qid, ctx)}",
    ]
    return pick(generic)

def variant_pool(tool_base: str, ctx: TutorialContext) -> List[str]:
    scenario = ctx.scenario

    def endings() -> List[str]:
        return [
            "Which tool in Galaxy can do this?",
            "What Galaxy tool should I run for this step?",
            "Is there a Galaxy tool that can handle this?",
            "What’s the right Galaxy tool for this?",
        ]

    def openers() -> List[str]:
        return [
            f"I'm working with {scenario}.",
            f"I have {scenario}.",
            f"In my project I’m using {scenario}.",
            f"I'm analyzing {scenario}.",
        ]

    def mix(action_variants: List[str]) -> List[str]:
        out: List[str] = []
        for o in openers():
            for a in action_variants:
                for e in endings():
                    out.append(f"{o} {a} {e}")
        return out

    factories: Dict[str, List[str]] = {
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical": mix(
            [
                "My labels are a single column of class IDs, but the model expects one-hot targets.",
                "I need to convert the class label column into a categorical/one-hot matrix before training.",
                "The target labels are categories; I want to one-hot encode them for model training.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config": mix(
            [
                "I want to specify the neural network architecture (layers/activations/input shape) in a config file.",
                "I’m prototyping a model and need a step that prepares a written architecture specification for building.",
                "I want to define a Keras-style model using a configuration so I can reuse it across runs.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder": mix(
            [
                "I already have a saved architecture/config and want to instantiate the actual model object.",
                "I’ve defined the network structure in a config; now I need the step that builds the runnable model.",
                "I want to create a trainable neural network from an architecture definition (without writing code).",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval": mix(
            [
                "I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data).",
                "I have training + validation splits and need the step that fits the model and reports performance.",
                "I need to run end-to-end training for a deep learning model and get evaluation metrics back.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction": mix(
            [
                "I’ve trained a model and now want predictions for a new dataset (labels or probabilities).",
                "After training, I need to apply the saved model to unseen samples to generate outputs.",
                "I want to run inference using a previously trained model and export the predicted classes.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline": mix(
            [
                "I want to bundle preprocessing (scaling/encoding) and the estimator into one pipeline for consistent CV.",
                "I have preprocessing steps and a model; I want to chain them into a single reusable pipeline.",
                "I’m preparing for cross-validation and need one object that includes preprocessing plus the model.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv": mix(
            [
                "I want to do cross-validated hyperparameter tuning (grid/random search) and pick the best settings.",
                "I need to compare hyperparameter combinations with CV and select the best-performing model.",
                "I want an automated hyperparameter search with CV and a ranked summary of results.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble": mix(
            [
                "I want to train a tree-based ensemble (random forest / boosting) and evaluate it.",
                "I’d like to fit an ensemble model for prediction and compare its performance to other methods.",
                "I need an ensemble approach for classification/regression and want metrics on held-out data.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier": mix(
            [
                "I want to train an SVM classifier and evaluate accuracy with a proper train/test split.",
                "I need a support vector machine classifier for my feature matrix and evaluation outputs.",
                "I want to fit an SVM for classification and inspect performance metrics.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear": mix(
            [
                "I want a simple, interpretable regression/classification model (linear/logistic) with evaluation.",
                "I’d like to fit a generalized linear model and examine coefficients plus prediction performance.",
                "I need a baseline linear/logistic model for prediction on tabular data.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner": mix(
            [
                "I want to try multiple models automatically on tabular data and see which performs best.",
                "I’m looking for an AutoML-style tool that trains several tabular models and compares them.",
                "I need to benchmark a few tabular predictors quickly and pick the top performer.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier": mix(
            [
                "I want to run k-nearest neighbors classification and evaluate it (e.g., with CV).",
                "I need a k-NN classifier tool that outputs predictions and basic performance metrics.",
                "I’d like to fit a nearest-neighbors classifier for my feature table and assess accuracy.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering": mix(
            [
                "I want to cluster samples based on numeric features and get cluster assignments.",
                "I need to run unsupervised clustering on a feature matrix (e.g., k-means) and inspect results.",
                "I want to group samples into clusters from numeric features and visualize/compare cluster structure.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots": mix(
            [
                "I want an interactive plot summarizing classification performance (ROC/PR/confusion-matrix style).",
                "I need to visualize classifier performance in an interactive report.",
                "I want performance plots to compare models across metrics.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots": mix(
            [
                "I want interactive plots to evaluate a regression model (predicted vs true, residuals).",
                "I need regression performance visualizations to check how good my predictions are.",
                "I want plots that summarize regression accuracy and error patterns.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot": mix(
            [
                "I ran hyperparameter tuning and want a parallel coordinates plot to see which settings correlate with performance.",
                "I need to visualize multi-parameter search results as a parallel coordinates plot.",
                "I want an interactive parallel coordinates plot to explore hyperparameter combinations.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex": mix(
            [
                "I want a quick visualization summary of my ML experiment outputs for inspection.",
                "I need a compact set of plots to sanity-check training/evaluation results.",
                "I want to visualize model performance and outputs to spot obvious issues.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment": mix(
            [
                "I want to train a deep learning model from a declarative config (features/targets specified in YAML/JSON).",
                "I have a config-driven experiment definition and want to run training + evaluation without writing code.",
                "I want a tool that consumes a model config and runs an end-to-end training experiment.",
            ]
        ),
        "toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2": mix(
            [
                "I want to train and evaluate a hyperdimensional computing classifier.",
                "I’m experimenting with hyperdimensional computing for classification and need a Galaxy tool for it.",
                "I want to fit a hyperdimensional computing model and compare performance with standard classifiers.",
            ]
        ),
    }

    if tool_base in factories:
        return factories[tool_base]

    # Generic fallbacks for unknown ML tools.
    return mix(
        [
            "I need to run a machine learning step but I’m not sure which Galaxy tool matches it.",
            "I’m building an ML workflow and want the right tool for this step.",
            "I want something that produces a clean output I can feed into the next step.",
        ]
    )


def pick_diverse_query(
    qid: str,
    tool_base: str,
    ctx: TutorialContext,
    already_used_for_tool: List[str],
    already_used_extras: set[str],
    similarity_threshold: float = 0.78,
) -> str:
    """
    Ensure queries for the same tool base are not too similar.

    We search a pool of variants and choose the one that minimizes similarity
    to already-used queries for that tool.
    """

    candidates = variant_pool(tool_base, ctx)
    diversifiers = tool_diversifiers(tool_base, ctx)

    # Prefer diversifiers not yet used for this tool_base.
    unused_diversifiers = [d for d in diversifiers if d not in already_used_extras]
    if unused_diversifiers:
        diversifiers = unused_diversifiers

    # Expand pool by injecting a short extra sentence before the final question.
    # This helps ensure queries for the same tool aren't near-duplicates.
    expanded: List[str] = []
    for c in candidates:
        expanded.append(c)
        for d in diversifiers[:6]:
            expanded.append(inject_extra_before_ending(c, d))
    candidates = expanded

    # Deduplicate while preserving order.
    seen: set[str] = set()
    uniq: List[str] = []
    for c in candidates:
        c = re.sub(r"\s+", " ", c).strip()
        if not c or c in seen:
            continue
        seen.add(c)
        uniq.append(c)

    if not already_used_for_tool:
        # Make sure the first one isn't bizarrely long.
        chosen = uniq[0]
        for d in diversifiers:
            if d in chosen:
                already_used_extras.add(d)
                break
        return chosen

    best = uniq[0]
    best_score = 1.0
    for c in uniq:
        score = max(jaccard_similarity(c, prev) for prev in already_used_for_tool)
        if score < best_score:
            best, best_score = c, score

    # If everything is still too similar, force uniqueness by adding a nugget.
    if best_score >= similarity_threshold:
        nugget = add_unique_nugget(qid, ctx)
        best = re.sub(r"\s+", " ", (best + " " + nugget)).strip()

    for d in diversifiers:
        if d in best:
            already_used_extras.add(d)
            break

    return best


def main() -> None:
    args = parse_args()
    ml_bases = load_ml_bases(args.tool_sections_file, args.section)

    items: List[dict] = []
    with args.v1.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))

    # Cache tutorials (best-effort) and infer domain per tutorial_id.
    tutorial_info: Dict[str, TutorialContext] = {}
    for item in items:
        tutorial_id = item.get("tutorial_id")
        if not isinstance(tutorial_id, str) or not tutorial_id:
            continue
        if tutorial_id in tutorial_info:
            continue
        md = fetch_tutorial_md(tutorial_id, args.cache_dir) or ""
        tutorial_info[tutorial_id] = tutorial_context(tutorial_id, md)

    changed: List[Tuple[str, str, str]] = []
    used_by_tool: Dict[str, List[str]] = {}
    used_extras_by_tool: Dict[str, set[str]] = {}
    for item in items:
        qid = item.get("id")
        if not isinstance(qid, str) or not qid:
            continue
        tool_ids = [t for t in (item.get("tools") or []) if isinstance(t, str)]
        if not tool_ids:
            continue
        bases = [normalize_tool_id(t) for t in tool_ids]
        tutorial_id = item.get("tutorial_id") if isinstance(item.get("tutorial_id"), str) else ""
        tool_base = normalize_tool_id(tool_ids[0])
        if not (
            any(b in ml_bases for b in bases) or tool_base in EXTRA_REWRITE_TOOL_BASES
        ):
            continue
        ctx = tutorial_info.get(
            tutorial_id,
            TutorialContext(
                tutorial_id=tutorial_id,
                title="",
                abstract="",
                questions=(),
                objectives=(),
                domain="machine learning",
                scenario="a machine learning dataset where you want to train and evaluate a predictive model",
            ),
        )

        old_query = str(item.get("query") or "").strip()
        # Always rewrite ML-section queries to be less templated and remove leakage.
        prev = used_by_tool.setdefault(tool_base, [])
        used_extras = used_extras_by_tool.setdefault(tool_base, set())
        new_query = pick_diverse_query(qid, tool_base, ctx, prev, used_extras)
        prev.append(new_query)
        if new_query != old_query:
            item["query"] = new_query
            changed.append((qid, old_query, new_query))

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
