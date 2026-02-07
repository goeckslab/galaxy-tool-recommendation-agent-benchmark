# GTN Benchmark Items (Readable)

## Deep Learning (Part 3) - Convolutional neural networks (CNN) (topics/statistics/tutorials/CNN)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0
- Datasets (1): 4697906

Questions:
- **statistics-CNN-q011** — I'm working with a labeled image dataset (handwritten digits) for multi-class classification. My labels are a single column of class IDs, but the model expects one-hot targets. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0
  - Datasets: 4697906
- **statistics-CNN-q012** — I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
  - Datasets: 4697906
- **statistics-CNN-q013** — I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I already have a saved architecture/config and want to instantiate the actual model object. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0
  - Datasets: 4697906
- **statistics-CNN-q014** — I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: 4697906
- **statistics-CNN-q015** — I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0
  - Datasets: 4697906
- **statistics-CNN-q016** — I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want a quick visualization summary of my ML experiment outputs for inspection. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0
  - Datasets: 4697906

## Deep Learning (Part 1) - Feedforward neural networks (FNN) (topics/statistics/tutorials/FNN)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
- Datasets (3): 4660497, X_test.tsv, X_train.tsv

Questions:
- **statistics-FNN-q011** — I have a tabular classification task with many numeric features. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
  - Datasets: 4660497, X_test.tsv, X_train.tsv
- **statistics-FNN-q012** — I'm analyzing a tabular classification task with many numeric features. I want to create a trainable neural network from an architecture definition (without writing code). Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0
  - Datasets: 4660497, X_test.tsv, X_train.tsv
- **statistics-FNN-q013** — I have a tabular classification task with many numeric features. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I need to control epochs and batch size. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: 4660497, X_test.tsv, X_train.tsv
- **statistics-FNN-q014** — I have a tabular classification task with many numeric features. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0
  - Datasets: 4660497, X_test.tsv, X_train.tsv
- **statistics-FNN-q015** — I'm working with a tabular classification task with many numeric features. I want interactive plots to evaluate a regression model (predicted vs true, residuals). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1
  - Datasets: 4660497, X_test.tsv, X_train.tsv

## Deep Learning (Part 2) - Recurrent neural networks (RNN) (topics/statistics/tutorials/RNN)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
- Datasets (3): 4477881, X_test.tsv, X_train.tsv

Questions:
- **statistics-RNN-q011** — I have a sequence/time-series dataset where order matters (e.g., for classification). I’m prototyping a model and need a step that prepares a written architecture specification for building. What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
  - Datasets: 4477881, X_test.tsv, X_train.tsv
- **statistics-RNN-q012** — In my project I’m using a sequence/time-series dataset where order matters (e.g., for classification). I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0
  - Datasets: 4477881, X_test.tsv, X_train.tsv
- **statistics-RNN-q013** — I have a sequence/time-series dataset where order matters (e.g., for classification). I have training + validation splits and need the step that fits the model and reports performance. Also, I want early stopping if validation performance stops improving. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: 4477881, X_test.tsv, X_train.tsv
- **statistics-RNN-q014** — I have a sequence/time-series dataset where order matters (e.g., for classification). I want to run inference using a previously trained model and export the predicted classes. Also, I want a simple table mapping each sample to its prediction. What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0
  - Datasets: 4477881, X_test.tsv, X_train.tsv
- **statistics-RNN-q015** — I have a sequence/time-series dataset where order matters (e.g., for classification). I need a compact set of plots to sanity-check training/evaluation results. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0
  - Datasets: 4477881, X_test.tsv, X_train.tsv

## Age prediction using machine learning (topics/statistics/tutorials/age-prediction-with-ml)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0
- Datasets (3): 2545213, 2545213#.XEWTJ9-YVa0, training_data_normal.tsv

Questions:
- **statistics-age-prediction-with-ml-q011** — I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to bundle preprocessing (scaling/encoding) and the estimator into one pipeline for consistent CV. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0
  - Datasets: 2545213, training_data_normal.tsv, 2545213#.XEWTJ9-YVa0
- **statistics-age-prediction-with-ml-q012** — I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to do cross-validated hyperparameter tuning (grid/random search) and pick the best settings. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0
  - Datasets: 2545213, training_data_normal.tsv, 2545213#.XEWTJ9-YVa0
- **statistics-age-prediction-with-ml-q013** — I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I ran hyperparameter tuning and want a parallel coordinates plot to see which settings correlate with performance. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_parallel_coordinates_plot/plotly_parallel_coordinates_plot/0.2
  - Datasets: 2545213, training_data_normal.tsv, 2545213#.XEWTJ9-YVa0
- **statistics-age-prediction-with-ml-q014** — I'm working with a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 2545213, training_data_normal.tsv, 2545213#.XEWTJ9-YVa0
- **statistics-age-prediction-with-ml-q015** — I have a high-dimensional biomarker feature table (e.g., RNA-seq or DNA methylation) to predict chronological age (regression). I need regression performance visualizations to check how good my predictions are. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1
  - Datasets: 2545213, training_data_normal.tsv, 2545213#.XEWTJ9-YVa0

## Classification in Machine Learning (topics/statistics/tutorials/classification_machinelearning)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
- Datasets (3): 3738729, test_rows_labels.csv, train_rows.csv

Questions:
- **statistics-classification_machinelearning-q011** — I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want a simple, interpretable regression/classification model (linear/logistic) with evaluation. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q012** — I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want an interactive plot summarizing classification performance (ROC/PR/confusion-matrix style). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q013** — I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to run k-nearest neighbors classification and evaluate it (e.g., with CV). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_nn_classifier/sklearn_nn_classifier/1.0.11.0
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q014** — I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to train an SVM classifier and evaluate accuracy with a proper train/test split. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q015** — I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I’d like to fit an ensemble model for prediction and compare its performance to other methods. Also, I want to inspect predicted vs true values to spot obvious issues. What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q016** — I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I have preprocessing steps and a model; I want to chain them into a single reusable pipeline. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q017** — I have a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I need to compare hyperparameter combinations with CV and select the best-performing model. Also, I care about picking a scoring metric that matches my goal. What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv
- **statistics-classification_machinelearning-q018** — I want to drop the first few lines of a text/tabular file as a quick cleanup step before importing it into downstream tools. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3
  - Datasets: 3738729, train_rows.csv, test_rows_labels.csv

## Machine learning: classification and regression (topics/statistics/tutorials/classification_regression)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
- Datasets (3): 2579649, breast-w_targets.tsv, breast-w_test.tsv

Questions:
- **statistics-classification_regression-q011** — I have a machine learning dataset where you want to train and evaluate a predictive model. I need a support vector machine classifier for my feature matrix and evaluation outputs. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 2579649, breast-w_targets.tsv, breast-w_test.tsv
- **statistics-classification_regression-q012** — I have a machine learning dataset where you want to train and evaluate a predictive model. I want performance plots to compare models across metrics. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_ml_performance_plots/plotly_ml_performance_plots/0.4
  - Datasets: 2579649, breast-w_targets.tsv, breast-w_test.tsv
- **statistics-classification_regression-q013** — In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need an ensemble approach for classification/regression and want metrics on held-out data. Also, I want the result to be easy to plug into the next step. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 2579649, breast-w_targets.tsv, breast-w_test.tsv
- **statistics-classification_regression-q014** — I have a machine learning dataset where you want to train and evaluate a predictive model. I want plots that summarize regression accuracy and error patterns. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1
  - Datasets: 2579649, breast-w_targets.tsv, breast-w_test.tsv

## Clustering in Machine Learning (topics/statistics/tutorials/clustering_machinelearning)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.11.0
- Datasets (3): 3813447, circles.csv, iris.csv

Questions:
- **statistics-clustering_machinelearning-q011** — I'm working with a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to cluster samples based on numeric features and get cluster assignments. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_numeric_clustering/sklearn_numeric_clustering/1.0.11.0
  - Datasets: 3813447, iris.csv, circles.csv
- **statistics-clustering_machinelearning-q012** — I have a table of x/y values (and optionally a group column) and want a simple scatter plot for quick exploratory data analysis. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/ggplot2_point/ggplot2_point/3.4.0+galaxy1
  - Datasets: 3813447, iris.csv, circles.csv

## Prepare Data from CbioPortal for Flexynesis Integration (topics/statistics/tutorials/flexynesis_cbio_import)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2
- Datasets (1): 16287482

Questions:
- **statistics-flexynesis_cbio_import-q013** — I need to derive a new column in a tabular file from existing columns (basic expressions/arithmetic) to prepare metadata for modeling. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2
  - Datasets: 16287482
- **statistics-flexynesis_cbio_import-q014** — I need to keep only specific columns from a tabular dataset (like selecting an ID column plus a small set of features) before merging tables. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 16287482
- **statistics-flexynesis_cbio_import-q015** — I need to sort a tabular dataset by one or more columns while keeping the header intact, so downstream merges behave predictably. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3
  - Datasets: 16287482

## Modeling Breast Cancer Subtypes with Flexynesis (topics/statistics/tutorials/flexynesis_classification)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3
- Datasets (3): 16287482, train_cna_brca.tabular, train_gex_brca.tabular

Questions:
- **statistics-flexynesis_classification-q013** — I have a tabular file with a header and want to sort the rows by a key column without breaking the header line. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sort_header_tool/9.5+galaxy3
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q015** — I need to compute a derived column in a tabular dataset (for example, create a label column from existing metadata fields) before modeling. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/table_compute/table_compute/1.2.4+galaxy2
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q016** — I have two tabular datasets that share a sample identifier column and I need to merge them into a single table for downstream analysis. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q017** — Before analysis, I want to quickly take the first N rows of a table to sanity-check formatting and sample IDs. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy3
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q018** — I have a wide table and need to select a specific set of columns (including a few feature columns plus an ID). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q019** — I need to join two tabular datasets on a shared key, but I also want control over which columns are kept from each side. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q020** — I need to transpose a tabular matrix (swap rows and columns) so that samples are rows and features are columns (or vice versa). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/datamash_transpose/datamash_transpose/1.9+galaxy0
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular
- **statistics-flexynesis_classification-q021** — I'm working with a multi-omics dataset to predict breast cancer subtypes and interpret learned features. I want to try multiple models automatically on tabular data and see which performs best. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 16287482, train_cna_brca.tabular, train_gex_brca.tabular

## Identifing Survival Markers of Brain tumor with Flexynesis (topics/statistics/tutorials/flexynesis_survival)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0
- Datasets (3): 16287482, train_clin_lgggbm.tabular, train_mut_lgggbm.tabular

Questions:
- **statistics-flexynesis_survival-q013** — I need to summarize a tabular dataset by applying simple operations across columns/rows (e.g., min/max/mean or group-wise summaries). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.9+galaxy0
  - Datasets: 16287482, train_mut_lgggbm.tabular, train_clin_lgggbm.tabular
- **statistics-flexynesis_survival-q014** — I have a tabular dataset and want to create a new column by combining or transforming existing columns (e.g., derive a time-to-event label). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/column_maker/Add_a_column1/2.1
  - Datasets: 16287482, train_mut_lgggbm.tabular, train_clin_lgggbm.tabular
- **statistics-flexynesis_survival-q015** — I need to clean up values in a specific column (e.g., replace strings, normalize identifiers) before merging with clinical metadata. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_replace_in_column/9.5+galaxy3
  - Datasets: 16287482, train_mut_lgggbm.tabular, train_clin_lgggbm.tabular

## Image classification in Galaxy with fruit 360 dataset (topics/statistics/tutorials/fruit_360)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
- Datasets (1): 5702887

Questions:
- **statistics-fruit_360-q011** — I have a tabular file with many columns and need to keep only a specific subset of columns to create a cleaner feature table for downstream machine learning. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 5702887
- **statistics-fruit_360-q012** — I have a labeled image dataset of fruits/vegetables for multi-class classification. I need to convert the class label column into a categorical/one-hot matrix before training. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0
  - Datasets: 5702887
- **statistics-fruit_360-q013** — In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
  - Datasets: 5702887
- **statistics-fruit_360-q014** — I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to create a trainable neural network from an architecture definition (without writing code). Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0
  - Datasets: 5702887
- **statistics-fruit_360-q015** — In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: 5702887
- **statistics-fruit_360-q016** — In my project I’m using a labeled image dataset of fruits/vegetables for multi-class classification. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0
  - Datasets: 5702887
- **statistics-fruit_360-q017** — I have a labeled image dataset of fruits/vegetables for multi-class classification. I want to visualize model performance and outputs to spot obvious issues. Also, I want the result to be easy to plug into the next step. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0
  - Datasets: 5702887

## Train and Test a Deep learning image classifier with Galaxy-Ludwig (topics/statistics/tutorials/galaxy-ludwig)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
- Datasets (3): mnist_images.zip, mnist_dataset.csv, config.yaml

Questions:
- **statistics-galaxy-ludwig-q011** — I'm working with a machine learning dataset where you want to train and evaluate a predictive model. I want to train a deep learning model from a declarative config (features/targets specified in YAML/JSON). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: mnist_images.zip, mnist_dataset.csv, config.yaml

## A Docker-based interactive Jupyterlab powered by GPU for artificial intelligence in Galaxy (topics/statistics/tutorials/gpu_jupyter_lab)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/iuc/filter_tabular/filter_tabular/3.3.1
- Datasets (1): 6091361

Questions:
- **statistics-gpu_jupyter_lab-q011** — I have a tabular dataset with a numeric score column and only want to keep records above a cutoff (e.g., score >= 0.8). Which Galaxy tool should I use to filter the rows?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/filter_tabular/filter_tabular/3.3.1
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q012** — I have a sample metadata table and want to drop all rows where a column contains a specific keyword (e.g., remove samples labeled as "control"). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_grep_tool/9.5+galaxy3
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q013** — I have a clinical table and want to keep only the rows that satisfy multiple criteria at once (for example: tumor_stage is III/IV AND age_at_diagnosis > 50). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/filter_tabular/filter_tabular/3.3.1
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q014** — Before running a heavy downstream step, I want to exclude rows with missing values in a key column (e.g., drop rows where the label column is empty/NA). Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/filter_tabular/filter_tabular/3.3.1
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q015** — I have a wide feature table and need to keep only an ID column plus a small set of feature columns to create a compact training matrix. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q016** — I need to drop some columns from a tabular file and reorder the remaining columns to match the column order of another dataset. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q017** — I have a tabular file where I only need a contiguous block of columns (e.g., columns 5–200) and I want to discard everything else. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 6091361
- **statistics-gpu_jupyter_lab-q018** — I have a table with metadata columns up front and many feature columns after that. I want to split out only the metadata columns (e.g., the first 4 columns) into a separate table. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3
  - Datasets: 6091361

## Supervised Learning with Hyperdimensional Computing (topics/statistics/tutorials/hyperdimensional_computing)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.9.post1+galaxy0
- Datasets (3): zenodo.6467875, 7806264):, RA__ThomasAM__species.csv

Questions:
- **statistics-hyperdimensional_computing-q011** — I'm working with a machine learning dataset where you want to train and evaluate a predictive model. I want to train and evaluate a hyperdimensional computing classifier. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/chopin2/chopin2/1.0.9.post1+galaxy0
  - Datasets: zenodo.6467875, 7806264):, RA__ThomasAM__species.csv

## Introduction to deep learning (topics/statistics/tutorials/intro_deep_learning)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
- Datasets (3): 3706539, X_test.tsv, X_train.tsv

Questions:
- **statistics-intro_deep_learning-q011** — I have a machine learning dataset where you want to train and evaluate a predictive model. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Also, I’d like the run to be reproducible (same results if I rerun it). Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0
  - Datasets: 3706539, X_test.tsv, X_train.tsv
- **statistics-intro_deep_learning-q012** — I have a machine learning dataset where you want to train and evaluate a predictive model. I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I want a quick way to see where the classifier is making mistakes. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0
  - Datasets: 3706539, X_test.tsv, X_train.tsv
- **statistics-intro_deep_learning-q013** — In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I have training + validation splits and need the step that fits the model and reports performance. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: 3706539, X_test.tsv, X_train.tsv
- **statistics-intro_deep_learning-q014** — In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I want to create a trainable neural network from an architecture definition (without writing code). Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0
  - Datasets: 3706539, X_test.tsv, X_train.tsv
- **statistics-intro_deep_learning-q015** — I have a machine learning dataset where you want to train and evaluate a predictive model. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0
  - Datasets: 3706539, X_test.tsv, X_train.tsv
- **statistics-intro_deep_learning-q016** — I'm analyzing a machine learning dataset where you want to train and evaluate a predictive model. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I want to keep the outputs easy to inspect and debug. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/ludwig_experiment/ludwig_experiment/0.10.1+3
  - Datasets: 3706539, X_test.tsv, X_train.tsv

## Interval-Wise Testing for omics data (topics/statistics/tutorials/iwtomics)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_loadandplot/iwtomics_loadandplot/1.0.0.0
- Datasets (3): zenodo.5589610, Control.bed, ETn_fixed.bed

Questions:
- **statistics-iwtomics-q011** — I have multiple omics signals along genomic coordinates and want to load them, apply smoothing, and generate exploratory plots of signal profiles. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_loadandplot/iwtomics_loadandplot/1.0.0.0
  - Datasets: zenodo.5589610, ETn_fixed.bed, Control.bed
- **statistics-iwtomics-q012** — I want to test for differences in genomic signal profiles between groups and then visualize the test results in a plot. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_testandplot/iwtomics_testandplot/1.0.0.0
  - Datasets: zenodo.5589610, ETn_fixed.bed, Control.bed
- **statistics-iwtomics-q013** — I have statistical test results and want to plot the signal profiles while highlighting regions that pass a chosen significance threshold. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/iwtomics_plotwithscale/iwtomics_plotwithscale/1.0.0.0
  - Datasets: zenodo.5589610, ETn_fixed.bed, Control.bed

## Building the LORIS LLR6 PanCancer Model Using PyCaret (topics/statistics/tutorials/loris_model)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
- Datasets (3): 13885908, Chowell_test_Response.tsv, Chowell_train_Response.tsv

Questions:
- **statistics-loris_model-q011** — I have a machine learning dataset where you want to train and evaluate a predictive model. I need to benchmark a few tabular predictors quickly and pick the top performer. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 13885908, Chowell_train_Response.tsv, Chowell_test_Response.tsv

## Basics of machine learning (topics/statistics/tutorials/machinelearning)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
- Datasets (3): breast-w_test.tsv, breast-w_train.tsv, 1468039

Questions:
- **statistics-machinelearning-q011** — I have a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to fit an SVM for classification and inspect performance metrics. Also, I want to inspect predicted vs true values to spot obvious issues. Is there a Galaxy tool that can handle this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 1468039, breast-w_train.tsv, breast-w_test.tsv

## Regression in Machine Learning (topics/statistics/tutorials/regression_machinelearning)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
- Datasets (3): 2545213, test_rows_labels.csv, train_rows.csv

Questions:
- **statistics-regression_machinelearning-q011** — I have a machine learning dataset where you want to train and evaluate a predictive model. I’d like to fit a generalized linear model and examine coefficients plus prediction performance. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_generalized_linear/sklearn_generalized_linear/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 2545213, train_rows.csv, test_rows_labels.csv
- **statistics-regression_machinelearning-q012** — In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I need regression performance visualizations to check how good my predictions are. Also, I’d like a quick run on a small subset first. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1
  - Datasets: 2545213, train_rows.csv, test_rows_labels.csv
- **statistics-regression_machinelearning-q013** — I have a machine learning dataset where you want to train and evaluate a predictive model. I want to train a tree-based ensemble (random forest / boosting) and evaluate it. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_ensemble/sklearn_ensemble/1.0.11.0, toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4
  - Datasets: 2545213, train_rows.csv, test_rows_labels.csv
- **statistics-regression_machinelearning-q014** — In my project I’m using a machine learning dataset where you want to train and evaluate a predictive model. I’m preparing for cross-validation and need one object that includes preprocessing plus the model. Also, I want to inspect predicted vs true values to spot obvious issues. What’s the right Galaxy tool for this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_build_pipeline/sklearn_build_pipeline/1.0.11.0
  - Datasets: 2545213, train_rows.csv, test_rows_labels.csv
- **statistics-regression_machinelearning-q015** — I'm analyzing a machine learning dataset where you want to train and evaluate a predictive model. I want an automated hyperparameter search with CV and a ranked summary of results. Also, I’d like a quick run on a small subset first. Which tool in Galaxy can do this?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_searchcv/sklearn_searchcv/1.0.11.0
  - Datasets: 2545213, train_rows.csv, test_rows_labels.csv
- **statistics-regression_machinelearning-q016** — I have a text/tabular file where the first lines are metadata or a header block, and I need to remove them before analysis. Which Galaxy tool should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3
  - Datasets: 2545213, train_rows.csv, test_rows_labels.csv
