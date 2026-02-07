# Statistics ML manual review

- Items: `57`
- Tutorials: `13`
- GTN root: `training-material` (exists=True)

## Tutorials in scope

- `topics/statistics/tutorials/classification_machinelearning`: `8` items
- `topics/statistics/tutorials/fruit_360`: `7` items
- `topics/statistics/tutorials/CNN`: `6` items
- `topics/statistics/tutorials/intro_deep_learning`: `6` items
- `topics/statistics/tutorials/regression_machinelearning`: `6` items
- `topics/statistics/tutorials/FNN`: `5` items
- `topics/statistics/tutorials/RNN`: `5` items
- `topics/statistics/tutorials/age-prediction-with-ml`: `5` items
- `topics/statistics/tutorials/classification_regression`: `4` items
- `topics/statistics/tutorials/clustering_machinelearning`: `2` items
- `topics/statistics/tutorials/galaxy-ludwig`: `1` items
- `topics/statistics/tutorials/hyperdimensional_computing`: `1` items
- `topics/statistics/tutorials/machinelearning`: `1` items

## Per-item notes

### `statistics-CNN-q011`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. My labels are a single column of class IDs, but the model expects one-hot targets. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:281`: > - {% tool [To categorical](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.10.0) %}

### `statistics-CNN-q012`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:293`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0) %}

### `statistics-CNN-q013`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I already have a saved architecture/config and want to instantiate the actual model object. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:338`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.10.0) %}

### `statistics-CNN-q014`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:363`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0) %}

### `statistics-CNN-q015`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:382`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0) %}

### `statistics-CNN-q016`

- tutorial: `topics/statistics/tutorials/CNN`
- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want a quick visualization summary of my ML experiment outputs for inspection. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/CNN/tutorial.md:398`: > - {% tool [Machine Learning Visualization Extension](toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0) %}

### `statistics-FNN-q011`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I have a tabular classification task with many numeric features. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:351`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0) %}

### `statistics-FNN-q012`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I'm analyzing a tabular classification task with many numeric features. I want to create a trainable neural network from an architecture definition (without writing code). Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:378`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.10.0) %}

### `statistics-FNN-q013`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I have a tabular classification task with many numeric features. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I need to control epochs and batch size. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:403`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.10.0) %}

### `statistics-FNN-q014`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I have a tabular classification task with many numeric features. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:424`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.10.0) %}

### `statistics-FNN-q015`

- tutorial: `topics/statistics/tutorials/FNN`
- query: I'm working with a tabular classification task with many numeric features. I want interactive plots to evaluate a regression model (predicted vs true, residuals). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/FNN/tutorial.md:442`: > - {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}

### `statistics-RNN-q011`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I’m prototyping a model and need a step that prepares a written architecture specification for building. What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:264`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0) %}

### `statistics-RNN-q012`

- tutorial: `topics/statistics/tutorials/RNN`
- query: In my project I’m using a sequence/time-series dataset where order matters (e.g., for classification). I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:293`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.10.0) %}

### `statistics-RNN-q013`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I have training + validation splits and need the step that fits the model and reports performance. Also, I want early stopping if validation performance stops improving. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:318`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.10.0) %}

### `statistics-RNN-q014`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I want to run inference using a previously trained model and export the predicted classes. Also, I want a simple table mapping each sample to its prediction. What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:338`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.10.0) %}

### `statistics-RNN-q015`

- tutorial: `topics/statistics/tutorials/RNN`
- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I need a compact set of plots to sanity-check training/evaluation results. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/RNN/tutorial.md:355`: > - {% tool [Machine Learning Visualization Extension](toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.10.0) %}

### `statistics-age-prediction-with-ml-q011`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to bundle preprocessing (scaling/encoding) and the estimator into one pipeline for consistent CV. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-age-prediction-with-ml-q012`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to do cross-validated hyperparameter tuning (grid/random search) and pick the best settings. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-age-prediction-with-ml-q013`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I ran hyperparameter tuning and want a parallel coordinates plot to see which settings correlate with performance. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.2']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-age-prediction-with-ml-q014`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-age-prediction-with-ml-q015`

- tutorial: `topics/statistics/tutorials/age-prediction-with-ml`
- query: I have a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I need regression performance visualizations to check how good my predictions are. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-classification_machinelearning-q011`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want a simple, interpretable regression/classification model (linear/logistic) with evaluation. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:156`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:192`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:

### `statistics-classification_machinelearning-q012`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want an interactive plot summarizing classification performance (ROC/PR/confusion-matrix style). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:217`: >  {% tool [Plot confusion matrix, precision, recall and ROC and AUC curves](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:331`: >  {% tool [Plot confusion matrix, precision, recall and ROC and AUC curves](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:402`: >  {% tool [Plot confusion matrix, precision, recall and ROC and AUC curves](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4) %}:

### `statistics-classification_machinelearning-q013`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to run k-nearest neighbors classification and evaluate it (e.g., with CV). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:288`: > {% tool [Nearest Neighbors Classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:318`: > {% tool [Nearest Neighbors Classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0) %}:

### `statistics-classification_machinelearning-q014`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to train an SVM classifier and evaluate accuracy with a proper train/test split. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:357`: >  {% tool [Support vector machines (SVMs)](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:389`: >  {% tool [Support vector machines (SVMs)](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %}:

### `statistics-classification_machinelearning-q015`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I’d like to fit an ensemble model for prediction and compare its performance to other methods. Also, I want to inspect predicted vs true values to spot obvious issues. What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:421`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:453`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:541`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:

### `statistics-classification_machinelearning-q016`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I have preprocessing steps and a model; I want to chain them into a single reusable pipeline. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:484`: > {% tool [Pipeline builder](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0) %}:

### `statistics-classification_machinelearning-q017`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I need to compare hyperparameter combinations with CV and select the best-performing model. Also, I care about picking a scoring metric that matches my goal. What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:500`: > {% tool [Hyperparameter search](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0) %}:

### `statistics-classification_machinelearning-q018`

- tutorial: `topics/statistics/tutorials/classification_machinelearning`
- query: I want to drop the first few lines of a text/tabular file as a quick cleanup step before importing it into downstream tools. Which Galaxy tool should I use?
- gold tools: ['Remove beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3']
- alternatives added: `True`
- note: Manual: this step removes the first line (header) from a tabular file. A sed-based text transformation can delete the first line (e.g., '1d'), so it is a valid alternative to the dedicated 'Remove beginning' tool.
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/classification_machinelearning/tutorial.md:207`: > 1. **Remove beginning** {% icon tool %} with the following parameters:

### `statistics-classification_regression-q011`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I need a support vector machine classifier for my feature matrix and evaluation outputs. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-classification_regression-q012`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want performance plots to compare models across metrics. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-classification_regression-q013`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need an ensemble approach for classification/regression and want metrics on held-out data. Also, I want the result to be easy to plug into the next step. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-classification_regression-q014`

- tutorial: `topics/statistics/tutorials/classification_regression`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want plots that summarize regression accuracy and error patterns. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-clustering_machinelearning-q011`

- tutorial: `topics/statistics/tutorials/clustering_machinelearning`
- query: I'm working with a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to cluster samples based on numeric features and get cluster assignments. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-clustering_machinelearning-q012`

- tutorial: `topics/statistics/tutorials/clustering_machinelearning`
- query: I have a table of x/y values (and optionally a group column) and want a simple scatter plot for quick exploratory data analysis. Which Galaxy tool should I use?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/iuc/ggplot2_point/ggplot2_point/3.4.0+galaxy1']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-fruit_360-q011`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a tabular file with many columns and need to keep only a specific subset of columns to create a cleaner feature table for downstream machine learning. Which Galaxy tool should I use?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3', 'Cut1']
- alternatives added: `True`
- note: Manual: the tutorial uses Advanced Cut to keep a specific column from a tabular dataset. Galaxy's core Cut tool can also select a specific column (e.g., column 3), so it is an acceptable alternative.
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:260`: > <hands-on-title>Advanced Cut</hands-on-title>
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:262`: > - {% tool [Advanced Cut](toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/1.1.0) %}
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:266`: >    - *"Cut by"*: Select `fields`

### `statistics-fruit_360-q012`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I need to convert the class label column into a categorical/one-hot matrix before training. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:276`: > - {% tool [To categorical](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.8.3) %}

### `statistics-fruit_360-q013`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:288`: > - {% tool [Create a deep learning model architecture](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.5.0) %}

### `statistics-fruit_360-q014`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to create a trainable neural network from an architecture definition (without writing code). Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:351`: > - {% tool [Create deep learning model](toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/0.5.0) %}

### `statistics-fruit_360-q015`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:376`: > - {% tool [Deep learning training and evaluation](toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.8.2) %}

### `statistics-fruit_360-q016`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:396`: > - {% tool [Model Prediction](toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.8.2) %}

### `statistics-fruit_360-q017`

- tutorial: `topics/statistics/tutorials/fruit_360`
- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to visualize model performance and outputs to spot obvious issues. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/fruit_360/tutorial.md:414`: > - {% tool [Machine Learning Visualization Extension](toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.2) %}

### `statistics-galaxy-ludwig-q011`

- tutorial: `topics/statistics/tutorials/galaxy-ludwig`
- query: I'm working with a machine learning dataset where you want to train and evaluate a predictive model. I want to train a deep learning model from a declarative config (features/targets specified in YAML/JSON). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-hyperdimensional_computing-q011`

- tutorial: `topics/statistics/tutorials/hyperdimensional_computing`
- query: I'm working with a machine learning dataset where you want to train and evaluate a predictive model. I want to train and evaluate a hyperdimensional computing classifier. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.9.post1+galaxy0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/hyperdimensional_computing/tutorial.md:94`: > {% tool [chopin2](toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.7+galaxy1) %} with the following configuration:
  - `training-material/topics/statistics/tutorials/hyperdimensional_computing/tutorial.md:129`: > {% tool [chopin2](toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.7+galaxy1) %} with the following configuration:

### `statistics-intro_deep_learning-q011`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Also, I’d like the run to be reproducible (same results if I rerun it). Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-intro_deep_learning-q012`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I want a quick way to see where the classifier is making mistakes. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-intro_deep_learning-q013`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I have training + validation splits and need the step that fits the model and reports performance. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-intro_deep_learning-q014`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I want to create a trainable neural network from an architecture definition (without writing code). Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-intro_deep_learning-q015`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-intro_deep_learning-q016`

- tutorial: `topics/statistics/tutorials/intro_deep_learning`
- query: I'm analyzing a machine learning dataset where you want to train and evaluate a predictive model. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I want to keep the outputs easy to inspect and debug. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `0` (manual check recommended; tool may be referenced by display name or an older version)

### `statistics-machinelearning-q011`

- tutorial: `topics/statistics/tutorials/machinelearning`
- query: I have a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to fit an SVM for classification and inspect performance metrics. Also, I want to inspect predicted vs true values to spot obvious issues. Is there a Galaxy tool that can handle this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/machinelearning/tutorial.md:101`: > {% tool [Support vector machines (SVMs) for classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %} with the following parameters to train:
  - `training-material/topics/statistics/tutorials/machinelearning/tutorial.md:122`: > {% tool [Support vector machines (SVMs) for classification](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0) %} with the following parameters:

### `statistics-regression_machinelearning-q011`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I’d like to fit a generalized linear model and examine coefficients plus prediction performance. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `2` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:136`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:172`: > 1. {% tool [Generalized linear models for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0) %}:

### `statistics-regression_machinelearning-q012`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need regression performance visualizations to check how good my predictions are. Also, I’d like a quick run on a small subset first. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:198`: > {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:306`: > {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:422`: > {% tool [Plot actual vs predicted curves and residual plots](toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1) %}:

### `statistics-regression_machinelearning-q013`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `3` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:262`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:295`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:409`: > 1. {% tool [Ensemble methods for classification and regression](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0) %}:

### `statistics-regression_machinelearning-q014`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I’m preparing for cross-validation and need one object that includes preprocessing plus the model. Also, I want to inspect predicted vs true values to spot obvious issues. What’s the right Galaxy tool for this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:322`: > {% tool [Pipeline builder](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0) %}:

### `statistics-regression_machinelearning-q015`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I'm analyzing a machine learning dataset where you want to train and evaluate a predictive model. I want an automated hyperparameter search with CV and a ranked summary of results. Also, I’d like a quick run on a small subset first. Which tool in Galaxy can do this?
- gold tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0']
- alternatives added: `False`
- decision: keep single-tool gold (no safe alternative identified during manual review)
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:349`: > {% tool [Hyperparameter search](toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0) %}:

### `statistics-regression_machinelearning-q016`

- tutorial: `topics/statistics/tutorials/regression_machinelearning`
- query: I have a text/tabular file where the first lines are metadata or a header block, and I need to remove them before analysis. Which Galaxy tool should I use?
- gold tools: ['Remove beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3']
- alternatives added: `True`
- note: Manual: this step removes the first line (header) from a tabular file. A sed-based text transformation can delete the first line (e.g., '1d'), so it is a valid alternative to the dedicated 'Remove beginning' tool.
- tutorial.md hits: `1` (showing up to 3)
  - `training-material/topics/statistics/tutorials/regression_machinelearning/tutorial.md:187`: > 1. **Remove beginning of a file** {% icon tool %} with the following parameters:

