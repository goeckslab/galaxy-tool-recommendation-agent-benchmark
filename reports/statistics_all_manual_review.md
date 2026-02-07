# Statistics topic manual review (all tutorials)

- Items: `111`
- Tutorials: `22`
- GTN root: `training-material` (exists=True)

## Tutorials in scope

- `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`: `11` items
- `topics/statistics/tutorials/flexynesis_classification`: `11` items
- `topics/statistics/tutorials/classification_machinelearning`: `8` items
- `topics/statistics/tutorials/gpu_jupyter_lab`: `8` items
- `topics/statistics/tutorials/flexynesis_cbio_import`: `7` items
- `topics/statistics/tutorials/fruit_360`: `7` items
- `topics/statistics/tutorials/CNN`: `6` items
- `topics/statistics/tutorials/flexynesis_survival`: `6` items
- `topics/statistics/tutorials/intro_deep_learning`: `6` items
- `topics/statistics/tutorials/regression_machinelearning`: `6` items
- `topics/statistics/tutorials/FNN`: `5` items
- `topics/statistics/tutorials/RNN`: `5` items
- `topics/statistics/tutorials/age-prediction-with-ml`: `5` items
- `topics/statistics/tutorials/classification_regression`: `4` items
- `topics/statistics/tutorials/flexynesis_unsupervised`: `4` items
- `topics/statistics/tutorials/iwtomics`: `3` items
- `topics/statistics/tutorials/text-mining_simtext`: `3` items
- `topics/statistics/tutorials/clustering_machinelearning`: `2` items
- `topics/statistics/tutorials/galaxy-ludwig`: `1` items
- `topics/statistics/tutorials/hyperdimensional_computing`: `1` items
- `topics/statistics/tutorials/loris_model`: `1` items
- `topics/statistics/tutorials/machinelearning`: `1` items

## Rewrite signals (should be 0 for a clean benchmark)

- `mentions_specific_dataset`: `0`
- `mentions_tutorial`: `0`
- `templated_recommend`: `0`
- `tool_leak_backticks`: `0`

- internal-like core tool IDs (first tool): `9`
- items with manual ground-truth alternatives: `13`

## Per-item review

### `statistics-CNN-q011`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. My labels are a single column of class IDs, but the model expects one-hot targets. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:281`: > - {% tool [To categorical](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.10.0) %}

### `statistics-CNN-q012`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:293`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0) %}

### `statistics-CNN-q013`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I already have a saved architecture/config and want to instantiate the actual model object. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:338`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.10.0) %}

### `statistics-CNN-q014`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:363`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0) %}

### `statistics-CNN-q015`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:382`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0) %}

### `statistics-CNN-q016`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want a quick visualization summary of my ML experiment outputs for inspection. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:398`: > - {% tool [Machine Learning Visualization Extension](toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0) %}

### `statistics-FNN-q011`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I have a tabular classification task with many numeric features. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:351`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0) %}

### `statistics-FNN-q012`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I'm analyzing a tabular classification task with many numeric features. I want to create a trainable neural network from an architecture definition (without writing code). Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:378`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.10.0) %}

### `statistics-FNN-q013`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I have a tabular classification task with many numeric features. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I need to control epochs and batch size. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:403`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.10.0) %}

### `statistics-FNN-q014`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I have a tabular classification task with many numeric features. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:424`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.10.0) %}

### `statistics-FNN-q015`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I'm working with a tabular classification task with many numeric features. I want interactive plots to evaluate a regression model (predicted vs true, residuals). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:442`: > - {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}

### `statistics-RNN-q011`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I’m prototyping a model and need a step that prepares a written architecture specification for building. What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:264`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0) %}

### `statistics-RNN-q012`

- tutorial: `topics/statistics/tutorials/RNN`
- query: In my project I’m using a sequence/time-series dataset where order matters (e.g., for classification). I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:293`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.10.0) %}

### `statistics-RNN-q013`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I have training + validation splits and need the step that fits the model and reports performance. Also, I want early stopping if validation performance stops improving. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:318`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.10.0) %}

### `statistics-RNN-q014`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I want to run inference using a previously trained model and export the predicted classes. Also, I want a simple table mapping each sample to its prediction. What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:338`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.10.0) %}

### `statistics-RNN-q015`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I need a compact set of plots to sanity-check training/evaluation results. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:355`: > - {% tool [Machine Learning Visualization Extension](toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.10.0) %}

### `statistics-aberrant_pi3k_pathway_analysis-q011`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I have gene expression data together with mutation and copy-number status across many cancer types. I want to train a classifier that predicts aberrant PI3K-pathway activity and evaluate it with AUROC/AUPR. Which Galaxy tool should I use if I want to do this interactively in Python?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q012`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I trained a pan-cancer model and now want to assess how well it works within a single cancer type (and compare performance across cohorts). Which Galaxy tool should I use for an interactive Python workflow?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q013`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I built several related models (different gene sets and cohort selections) and want to compare their performance curves and key features side-by-side. Which Galaxy tool should I use to explore this in Python?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q014`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I have a trained model and need to score a new cohort to produce per-sample pathway-activity predictions (including decision scores). What Galaxy tool should I use if I want to run this in a notebook?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q015`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: After training a classifier, I want to understand why it makes certain calls (feature weights/ranks) and generate a few diagnostic plots. Which Galaxy tool should I use for interactive Python analysis?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q016`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I have a table of mutations per sample and need to standardize/annotate mutations into classes that can be used as labels or covariates in downstream modeling. Which Galaxy tool should I use if I want to do this in Python?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q017`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I want to explore which alternative genes in a pathway might explain a phenotype, and I need to inspect pathway-level summaries and candidate gene lists interactively. Which Galaxy tool should I use in Galaxy?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q018`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I want to make heatmaps summarizing pathway-related signals across cohorts and iterate on the visualization until it looks right. Which Galaxy tool should I use for interactive Python plotting?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q019`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I want compact summary figures for a set of target genes (e.g., comparing groups and highlighting top signals) as part of a classifier interpretation workflow. Which Galaxy tool should I use to do this interactively?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q020`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I want to apply a trained pathway-activity model to cell line data to get predicted statuses and then compare those predictions with drug response measurements. Which Galaxy tool should I use for an interactive Python workflow?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-aberrant_pi3k_pathway_analysis-q021`

- tutorial: `topics/statistics/tutorials/aberrant_pi3k_pathway_analysis`
- query: I have an external cohort and want to run the same trained classifier to assign pathway-activity status, then inspect the distribution of predictions. Which Galaxy tool should I use in Galaxy for this kind of notebook analysis?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-age-prediction-with-ml-q011`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to bundle preprocessing (scaling/encoding) and the estimator into one pipeline for consistent CV. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-age-prediction-with-ml-q012`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to do cross-validated hyperparameter tuning (grid/random search) and pick the best settings. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-age-prediction-with-ml-q013`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I ran hyperparameter tuning and want a parallel coordinates plot to see which settings correlate with performance. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.2']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-age-prediction-with-ml-q014`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-age-prediction-with-ml-q015`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I have a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I need regression performance visualizations to check how good my predictions are. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-classification_machinelearning-q011`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want a simple, interpretable regression/classification model (linear/logistic) with evaluation. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:156`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:192`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:

### `statistics-classification_machinelearning-q012`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want an interactive plot summarizing classification performance (ROC/PR/confusion-matrix style). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:217`: >  {% tool [Plot confusion matrix, precision, recall and ROC and AUC curves](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:331`: >  {% tool [Plot confusion matrix, precision, recall and ROC and AUC curves](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:402`: >  {% tool [Plot confusion matrix, precision, recall and ROC and AUC curves](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4) %}:

### `statistics-classification_machinelearning-q013`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to run k-nearest neighbors classification and evaluate it (e.g., with CV). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:288`: > {% tool [Nearest Neighbors Classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:318`: > {% tool [Nearest Neighbors Classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0) %}:

### `statistics-classification_machinelearning-q014`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to train an SVM classifier and evaluate accuracy with a proper train/test split. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0', 'toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). If you restrict the compared models to SVM only, it can serve as an alternative way to train an SVM classifier on tabular data with reproducible splits via the random seed and (optionally) a sample ID column.
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:357`: >  {% tool [Support vector machines (SVMs)](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:389`: >  {% tool [Support vector machines (SVMs)](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %}:

### `statistics-classification_machinelearning-q015`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I’d like to fit an ensemble model for prediction and compare its performance to other methods. Also, I want to inspect predicted vs true values to spot obvious issues. What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:421`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:453`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:541`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:

### `statistics-classification_machinelearning-q016`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I have preprocessing steps and a model; I want to chain them into a single reusable pipeline. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:484`: > {% tool [Pipeline builder](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0) %}:

### `statistics-classification_machinelearning-q017`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I need to compare hyperparameter combinations with CV and select the best-performing model. Also, I care about picking a scoring metric that matches my goal. What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:500`: > {% tool [Hyperparameter search](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0) %}:

### `statistics-classification_machinelearning-q018`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I want to drop the first few lines of a text/tabular file as a quick cleanup step before importing it into downstream tools. Which Galaxy tool should I use?
- tools: ['Remove beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: this step removes the first line (header) from a tabular file. A sed-based text transformation can delete the first line (e.g., '1d'), so it is a valid alternative to the dedicated 'Remove beginning' tool.
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:207`: > 1. **Remove beginning** {% icon tool %} with the following parameters:

### `statistics-classification_regression-q011`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I need a support vector machine classifier for my feature matrix and evaluation outputs. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0', 'toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). Restricting the compared models to SVM only provides an SVM-classifier training path comparable in intent to the dedicated SVM classifier tool for tabular inputs.
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-classification_regression-q012`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want performance plots to compare models across metrics. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-classification_regression-q013`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need an ensemble approach for classification/regression and want metrics on held-out data. Also, I want the result to be easy to plug into the next step. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-classification_regression-q014`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want plots that summarize regression accuracy and error patterns. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-clustering_machinelearning-q011`

- tutorial: `topics/statistics/tutorials/clustering_machinelearning`
- query: I'm working with a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to cluster samples based on numeric features and get cluster assignments. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-clustering_machinelearning-q012`

- tutorial: `topics/statistics/tutorials/clustering_machinelearning`
- query: I have a table of x/y values (and optionally a group column) and want a simple scatter plot for quick exploratory data analysis. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/ggplot2_point/ggplot2_point/3.4.0+galaxy1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_cbio_import-q011`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I need to pull multi-omics data and clinical labels from a cancer portal and organize them into analysis-ready tables in R. Which Galaxy tool should I use for an interactive R/Bioconductor session?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_cbio_import-q012`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I have a dataset inside a collection/history that I need to extract as a standalone dataset so I can reuse it in multiple steps. Which Galaxy tool should I use?
- tools: ['__EXTRACT_DATASET__']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:78`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:122`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:162`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:

### `statistics-flexynesis_cbio_import-q013`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I need to derive a new column in a tabular file from existing columns (basic expressions/arithmetic) to prepare metadata for modeling. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:84`: > 2. {% tool [Table Compute](toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:167`: > 2. {% tool [Table Compute](toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2) %} with the following parameters:

### `statistics-flexynesis_cbio_import-q014`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I need to keep only specific columns from a tabular dataset (like selecting an ID column plus a small set of features) before merging tables. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:91`: > 3. {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:135`: > 3. {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:174`: > 3. {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_cbio_import-q015`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I need to sort a tabular dataset by one or more columns while keeping the header intact, so downstream merges behave predictably. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_cbio_import/tutorial.md:127`: > 2. {% tool [Sort](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_cbio_import-q016`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I want to run a short R script to reshape/clean a set of omics tables (renaming columns, harmonizing sample IDs) and inspect the results. Which Galaxy tool should I use for an interactive R session?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_cbio_import-q017`

- tutorial: `topics/statistics/tutorials/flexynesis_cbio_import`
- query: I need to do a bit of custom data preparation in R (sanity checks, small transformations, and quick plots) before training a model. Which Galaxy tool should I use in Galaxy?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_classification-q011`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I want to train a classifier on multi-omics data in R and then inspect feature importance/embeddings to understand what the model learned. Which Galaxy tool should I use for an interactive R/Bioconductor workflow?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_classification-q012`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I need to extract one dataset from a larger history/collection so I can feed it into an R-based modeling step. Which Galaxy tool should I use?
- tools: ['__EXTRACT_DATASET__']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `4` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:204`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:209`: > 2. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:329`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:

### `statistics-flexynesis_classification-q013`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I have a tabular file with a header and want to sort the rows by a key column without breaking the header line. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `8` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:232`: > 1. {% tool [Sort](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:343`: > 1. {% tool [Sort](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:443`: > 3. {% tool [Sort](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_classification-q014`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I have model outputs (predictions/embeddings) and want to generate a few publication-style plots in R and tweak them interactively. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_classification-q015`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I need to compute a derived column in a tabular dataset (for example, create a label column from existing metadata fields) before modeling. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:428`: > 1. {% tool [Table Compute](toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:592`: > 1. {% tool [Table Compute](toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2) %} with the following parameters:

### `statistics-flexynesis_classification-q016`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I have two tabular datasets that share a sample identifier column and I need to merge them into a single table for downstream analysis. Which Galaxy tool should I use?
- tools: ['join1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: both tools perform a key-based join of two tabular datasets into a single table. The text_processing EasyJoin variant is an acceptable alternative when you need more control over which columns are kept from each input.
- tutorial.md hits: `10` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:435`: > 2. {% tool [Join two Datasets](join1) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:444`: >    - {% icon param-file %} *"Sort Query"*: `table` (output of **Join two Datasets** {% icon tool %})
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:489`: > 9. {% tool [Join](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_classification-q017`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: Before analysis, I want to quickly take the first N rows of a table to sanity-check formatting and sample IDs. Which Galaxy tool should I use?
- tools: ['Show beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: both tools output the first N lines of a dataset for quick inspection (head/select-first). Either is appropriate for sanity-checking a table before analysis.
- tutorial.md hits: `6` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:452`: > 4. {% tool [Select first](Show beginning1) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:453`: >    - *"Select first"*: `500`
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:458`: >    - {% icon param-file %} *"File to cut"*: `table` (output of **Select first** {% icon tool %})

### `statistics-flexynesis_classification-q018`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I have a wide table and need to select a specific set of columns (including a few feature columns plus an ID). Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `12` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:457`: > 5. {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:482`: > 8. {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:523`: > 16. {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_classification-q019`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I need to join two tabular datasets on a shared key, but I also want control over which columns are kept from each side. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `6` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:489`: > 9. {% tool [Join](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:541`: > 20. {% tool [Join](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy2) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:550`: > 22. {% tool [Join](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_classification-q020`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I need to transpose a tabular matrix (swap rows and columns) so that samples are rows and features are columns (or vice versa). Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.9+galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `4` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:506`: > 12. {% tool [Transpose](toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.9+galaxy0) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:511`: > 14. {% tool [Transpose](toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.9+galaxy0) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_classification/tutorial.md:670`: > 12. {% tool [Transpose](toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.9+galaxy0) %} with the following parameters:

### `statistics-flexynesis_classification-q021`

- tutorial: `topics/statistics/tutorials/flexynesis_classification`
- query: I'm working with a multi-omics dataset to predict breast cancer subtypes and interpret learned features. I want to try multiple models automatically on tabular data and see which performs best. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_survival-q011`

- tutorial: `topics/statistics/tutorials/flexynesis_survival`
- query: I want to build a model in R that relates omics features to survival outcomes and then produce standard survival plots and summaries. Which Galaxy tool should I use for an interactive R/Bioconductor session?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_survival-q012`

- tutorial: `topics/statistics/tutorials/flexynesis_survival`
- query: I have a dataset embedded in a collection and need to pull it out as a standalone dataset for downstream joining and modeling. Which Galaxy tool should I use?
- tools: ['__EXTRACT_DATASET__']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.md:180`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.md:248`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:

### `statistics-flexynesis_survival-q013`

- tutorial: `topics/statistics/tutorials/flexynesis_survival`
- query: I need to summarize a tabular dataset by applying simple operations across columns/rows (e.g., min/max/mean or group-wise summaries). Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.md:185`: > 2. {% tool [Datamash](toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0) %} with the following parameters:

### `statistics-flexynesis_survival-q014`

- tutorial: `topics/statistics/tutorials/flexynesis_survival`
- query: I have a tabular dataset and want to create a new column by combining or transforming existing columns (e.g., derive a time-to-event label). Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.md:213`: > 1. {% tool [Compute](toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1) %} with the following parameters:

### `statistics-flexynesis_survival-q015`

- tutorial: `topics/statistics/tutorials/flexynesis_survival`
- query: I need to clean up values in a specific column (e.g., replace strings, normalize identifiers) before merging with clinical metadata. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_replace_in_column/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_survival/tutorial.md:230`: > 1. {% tool [Replace Text](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_replace_in_column/9.5+galaxy2) %} with the following parameters:

### `statistics-flexynesis_survival-q016`

- tutorial: `topics/statistics/tutorials/flexynesis_survival`
- query: I want to generate survival-related figures in R (Kaplan–Meier curves and risk tables) and iterate on the plot styling interactively. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_unsupervised-q011`

- tutorial: `topics/statistics/tutorials/flexynesis_unsupervised`
- query: I want to do unsupervised analysis in R on multi-omics data (learn latent representations and visualize clusters/UMAP). Which Galaxy tool should I use for an interactive R/Bioconductor workflow?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_unsupervised-q012`

- tutorial: `topics/statistics/tutorials/flexynesis_unsupervised`
- query: I need to extract a dataset from a collection/history so I can reuse it across multiple analysis branches. Which Galaxy tool should I use?
- tools: ['__EXTRACT_DATASET__']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/flexynesis_unsupervised/tutorial.md:146`: > 1. {% tool [Extract dataset](__EXTRACT_DATASET__) %} with the following parameters:

### `statistics-flexynesis_unsupervised-q013`

- tutorial: `topics/statistics/tutorials/flexynesis_unsupervised`
- query: I need to do a few small but custom data transformations in R (reshaping tables, checking sample alignment) before running unsupervised modeling. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-flexynesis_unsupervised-q014`

- tutorial: `topics/statistics/tutorials/flexynesis_unsupervised`
- query: I have an embedding/latent-space output and want to make exploratory plots (UMAP/cluster plots) in R and adjust parameters interactively. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-fruit_360-q011`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a tabular file with many columns and need to keep only a specific subset of columns to create a cleaner feature table for downstream machine learning. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3', 'Cut1']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: the tutorial uses Advanced Cut to keep a specific column from a tabular dataset. Galaxy's core Cut tool can also select a specific column (e.g., column 3), so it is an acceptable alternative.
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:260`: > <hands-on-title>Advanced Cut</hands-on-title>
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:262`: > - {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/1.1.0) %}
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:266`: >    - *"Cut by"*: Select `fields`

### `statistics-fruit_360-q012`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I need to convert the class label column into a categorical/one-hot matrix before training. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:276`: > - {% tool [To categorical](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.8.3) %}

### `statistics-fruit_360-q013`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:288`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.5.0) %}

### `statistics-fruit_360-q014`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to create a trainable neural network from an architecture definition (without writing code). Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:351`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/0.5.0) %}

### `statistics-fruit_360-q015`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:376`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.8.2) %}

### `statistics-fruit_360-q016`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:396`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.8.2) %}

### `statistics-fruit_360-q017`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to visualize model performance and outputs to spot obvious issues. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:414`: > - {% tool [Machine Learning Visualization Extension](toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.2) %}

### `statistics-galaxy-ludwig-q011`

- tutorial: `topics/statistics/tutorials/galaxy-ludwig`
- query: I'm working with a machine learning dataset where you want to train and evaluate a predictive model. I want to train a deep learning model from a declarative config (features/targets specified in YAML/JSON). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-gpu_jupyter_lab-q011`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I have a tabular dataset with a numeric score column and only want to keep records above a cutoff (e.g., score >= 0.8). Which Galaxy tool should I use to filter the rows?
- tools: ['Filter1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:268`: ### Filter training dataset
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:271`: > <hands-on-title>Filter</hands-on-title>

### `statistics-gpu_jupyter_lab-q012`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I have a sample metadata table and want to drop all rows where a column contains a specific keyword (e.g., remove samples labeled as "control"). Which Galaxy tool should I use?
- tools: ['Filter1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_grep_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: for dropping rows based on a keyword/category in a column, a grep-style filter (keeping or excluding matching lines) is also valid in addition to the generic column filter tool.
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:268`: ### Filter training dataset
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:271`: > <hands-on-title>Filter</hands-on-title>

### `statistics-gpu_jupyter_lab-q013`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I have a clinical table and want to keep only the rows that satisfy multiple criteria at once (for example: tumor_stage is III/IV AND age_at_diagnosis > 50). Which Galaxy tool should I use?
- tools: ['Filter1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:268`: ### Filter training dataset
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:271`: > <hands-on-title>Filter</hands-on-title>

### `statistics-gpu_jupyter_lab-q014`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: Before running a heavy downstream step, I want to exclude rows with missing values in a key column (e.g., drop rows where the label column is empty/NA). Which Galaxy tool should I use?
- tools: ['Filter1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:268`: ### Filter training dataset
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:271`: > <hands-on-title>Filter</hands-on-title>

### `statistics-gpu_jupyter_lab-q015`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I have a wide feature table and need to keep only an ID column plus a small set of feature columns to create a compact training matrix. Which Galaxy tool should I use?
- tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: selecting/reordering columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:309`: ### Cut a column from the output collection
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:312`: > <hands-on-title>Cut</hands-on-title>

### `statistics-gpu_jupyter_lab-q016`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I need to drop some columns from a tabular file and reorder the remaining columns to match the column order of another dataset. Which Galaxy tool should I use?
- tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: selecting/reordering columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:309`: ### Cut a column from the output collection
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:312`: > <hands-on-title>Cut</hands-on-title>

### `statistics-gpu_jupyter_lab-q017`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I have a tabular file where I only need a contiguous block of columns (e.g., columns 5–200) and I want to discard everything else. Which Galaxy tool should I use?
- tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: selecting a contiguous block of columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:309`: ### Cut a column from the output collection
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:312`: > <hands-on-title>Cut</hands-on-title>

### `statistics-gpu_jupyter_lab-q018`

- tutorial: `topics/statistics/tutorials/gpu_jupyter_lab`
- query: I have a table with metadata columns up front and many feature columns after that. I want to split out only the metadata columns (e.g., the first 4 columns) into a separate table. Which Galaxy tool should I use?
- tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: extracting the first few metadata columns is a column-selection task supported by both core Cut and text_processing Cut.
- tutorial.md hits: `5` (showing up to 3)
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:220`: Let's look at how can this workflow be created in a step-wise manner. There are 3 steps - first, the training dataset is filtered using the `Filter` tool. The output of this tool along with 2 other datasets (`test_rows` …
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:309`: ### Cut a column from the output collection
  - `training-material/topics/statistics/tutorials/gpu_jupyter_lab/tutorial.md:312`: > <hands-on-title>Cut</hands-on-title>

### `statistics-hyperdimensional_computing-q011`

- tutorial: `topics/statistics/tutorials/hyperdimensional_computing`
- query: I'm working with a machine learning dataset where you want to train and evaluate a predictive model. I want to train and evaluate a hyperdimensional computing classifier. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.9.post1+galaxy0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/hyperdimensional_computing/tutorial.md:94`: > {% tool [chopin2](toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.7+galaxy1) %} with the following configuration:
  - `training-material/topics/statistics/tutorials/hyperdimensional_computing/tutorial.md:129`: > {% tool [chopin2](toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.7+galaxy1) %} with the following configuration:

### `statistics-intro_deep_learning-q011`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Also, I’d like the run to be reproducible (same results if I rerun it). Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-intro_deep_learning-q012`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I want a quick way to see where the classifier is making mistakes. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-intro_deep_learning-q013`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I have training + validation splits and need the step that fits the model and reports performance. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-intro_deep_learning-q014`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I want to create a trainable neural network from an architecture definition (without writing code). Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-intro_deep_learning-q015`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-intro_deep_learning-q016`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I'm analyzing a machine learning dataset where you want to train and evaluate a predictive model. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I want to keep the outputs easy to inspect and debug. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-iwtomics-q011`

- tutorial: `topics/statistics/tutorials/iwtomics`
- query: I have multiple omics signals along genomic coordinates and want to load them, apply smoothing, and generate exploratory plots of signal profiles. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_loadandplot/iwtomics_loadandplot/1.0.0.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-iwtomics-q012`

- tutorial: `topics/statistics/tutorials/iwtomics`
- query: I want to test for differences in genomic signal profiles between groups and then visualize the test results in a plot. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_testandplot/iwtomics_testandplot/1.0.0.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-iwtomics-q013`

- tutorial: `topics/statistics/tutorials/iwtomics`
- query: I have statistical test results and want to plot the signal profiles while highlighting regions that pass a chosen significance threshold. Which Galaxy tool should I use?
- tools: ['toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_plotwithscale/iwtomics_plotwithscale/1.0.0.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-loris_model-q011`

- tutorial: `topics/statistics/tutorials/loris_model`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I need to benchmark a few tabular predictors quickly and pick the top performer. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/loris_model/tutorial.md:163`: > 1. {% tool [Tabular Learner](toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.3) %} with the following parameters:
  - `training-material/topics/statistics/tutorials/loris_model/tutorial.md:176`: > 1. {% tool [Tabular Learner](toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.3) %} with the following parameters:

### `statistics-machinelearning-q011`

- tutorial: `topics/statistics/tutorials/machinelearning`
- query: I have a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to fit an SVM for classification and inspect performance metrics. Also, I want to inspect predicted vs true values to spot obvious issues. Is there a Galaxy tool that can handle this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0', 'toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). When configured to compare only SVM models, it can train an SVM and report evaluation metrics, making it an acceptable alternative for SVM-focused classification on tabular data.
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/machinelearning/tutorial.md:101`: > {% tool [Support vector machines (SVMs) for classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %} with the following parameters to train:
  - `training-material/topics/statistics/tutorials/machinelearning/tutorial.md:122`: > {% tool [Support vector machines (SVMs) for classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %} with the following parameters:

### `statistics-regression_machinelearning-q011`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I’d like to fit a generalized linear model and examine coefficients plus prediction performance. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:136`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:172`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:

### `statistics-regression_machinelearning-q012`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need regression performance visualizations to check how good my predictions are. Also, I’d like a quick run on a small subset first. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:198`: > {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:306`: > {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:422`: > {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}:

### `statistics-regression_machinelearning-q013`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:262`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:295`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:409`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:

### `statistics-regression_machinelearning-q014`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I’m preparing for cross-validation and need one object that includes preprocessing plus the model. Also, I want to inspect predicted vs true values to spot obvious issues. What’s the right Galaxy tool for this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:322`: > {% tool [Pipeline builder](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0) %}:

### `statistics-regression_machinelearning-q015`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I'm analyzing a machine learning dataset where you want to train and evaluate a predictive model. I want an automated hyperparameter search with CV and a ranked summary of results. Also, I’d like a quick run on a small subset first. Which tool in Galaxy can do this?
- tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:349`: > {% tool [Hyperparameter search](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0) %}:

### `statistics-regression_machinelearning-q016`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I have a text/tabular file where the first lines are metadata or a header block, and I need to remove them before analysis. Which Galaxy tool should I use?
- tools: ['Remove beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3']
- rewrite_needed: `False`
- ground_truth_alternatives: `True`
- alternatives_note: Manual: this step removes the first line (header) from a tabular file. A sed-based text transformation can delete the first line (e.g., '1d'), so it is a valid alternative to the dedicated 'Remove beginning' tool.
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:187`: > 1. **Remove beginning of a file** {% icon tool %} with the following parameters:

### `statistics-text-mining_simtext-q011`

- tutorial: `topics/statistics/tutorials/text-mining_simtext`
- query: I want to programmatically query PubMed from Galaxy, retrieve a set of matching papers, and keep the results for downstream text mining. Which Galaxy tool should I use?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-text-mining_simtext-q012`

- tutorial: `topics/statistics/tutorials/text-mining_simtext`
- query: I have a list of PubMed IDs and want to fetch biomedical entity annotations for them (for example, using PubTator-style output) for text mining. Which Galaxy tool should I use?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

### `statistics-text-mining_simtext-q013`

- tutorial: `topics/statistics/tutorials/text-mining_simtext`
- query: I want to explore document similarity for a set of papers and interactively inspect the results (clusters/nearest neighbors) in a Python app or notebook. Which Galaxy tool should I use?
- tools: ['interactive_tool_jupyter_notebook']
- rewrite_needed: `False`
- ground_truth_alternatives: `False`
- tutorial.md hits: `0` (tool may be referenced by display name or older version)

