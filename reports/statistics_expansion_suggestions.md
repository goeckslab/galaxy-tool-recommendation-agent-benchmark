# Statistics expansion suggestions (manual review required)

- Items considered: `60` (subset of statistics items without current alternatives)
- Tool catalog: `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl`
- top_n: `6` min_score: `0.28`

These are *suggestions only*. Do not add alternatives unless you can justify them with IO compatibility + tool_help_text.

## `statistics-CNN-q011`

- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. My labels are a single column of class IDs, but the model expects one-hot targets. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0`
- suggestions: `0`

## `statistics-CNN-q012`

- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
- suggestions: `3`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.5.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['architecture', 'shape']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['architecture', 'shape']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.4.2` (Create a deep learning model architecture) score=0.77
    - why: io_sim=1.00, txt_sim=0.25, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['architecture', 'shape']

## `statistics-CNN-q013`

- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I already have a saved architecture/config and want to instantiate the actual model object. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
- suggestions: `0`

## `statistics-CNN-q014`

- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data). Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
- suggestions: `0`

## `statistics-CNN-q015`

- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
- suggestions: `0`

## `statistics-CNN-q016`

- query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want a quick visualization summary of my ML experiment outputs for inspection. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.10.0` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi', 'visualization']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.2` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi', 'visualization']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.3` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi', 'visualization']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.4` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi', 'visualization']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.1` (Machine Learning Visualization Extension) score=0.88
    - why: io_sim=1.00, txt_sim=0.59, shared_rare=['corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi', 'visualization']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.7.12` (Machine Learning Visualization Extension) score=0.86
    - why: io_sim=1.00, txt_sim=0.52, shared_rare=['corss', 'gridscores', 'multpi', 'precison'], shared_query=['multi', 'visualization']

## `statistics-FNN-q011`

- query: I have a tabular classification task with many numeric features. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
- suggestions: `3`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.5.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['keras']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['keras']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.4.2` (Create a deep learning model architecture) score=0.77
    - why: io_sim=1.00, txt_sim=0.25, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['keras']

## `statistics-FNN-q012`

- query: I'm analyzing a tabular classification task with many numeric features. I want to create a trainable neural network from an architecture definition (without writing code). Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
- suggestions: `0`

## `statistics-FNN-q013`

- query: I have a tabular classification task with many numeric features. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I need to control epochs and batch size. What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
- suggestions: `2`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.11.0` (Build Deep learning Batch Training Models) score=0.36
    - why: io_sim=0.50, txt_sim=0.07, shared_rare=['genomicintervalbatchgenerator'], shared_query=['batch', 'control', 'deep', 'learning']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.10.0` (Build Deep learning Batch Training Models) score=0.35
    - why: io_sim=0.50, txt_sim=0.05, shared_rare=['genomicintervalbatchgenerator'], shared_query=['batch', 'deep', 'learning']

## `statistics-FNN-q014`

- query: I have a tabular classification task with many numeric features. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
- suggestions: `0`

## `statistics-FNN-q015`

- query: I'm working with a tabular classification task with many numeric features. I want interactive plots to evaluate a regression model (predicted vs true, residuals). Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1`
- suggestions: `2`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4` (Plot confusion matrix, precision, recall and ROC and AUC curves) score=0.89
    - why: io_sim=1.00, txt_sim=0.62, tabular_input=yes, shared_rare=['buried', 'curves', 'interactive', 'jpeg', 'plotted', 'rich', 'saved'], shared_query=['interactive', 'predicted', 'true']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.2` (Parallel Coordinates Plot) score=0.37
    - why: io_sim=0.25, txt_sim=0.40, tabular_input=yes, shared_rare=['buried', 'interactive', 'jpeg', 'rich', 'saved'], shared_query=['interactive']

## `statistics-RNN-q011`

- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I’m prototyping a model and need a step that prepares a written architecture specification for building. What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
- suggestions: `3`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.5.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['architecture']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['architecture']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.4.2` (Create a deep learning model architecture) score=0.77
    - why: io_sim=1.00, txt_sim=0.25, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['architecture']

## `statistics-RNN-q012`

- query: In my project I’m using a sequence/time-series dataset where order matters (e.g., for classification). I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
- suggestions: `1`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.11.0` (Build Deep learning Batch Training Models) score=0.80
    - why: io_sim=1.00, txt_sim=0.43, shared_rare=['compile', 'ftrl'], shared_query=['builds']

## `statistics-RNN-q013`

- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I have training + validation splits and need the step that fits the model and reports performance. Also, I want early stopping if validation performance stops improving. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
- suggestions: `2`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.11.0` (Build Deep learning Batch Training Models) score=0.36
    - why: io_sim=0.50, txt_sim=0.07, shared_rare=['genomicintervalbatchgenerator'], shared_query=['improving']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.10.0` (Build Deep learning Batch Training Models) score=0.35
    - why: io_sim=0.50, txt_sim=0.05, shared_rare=['genomicintervalbatchgenerator'], shared_query=['improving']

## `statistics-RNN-q014`

- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I want to run inference using a previously trained model and export the predicted classes. Also, I want a simple table mapping each sample to its prediction. What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
- suggestions: `0`

## `statistics-RNN-q015`

- query: I have a sequence/time-series dataset where order matters (e.g., for classification). I need a compact set of plots to sanity-check training/evaluation results. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0`
- suggestions: `0`

## `statistics-age-prediction-with-ml-q011`

- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to bundle preprocessing (scaling/encoding) and the estimator into one pipeline for consistent CV. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0`
- suggestions: `0`

## `statistics-age-prediction-with-ml-q012`

- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to do cross-validated hyperparameter tuning (grid/random search) and pick the best settings. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0`
- suggestions: `0`

## `statistics-age-prediction-with-ml-q013`

- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I ran hyperparameter tuning and want a parallel coordinates plot to see which settings correlate with performance. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.2`
- suggestions: `1`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.1` (Parallel Coordinates Plot) score=0.51
    - why: io_sim=0.75, txt_sim=0.07, target_column=yes, tabular_input=yes, shared_rare=['parallel'], shared_query=['coordinates', 'parallel']

## `statistics-age-prediction-with-ml-q014`

- query: I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0` (Generalized linear models) score=0.83
    - why: io_sim=1.00, txt_sim=0.55, shared_rare=['specifiy', 'trainig'], shared_query=['regression']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.10.0` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['boosting', 'ensemble', 'regression']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.7.12` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['boosting', 'ensemble', 'regression']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.1` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['boosting', 'ensemble', 'regression']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.2` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['boosting', 'ensemble', 'regression']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.3` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['boosting', 'ensemble', 'regression']

## `statistics-age-prediction-with-ml-q015`

- query: I have a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I need regression performance visualizations to check how good my predictions are. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1`
- suggestions: `0`

## `statistics-classification_machinelearning-q011`

- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want a simple, interpretable regression/classification model (linear/logistic) with evaluation. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0`
- suggestions: `3`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_lightgbm/sklearn_lightgbm/1.0.11.0` (LightGBM) score=0.87
    - why: io_sim=1.00, txt_sim=0.58, shared_rare=['expects', 'huber', 'predicts', 'respective', 'returned'], shared_query=['classify']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0` (Ensemble methods) score=0.86
    - why: io_sim=1.00, txt_sim=0.55, shared_rare=['expects', 'predicts', 'respective', 'returned', 'specifiy', 'trainig'], shared_query=['classify']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_discriminant_classifier/sklearn_discriminant_classifier/1.0.11.0` (Discriminant Analysis) score=0.81
    - why: io_sim=1.00, txt_sim=0.36, shared_rare=['expects', 'predicts', 'trainig'], shared_query=['classify']

## `statistics-classification_machinelearning-q012`

- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want an interactive plot summarizing classification performance (ROC/PR/confusion-matrix style). Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4`
- suggestions: `2`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1` (Plot actual vs predicted curves and residual plots) score=0.89
    - why: io_sim=1.00, txt_sim=0.62, tabular_input=yes, shared_rare=['buried', 'curves', 'interactive', 'jpeg', 'plotted', 'rich', 'saved'], shared_query=['interactive']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.2` (Parallel Coordinates Plot) score=0.35
    - why: io_sim=0.25, txt_sim=0.34, tabular_input=yes, shared_rare=['buried', 'interactive', 'jpeg', 'rich', 'saved'], shared_query=['interactive']

## `statistics-classification_machinelearning-q013`

- query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to run k-nearest neighbors classification and evaluate it (e.g., with CV). Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.10.0` (Nearest Neighbors Classification) score=0.95
    - why: io_sim=1.00, txt_sim=0.83, shared_rare=['balltree', 'brute', 'equally', 'inverse', 'kdtree', 'neighborhood', 'radius', 'weight'], shared_query=['classification', 'nearest', 'neighbors']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.7.12` (Nearest Neighbors Classification) score=0.95
    - why: io_sim=1.00, txt_sim=0.83, shared_rare=['balltree', 'brute', 'equally', 'inverse', 'kdtree', 'neighborhood', 'radius', 'weight'], shared_query=['classification', 'nearest', 'neighbors']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.8.1` (Nearest Neighbors Classification) score=0.95
    - why: io_sim=1.00, txt_sim=0.83, shared_rare=['balltree', 'brute', 'equally', 'inverse', 'kdtree', 'neighborhood', 'radius', 'weight'], shared_query=['classification', 'nearest', 'neighbors']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.8.2` (Nearest Neighbors Classification) score=0.95
    - why: io_sim=1.00, txt_sim=0.83, shared_rare=['balltree', 'brute', 'equally', 'inverse', 'kdtree', 'neighborhood', 'radius', 'weight'], shared_query=['classification', 'nearest', 'neighbors']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.8.3` (Nearest Neighbors Classification) score=0.95
    - why: io_sim=1.00, txt_sim=0.83, shared_rare=['balltree', 'brute', 'equally', 'inverse', 'kdtree', 'neighborhood', 'radius', 'weight'], shared_query=['classification', 'nearest', 'neighbors']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.8.4` (Nearest Neighbors Classification) score=0.95
    - why: io_sim=1.00, txt_sim=0.83, shared_rare=['balltree', 'brute', 'equally', 'inverse', 'kdtree', 'neighborhood', 'radius', 'weight'], shared_query=['classification', 'nearest', 'neighbors']

## `statistics-classification_machinelearning-q015`

- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I’d like to fit an ensemble model for prediction and compare its performance to other methods. Also, I want to inspect predicted vs true values to spot obvious issues. What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0` (Generalized linear models) score=0.83
    - why: io_sim=1.00, txt_sim=0.55, shared_rare=['specifiy', 'trainig'], shared_query=['classify', 'like', 'methods', 'predicted']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.10.0` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble', 'methods']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.7.12` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble', 'methods', 'true']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.1` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble', 'methods', 'true']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.2` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble', 'methods', 'true']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.3` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble', 'methods', 'true']

## `statistics-classification_machinelearning-q016`

- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I have preprocessing steps and a model; I want to chain them into a single reusable pipeline. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0`
- suggestions: `0`

## `statistics-classification_machinelearning-q017`

- query: I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I need to compare hyperparameter combinations with CV and select the best-performing model. Also, I care about picking a scoring metric that matches my goal. What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0`
- suggestions: `0`

## `statistics-classification_regression-q012`

- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want performance plots to compare models across metrics. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4`
- suggestions: `0`

## `statistics-classification_regression-q013`

- query: In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need an ensemble approach for classification/regression and want metrics on held-out data. Also, I want the result to be easy to plug into the next step. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0` (Generalized linear models) score=0.83
    - why: io_sim=1.00, txt_sim=0.55, shared_rare=['specifiy', 'trainig'], shared_query=['there']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.10.0` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.7.12` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.1` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.2` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.8.3` (Ensemble methods) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['deviance', 'gain', 'gini', 'impurity', 'recovers', 'samme'], shared_query=['ensemble']

## `statistics-classification_regression-q014`

- query: I have a machine learning dataset where you want to train and evaluate a predictive model. I want plots that summarize regression accuracy and error patterns. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1`
- suggestions: `0`

## `statistics-clustering_machinelearning-q011`

- query: I'm working with a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to cluster samples based on numeric features and get cluster assignments. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.10.0` (Numeric Clustering) score=0.93
    - why: io_sim=1.00, txt_sim=0.78, shared_rare=['agglomerative', 'birch', 'brute', 'dbscan', 'discretize', 'elkan', 'lobpcg', 'meanshift'], shared_query=['clustering', 'numeric']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.7.12` (Numeric Clustering) score=0.93
    - why: io_sim=1.00, txt_sim=0.78, shared_rare=['agglomerative', 'birch', 'brute', 'dbscan', 'discretize', 'elkan', 'lobpcg', 'meanshift'], shared_query=['clustering', 'numeric']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.8.1` (Numeric Clustering) score=0.93
    - why: io_sim=1.00, txt_sim=0.78, shared_rare=['agglomerative', 'birch', 'brute', 'dbscan', 'discretize', 'elkan', 'lobpcg', 'meanshift'], shared_query=['clustering', 'numeric']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.8.2` (Numeric Clustering) score=0.93
    - why: io_sim=1.00, txt_sim=0.78, shared_rare=['agglomerative', 'birch', 'brute', 'dbscan', 'discretize', 'elkan', 'lobpcg', 'meanshift'], shared_query=['clustering', 'numeric']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.8.3` (Numeric Clustering) score=0.93
    - why: io_sim=1.00, txt_sim=0.78, shared_rare=['agglomerative', 'birch', 'brute', 'dbscan', 'discretize', 'elkan', 'lobpcg', 'meanshift'], shared_query=['clustering', 'numeric']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.8.4` (Numeric Clustering) score=0.93
    - why: io_sim=1.00, txt_sim=0.78, shared_rare=['agglomerative', 'birch', 'brute', 'dbscan', 'discretize', 'elkan', 'lobpcg', 'meanshift'], shared_query=['clustering', 'numeric']

## `statistics-clustering_machinelearning-q012`

- query: I have a table of x/y values (and optionally a group column) and want a simple scatter plot for quick exploratory data analysis. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/iuc/ggplot2_point/ggplot2_point/3.4.0+galaxy1`
- suggestions: `0`

## `statistics-flexynesis_cbio_import-q011`

- query: I need to pull multi-omics data and clinical labels from a cancer portal and organize them into analysis-ready tables in R. Which Galaxy tool should I use for an interactive R/Bioconductor session?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_cbio_import-q013`

- query: I need to derive a new column in a tabular file from existing columns (basic expressions/arithmetic) to prepare metadata for modeling. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2`
- suggestions: `0`

## `statistics-flexynesis_cbio_import-q014`

- query: I need to keep only specific columns from a tabular dataset (like selecting an ID column plus a small set of features) before merging tables. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.3+galaxy1` (Advanced Cut) score=0.79
    - why: io_sim=1.00, txt_sim=0.31, shared_rare=['dash', 'underscore', 'whitespace'], shared_query=['keep']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.3+galaxy2` (Advanced Cut) score=0.79
    - why: io_sim=1.00, txt_sim=0.31, shared_rare=['dash', 'underscore', 'whitespace'], shared_query=['keep']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy0` (Advanced Cut) score=0.79
    - why: io_sim=1.00, txt_sim=0.31, shared_rare=['dash', 'underscore', 'whitespace'], shared_query=['keep']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy2` (Advanced Cut) score=0.79
    - why: io_sim=1.00, txt_sim=0.31, shared_rare=['dash', 'underscore', 'whitespace'], shared_query=['keep']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/1.1.0` (Advanced Cut) score=0.79
    - why: io_sim=1.00, txt_sim=0.29, shared_rare=['dash', 'underscore', 'whitespace'], shared_query=['keep']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/1.0.0` (Cut) score=0.78
    - why: io_sim=1.00, txt_sim=0.27, shared_rare=['dash', 'underscore', 'whitespace'], shared_query=['keep']

## `statistics-flexynesis_cbio_import-q015`

- query: I need to sort a tabular dataset by one or more columns while keeping the header intact, so downstream merges behave predictably. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3`
- suggestions: `0`

## `statistics-flexynesis_cbio_import-q016`

- query: I want to run a short R script to reshape/clean a set of omics tables (renaming columns, harmonizing sample IDs) and inspect the results. Which Galaxy tool should I use for an interactive R session?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_cbio_import-q017`

- query: I need to do a bit of custom data preparation in R (sanity checks, small transformations, and quick plots) before training a model. Which Galaxy tool should I use in Galaxy?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_classification-q011`

- query: I want to train a classifier on multi-omics data in R and then inspect feature importance/embeddings to understand what the model learned. Which Galaxy tool should I use for an interactive R/Bioconductor workflow?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_classification-q013`

- query: I have a tabular file with a header and want to sort the rows by a key column without breaking the header line. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3`
- suggestions: `0`

## `statistics-flexynesis_classification-q014`

- query: I have model outputs (predictions/embeddings) and want to generate a few publication-style plots in R and tweak them interactively. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_classification-q015`

- query: I need to compute a derived column in a tabular dataset (for example, create a label column from existing metadata fields) before modeling. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2`
- suggestions: `0`

## `statistics-flexynesis_classification-q018`

- query: I have a wide table and need to select a specific set of columns (including a few feature columns plus an ID). Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3`
- suggestions: `1`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3` (Join) score=0.35
    - why: io_sim=0.33, txt_sim=0.16, shared_rare=['apple', 'banana', 'fruit', 'price'], shared_query=['plus']

## `statistics-flexynesis_classification-q019`

- query: I need to join two tabular datasets on a shared key, but I also want control over which columns are kept from each side. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/1.0.0` (Join) score=0.71
    - why: io_sim=1.00, txt_sim=0.24, target_column=yes, tabular_input=yes, shared_rare=['unpairable'], shared_query=['join']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/1.1.0` (Join) score=0.71
    - why: io_sim=1.00, txt_sim=0.24, target_column=yes, tabular_input=yes, shared_rare=['unpairable'], shared_query=['join']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/1.1.1` (Join) score=0.71
    - why: io_sim=1.00, txt_sim=0.24, target_column=yes, tabular_input=yes, shared_rare=['unpairable'], shared_query=['join']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/1.1.2` (Join) score=0.71
    - why: io_sim=1.00, txt_sim=0.24, target_column=yes, tabular_input=yes, shared_rare=['unpairable'], shared_query=['join']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.3+galaxy1` (Join) score=0.71
    - why: io_sim=1.00, txt_sim=0.24, target_column=yes, tabular_input=yes, shared_rare=['unpairable'], shared_query=['join']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy0` (Join) score=0.71
    - why: io_sim=1.00, txt_sim=0.24, target_column=yes, tabular_input=yes, shared_rare=['unpairable'], shared_query=['join']

## `statistics-flexynesis_classification-q020`

- query: I need to transpose a tabular matrix (swap rows and columns) so that samples are rows and features are columns (or vice versa). Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.9+galaxy0`
- suggestions: `5`
  - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.0.6` (Transpose) score=0.64
    - why: io_sim=1.00, txt_sim=0.02, tabular_input=yes, shared_rare=['transpose'], shared_query=['transpose']
  - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.1.0` (Transpose) score=0.64
    - why: io_sim=1.00, txt_sim=0.02, tabular_input=yes, shared_rare=['transpose'], shared_query=['transpose']
  - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.1.0+galaxy2` (Transpose) score=0.64
    - why: io_sim=1.00, txt_sim=0.02, tabular_input=yes, shared_rare=['transpose'], shared_query=['transpose']
  - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.8+galaxy0` (Transpose) score=0.64
    - why: io_sim=1.00, txt_sim=0.02, tabular_input=yes, shared_rare=['transpose'], shared_query=['transpose']
  - `toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.8+galaxy1` (Transpose) score=0.64
    - why: io_sim=1.00, txt_sim=0.02, tabular_input=yes, shared_rare=['transpose'], shared_query=['transpose']

## `statistics-flexynesis_classification-q021`

- query: I'm working with a multi-omics dataset to predict breast cancer subtypes and interpret learned features. I want to try multiple models automatically on tabular data and see which performs best. Which tool in Galaxy can do this?
- gold: `toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4`
- suggestions: `0`

## `statistics-flexynesis_survival-q011`

- query: I want to build a model in R that relates omics features to survival outcomes and then produce standard survival plots and summaries. Which Galaxy tool should I use for an interactive R/Bioconductor session?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_survival-q013`

- query: I need to summarize a tabular dataset by applying simple operations across columns/rows (e.g., min/max/mean or group-wise summaries). Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0`
- suggestions: `0`

## `statistics-flexynesis_survival-q014`

- query: I have a tabular dataset and want to create a new column by combining or transforming existing columns (e.g., derive a time-to-event label). Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1`
- suggestions: `0`

## `statistics-flexynesis_survival-q015`

- query: I need to clean up values in a specific column (e.g., replace strings, normalize identifiers) before merging with clinical metadata. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_replace_in_column/9.5+galaxy3`
- suggestions: `0`

## `statistics-flexynesis_survival-q016`

- query: I want to generate survival-related figures in R (Kaplan–Meier curves and risk tables) and iterate on the plot styling interactively. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_unsupervised-q011`

- query: I want to do unsupervised analysis in R on multi-omics data (learn latent representations and visualize clusters/UMAP). Which Galaxy tool should I use for an interactive R/Bioconductor workflow?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_unsupervised-q013`

- query: I need to do a few small but custom data transformations in R (reshaping tables, checking sample alignment) before running unsupervised modeling. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-flexynesis_unsupervised-q014`

- query: I have an embedding/latent-space output and want to make exploratory plots (UMAP/cluster plots) in R and adjust parameters interactively. Which Galaxy tool should I use?
- gold: `toolshed.g2.bx.psu.edu/repos/enis/interactive_tool_rstudio_bioconductor/interactive_tool_rstudio_bioconductor/4.6.0+3.22.galaxy0`
- suggestions: `0`

## `statistics-fruit_360-q012`

- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I need to convert the class label column into a categorical/one-hot matrix before training. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0`
- suggestions: `0`

## `statistics-fruit_360-q013`

- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
- suggestions: `3`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.5.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['keras']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.10.0` (Create a deep learning model architecture) score=0.78
    - why: io_sim=1.00, txt_sim=0.26, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['keras']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/0.4.2` (Create a deep learning model architecture) score=0.77
    - why: io_sim=1.00, txt_sim=0.25, shared_rare=['relu', 'selu', 'softplus', 'softsign'], shared_query=['keras']

## `statistics-fruit_360-q014`

- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to create a trainable neural network from an architecture definition (without writing code). Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
- suggestions: `0`

## `statistics-fruit_360-q015`

- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
- suggestions: `2`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.11.0` (Build Deep learning Batch Training Models) score=0.36
    - why: io_sim=0.50, txt_sim=0.07, shared_rare=['genomicintervalbatchgenerator'], shared_query=['deep', 'learning']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/keras_batch_models/keras_batch_models/1.0.10.0` (Build Deep learning Batch Training Models) score=0.35
    - why: io_sim=0.50, txt_sim=0.05, shared_rare=['genomicintervalbatchgenerator'], shared_query=['deep', 'learning']

## `statistics-fruit_360-q016`

- query: In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
- suggestions: `0`

## `statistics-fruit_360-q017`

- query: I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to visualize model performance and outputs to spot obvious issues. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
- gold: `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0`
- suggestions: `6`
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.10.0` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.2` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.3` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.4` (Machine Learning Visualization Extension) score=0.93
    - why: io_sim=1.00, txt_sim=0.77, shared_rare=['autumn', 'corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.8.1` (Machine Learning Visualization Extension) score=0.88
    - why: io_sim=1.00, txt_sim=0.59, shared_rare=['corss', 'gridscores', 'matplotlib', 'multpi', 'precison'], shared_query=['image', 'multi']
  - `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.7.12` (Machine Learning Visualization Extension) score=0.86
    - why: io_sim=1.00, txt_sim=0.52, shared_rare=['corss', 'gridscores', 'multpi', 'precison'], shared_query=['multi']

