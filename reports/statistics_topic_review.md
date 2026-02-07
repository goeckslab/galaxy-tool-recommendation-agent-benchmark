# Statistics topic review

- Items scanned: `111`
- Tool catalog used: `data/tool_catalog/usegalaxy_org_all_tools_with_helptext.jsonl` (exists=True)
- Tutorials scanned: `22`

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

## Rewrite audit (rule-based signals)

- `multi_tools`: `13`
- `internal_like_tool_id`: `9`

## Tool spotlight (sanity-check)

### `sklearn_svm_classifier`

- Items: `3`
- `statistics-classification_machinelearning-q014`
  - tool: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0`
  - query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to train an SVM classifier and evaluate accuracy with a proper train/test split. …
- `statistics-classification_regression-q011`
  - tool: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0`
  - query: I have a machine learning dataset where you want to train and evaluate a predictive model. I need a support vector machine classifier for my feature matrix and evaluation outputs. Also, I’d like the r…
- `statistics-machinelearning-q011`
  - tool: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0`
  - query: I have a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to fit an SVM for classification and inspect performance metrics. Also, I want to inspect predicted …

### Exact duplicate query texts under the same tool

- Tools with duplicates: `0`

### Near-duplicate query texts under the same tool (token Jaccard)

- Pairs (>=0.80): `0`

### Needs rewrite: tool leakage in query

- Count: `0`

### Needs rewrite: templated phrasing

- Count: `0`

### Check: internal-like tool IDs

- Count: `9`
- `statistics-flexynesis_classification-q016`
- `statistics-gpu_jupyter_lab-q011`
- `statistics-gpu_jupyter_lab-q012`
- `statistics-gpu_jupyter_lab-q013`
- `statistics-gpu_jupyter_lab-q014`
- `statistics-gpu_jupyter_lab-q015`
- `statistics-gpu_jupyter_lab-q016`
- `statistics-gpu_jupyter_lab-q017`
- `statistics-gpu_jupyter_lab-q018`

### Check: multi-tool ground truth (manual review)

- Count: `13`
- `statistics-classification_machinelearning-q014`
- `statistics-classification_machinelearning-q018`
- `statistics-classification_regression-q011`
- `statistics-flexynesis_classification-q016`
- `statistics-flexynesis_classification-q017`
- `statistics-fruit_360-q011`
- `statistics-gpu_jupyter_lab-q012`
- `statistics-gpu_jupyter_lab-q015`
- `statistics-gpu_jupyter_lab-q016`
- `statistics-gpu_jupyter_lab-q017`
- `statistics-gpu_jupyter_lab-q018`
- `statistics-machinelearning-q011`
- `statistics-regression_machinelearning-q016`

## Ground truth: manual alternatives present

- Count: `13`

- `statistics-classification_machinelearning-q014`
  - tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0', 'toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
  - query: I'm working with a chemical dataset where you want to classify samples from molecular descriptors (QSAR-style). I want to train an SVM classifier and evaluate accuracy with a proper train/test split. Which tool in Galaxy can do this?
  - note: Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). If you restrict the compared models to SVM only, it can serve as an alternative way to train an SVM classifier on tabular data with reproducible splits via the random seed and (optionally) a sample ID column.
- `statistics-classification_machinelearning-q018`
  - tools: ['Remove beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3']
  - query: I want to drop the first few lines of a text/tabular file as a quick cleanup step before importing it into downstream tools. Which Galaxy tool should I use?
  - note: Manual: this step removes the first line (header) from a tabular file. A sed-based text transformation can delete the first line (e.g., '1d'), so it is a valid alternative to the dedicated 'Remove beginning' tool.
- `statistics-classification_regression-q011`
  - tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0', 'toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
  - query: I have a machine learning dataset where you want to train and evaluate a predictive model. I need a support vector machine classifier for my feature matrix and evaluation outputs. Also, I’d like the run to be reproducible (same results if I rerun it). What Galaxy tool should I run for this step?
  - note: Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). Restricting the compared models to SVM only provides an SVM-classifier training path comparable in intent to the dedicated SVM classifier tool for tabular inputs.
- `statistics-flexynesis_classification-q016`
  - tools: ['join1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_easyjoin_tool/9.5+galaxy3']
  - query: I have two tabular datasets that share a sample identifier column and I need to merge them into a single table for downstream analysis. Which Galaxy tool should I use?
  - note: Manual: both tools perform a key-based join of two tabular datasets into a single table. The text_processing EasyJoin variant is an acceptable alternative when you need more control over which columns are kept from each input.
- `statistics-flexynesis_classification-q017`
  - tools: ['Show beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_head_tool/9.5+galaxy3']
  - query: Before analysis, I want to quickly take the first N rows of a table to sanity-check formatting and sample IDs. Which Galaxy tool should I use?
  - note: Manual: both tools output the first N lines of a dataset for quick inspection (head/select-first). Either is appropriate for sanity-checking a table before analysis.
- `statistics-fruit_360-q011`
  - tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3', 'Cut1']
  - query: I have a tabular file with many columns and need to keep only a specific subset of columns to create a cleaner feature table for downstream machine learning. Which Galaxy tool should I use?
  - note: Manual: the tutorial uses Advanced Cut to keep a specific column from a tabular dataset. Galaxy's core Cut tool can also select a specific column (e.g., column 3), so it is an acceptable alternative.
- `statistics-gpu_jupyter_lab-q012`
  - tools: ['Filter1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_grep_tool/9.5+galaxy3']
  - query: I have a sample metadata table and want to drop all rows where a column contains a specific keyword (e.g., remove samples labeled as "control"). Which Galaxy tool should I use?
  - note: Manual: for dropping rows based on a keyword/category in a column, a grep-style filter (keeping or excluding matching lines) is also valid in addition to the generic column filter tool.
- `statistics-gpu_jupyter_lab-q015`
  - tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
  - query: I have a wide feature table and need to keep only an ID column plus a small set of feature columns to create a compact training matrix. Which Galaxy tool should I use?
  - note: Manual: selecting/reordering columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.
- `statistics-gpu_jupyter_lab-q016`
  - tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
  - query: I need to drop some columns from a tabular file and reorder the remaining columns to match the column order of another dataset. Which Galaxy tool should I use?
  - note: Manual: selecting/reordering columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.
- `statistics-gpu_jupyter_lab-q017`
  - tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
  - query: I have a tabular file where I only need a contiguous block of columns (e.g., columns 5–200) and I want to discard everything else. Which Galaxy tool should I use?
  - note: Manual: selecting a contiguous block of columns can be done with either Galaxy's core Cut tool or the text_processing Cut wrapper.
- `statistics-gpu_jupyter_lab-q018`
  - tools: ['Cut1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_cut_tool/9.5+galaxy3']
  - query: I have a table with metadata columns up front and many feature columns after that. I want to split out only the metadata columns (e.g., the first 4 columns) into a separate table. Which Galaxy tool should I use?
  - note: Manual: extracting the first few metadata columns is a column-selection task supported by both core Cut and text_processing Cut.
- `statistics-machinelearning-q011`
  - tools: ['toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_svm_classifier/sklearn_svm_classifier/1.0.11.0', 'toolshed.g2.bx.psu.edu/repos/goeckslab/tabular_learner/tabular_learner/0.1.4']
  - query: I have a numeric feature matrix where you want to discover groups (unsupervised clustering). I want to fit an SVM for classification and inspect performance metrics. Also, I want to inspect predicted vs true values to spot obvious issues. Is there a Galaxy tool that can handle this?
  - note: Manual: Tabular Learner supports classification and includes explicit SVM options (linear/radial kernels). When configured to compare only SVM models, it can train an SVM and report evaluation metrics, making it an acceptable alternative for SVM-focused classification on tabular data.
- `statistics-regression_machinelearning-q016`
  - tools: ['Remove beginning1', 'toolshed.g2.bx.psu.edu/repos/bgruening/text_processing/tp_sed_tool/9.5+galaxy3']
  - query: I have a text/tabular file where the first lines are metadata or a header block, and I need to remove them before analysis. Which Galaxy tool should I use?
  - note: Manual: this step removes the first line (header) from a tabular file. A sed-based text transformation can delete the first line (e.g., '1d'), so it is a valid alternative to the dedicated 'Remove beginning' tool.

## Ground-truth expansion (needs manual review)

This project’s expansion skill is intentionally conservative: **do not auto-expand** based on loose similarity.
Use IO details + help text to manually justify any alternative.

Sample items that look eligible for manual expansion review (single-tool gold, toolshed tool, tool_help_text present):

- `statistics-CNN-q011`
  - query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. My labels are a single column of class IDs, but the model expects one-hot targets. Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/sklearn_to_categorical/sklearn_to_categorical/1.0.11.0`
  - io: inputs=['boolean', 'data', 'integer'] outputs=[]
  - tool_help_text: present (len=581)
- `statistics-CNN-q012`
  - query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to specify the neural network architecture (layers/activations/input shape) in a config file. Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1452)
- `statistics-CNN-q013`
  - query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I already have a saved architecture/config and want to instantiate the actual model object. Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1261)
- `statistics-CNN-q014`
  - query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want to train a neural network and evaluate it (e.g., accuracy/loss on validation data). Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
  - io: inputs=['conditional', 'select'] outputs=[]
  - tool_help_text: present (len=2022)
- `statistics-CNN-q015`
  - query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I’ve trained a model and now want predictions for a new dataset (labels or probabilities). Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
  - io: inputs=['conditional', 'data', 'select'] outputs=[]
  - tool_help_text: present (len=413)
- `statistics-CNN-q016`
  - query: I'm working with a labeled image dataset (handwritten digits) for multi-class classification. I want a quick visualization summary of my ML experiment outputs for inspection. Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/ml_visualization_ex/ml_visualization_ex/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1463)
- `statistics-FNN-q011`
  - query: I have a tabular classification task with many numeric features. I want to define a Keras-style model using a configuration so I can reuse it across runs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1452)
- `statistics-FNN-q012`
  - query: I'm analyzing a tabular classification task with many numeric features. I want to create a trainable neural network from an architecture definition (without writing code). Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1261)
- `statistics-FNN-q013`
  - query: I have a tabular classification task with many numeric features. I need to run end-to-end training for a deep learning model and get evaluation metrics back. Also, I need to control epochs and batch size. What’s the right Galaxy tool for this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
  - io: inputs=['conditional', 'select'] outputs=[]
  - tool_help_text: present (len=2022)
- `statistics-FNN-q014`
  - query: I have a tabular classification task with many numeric features. After training, I need to apply the saved model to unseen samples to generate outputs. Also, I’d like a quick run on a small subset first. Is there a Galaxy tool that can handle this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
  - io: inputs=['conditional', 'data', 'select'] outputs=[]
  - tool_help_text: present (len=413)
- `statistics-FNN-q015`
  - query: I'm working with a tabular classification task with many numeric features. I want interactive plots to evaluate a regression model (predicted vs true, residuals). Which tool in Galaxy can do this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/plotly_regression_performance_plots/plotly_regression_performance_plots/0.1`
  - io: inputs=['data'] outputs=[]
  - tool_help_text: present (len=457)
- `statistics-RNN-q011`
  - query: I have a sequence/time-series dataset where order matters (e.g., for classification). I’m prototyping a model and need a step that prepares a written architecture specification for building. What Galaxy tool should I run for this step?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_config/keras_model_config/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1452)
- `statistics-RNN-q012`
  - query: In my project I’m using a sequence/time-series dataset where order matters (e.g., for classification). I’ve defined the network structure in a config; now I need the step that builds the runnable model. Also, I’d like the run to be reproducible (same results if I rerun it). What’s the right Galaxy tool for this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_model_builder/keras_model_builder/1.0.11.0`
  - io: inputs=['conditional'] outputs=[]
  - tool_help_text: present (len=1261)
- `statistics-RNN-q013`
  - query: I have a sequence/time-series dataset where order matters (e.g., for classification). I have training + validation splits and need the step that fits the model and reports performance. Also, I want early stopping if validation performance stops improving. Is there a Galaxy tool that can handle this?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/keras_train_and_eval/keras_train_and_eval/1.0.11.0`
  - io: inputs=['conditional', 'select'] outputs=[]
  - tool_help_text: present (len=2022)
- `statistics-RNN-q014`
  - query: I have a sequence/time-series dataset where order matters (e.g., for classification). I want to run inference using a previously trained model and export the predicted classes. Also, I want a simple table mapping each sample to its prediction. What Galaxy tool should I run for this step?
  - gold: `toolshed.g2.bx.psu.edu/repos/bgruening/model_prediction/model_prediction/1.0.11.0`
  - io: inputs=['conditional', 'data', 'select'] outputs=[]
  - tool_help_text: present (len=413)

