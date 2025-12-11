# GTN Benchmark Items (Readable)

## A short introduction to Galaxy (topics/introduction/tutorials/galaxy-intro-short)
- Topic: introduction
- Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72
- Datasets (1): mutant_R1.fastq

Questions:
- **galaxy-intro-short-q01** — I have paired-end FASTQ reads from a ChIP-seq experiment (mutant_R1.fastq), want to assess library quality before alignment. What should I do?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q02** — My single-cell FASTQ files (mutant_R1.fastq) show variable read quality; how can I clean them for downstream analysis?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q03** — Which Galaxy tool should I use to assess read quality for mutant_R1.fastq?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q04** — How can I get a quality report for my FASTQ file (mutant_R1.fastq) in Galaxy?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q05** — I have paired-end FASTQ reads from a ChIP-seq experiment (mutant_R1.fastq), want to trim adapters and low-quality bases. What should I do?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastq_quality_filter/cshl_fastq_quality_filter/1.0.1
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q06** — My FASTQ files (mutant_R1.fastq) have poor quality scores; how can I filter them to improve downstream analysis?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastq_quality_filter/cshl_fastq_quality_filter/1.0.1
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q07** — Which Galaxy tool should I use to filter low-quality reads from mutant_R1.fastq?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastq_quality_filter/cshl_fastq_quality_filter/1.0.1
  - Datasets: mutant_R1.fastq
- **galaxy-intro-short-q08** — How can I trim adapters and low-quality bases on mutant_R1.fastq in Galaxy?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastq_quality_filter/cshl_fastq_quality_filter/1.0.1
  - Datasets: mutant_R1.fastq

## Quality Control (topics/sequence-analysis/tutorials/quality-control)
- Topic: sequence-analysis
- Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72+galaxy1
- Datasets (12): GSM461176_untreat_single_subset.fastq, GSM461177_untreat_paired_chr4.bam, GSM461177_untreat_paired_subset_1.fastq, GSM461177_untreat_paired_subset_2.fastq, GSM461178_untreat_paired_subset_1.fastq, GSM461178_untreat_paired_subset_2.fastq, GSM461179_treat_single_subset.fastq, GSM461180_treat_paired_subset_1.fastq, GSM461180_treat_paired_subset_2.fastq, GSM461181_treat_paired_subset_1.fastq, GSM461181_treat_paired_subset_2.fastq, GSM461182_untreat_single_subset.fastq

Questions:
- **quality-control-q01** — I have paired-end FASTQ reads from a ChIP-seq experiment (GSM461177_untreat_paired_subset_1.fastq, GSM461177_untreat_paired_subset_2.fastq), want to assess library quality before alignment. What should I do?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72+galaxy1
  - Datasets: GSM461177_untreat_paired_subset_1.fastq, GSM461177_untreat_paired_subset_2.fastq
- **quality-control-q02** — My single-cell FASTQ files (GSM461176_untreat_single_subset.fastq) show variable read quality; how can I clean them for downstream analysis?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72+galaxy1
  - Datasets: GSM461176_untreat_single_subset.fastq
- **quality-control-q03** — We sequenced tumor samples (GSM461178_untreat_paired_subset_1.fastq, GSM461178_untreat_paired_subset_2.fastq); how do I check for adapter contamination and trim low-quality bases?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72+galaxy1
  - Datasets: GSM461178_untreat_paired_subset_1.fastq, GSM461178_untreat_paired_subset_2.fastq
- **quality-control-q04** — Which Galaxy tool should I use to assess read quality for GSM461176_untreat_single_subset.fastq?
  - Tools: toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.72+galaxy1
  - Datasets: GSM461176_untreat_single_subset.fastq
- **quality-control-q05** — How can I trim adapters and low-quality bases on GSM461177_untreat_paired_subset_1.fastq and GSM461177_untreat_paired_subset_2.fastq in Galaxy?
  - Tools: toolshed.g2.bx.psu.edu/repos/lparsons/cutadapt/cutadapt/1.16.3
  - Datasets: GSM461177_untreat_paired_subset_1.fastq, GSM461177_untreat_paired_subset_2.fastq
- **quality-control-q06** — I have single-end FASTQ reads from a RNA-seq experiment (GSM461179_treat_single_subset.fastq), want to assess library quality before alignment. What should I do?
  - Tools: toolshed.g2.bx.psu.edu/repos/lparsons/cutadapt/cutadapt/1.16.3
  - Datasets: GSM461179_treat_single_subset.fastq
- **quality-control-q07** — My FASTQ files (GSM461180_treat_paired_subset_1.fastq, GSM461180_treat_paired_subset_2.fastq) show variable read quality; how can I clean them for downstream analysis?
  - Tools: toolshed.g2.bx.psu.edu/repos/lparsons/cutadapt/cutadapt/1.16.3
  - Datasets: GSM461180_treat_paired_subset_1.fastq, GSM461180_treat_paired_subset_2.fastq
- **quality-control-q08** — We sequenced tumor samples (GSM461181_treat_paired_subset_1.fastq, GSM461181_treat_paired_subset_2.fastq); how do I check for adapter contamination and trim low-quality bases?
  - Tools: toolshed.g2.bx.psu.edu/repos/lparsons/cutadapt/cutadapt/1.16.3
  - Datasets: GSM461181_treat_paired_subset_1.fastq, GSM461181_treat_paired_subset_2.fastq
- **quality-control-q09** — Which Galaxy tool should I use to assess read quality for GSM461182_untreat_single_subset.fastq?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.9+galaxy1
  - Datasets: GSM461182_untreat_single_subset.fastq
- **quality-control-q10** — How can I trim adapters and low-quality bases on GSM461177_untreat_paired_subset_1.fastq and GSM461177_untreat_paired_subset_2.fastq in Galaxy?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.9+galaxy1
  - Datasets: GSM461177_untreat_paired_subset_1.fastq, GSM461177_untreat_paired_subset_2.fastq
- **quality-control-q11** — I have paired-end FASTQ reads from a ChIP-seq experiment (GSM461178_untreat_paired_subset_1.fastq, GSM461178_untreat_paired_subset_2.fastq), want to assess library quality before alignment. What should I do?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.9+galaxy1
  - Datasets: GSM461178_untreat_paired_subset_1.fastq, GSM461178_untreat_paired_subset_2.fastq
- **quality-control-q12** — Which Galaxy tool should I use to aggregate the FastQC reports of both forward and reverse reads?
  - Tools: toolshed.g2.bx.psu.edu/repos/iuc/multiqc/multiqc/1.9+galaxy1
  - Datasets: GSM461176_untreat_single_subset.fastq, GSM461177_untreat_paired_chr4.bam, GSM461177_untreat_paired_subset_1.fastq, GSM461177_untreat_paired_subset_2.fastq

## Building the LORIS LLR6 PanCancer Model Using PyCaret (topics/statistics/tutorials/loris_model)
- Topic: statistics
- Tools: toolshed.g2.bx.psu.edu/repos/paulo_lyra_jr/pycaret_model_comparison/PyCaret_Model_Comparison/2024.3.3.2+0
- Datasets (2): Chowell_test_Response.tsv, Chowell_train_Response.tsv

Questions:
- **loris_model-q01** — I have a dataset of patients treated with immune checkpoint blockade (ICB) and non-ICB-treated patients across 18 solid tumor types, and I want to develop a model to accurately predict patient responses to the treatment. What type of machine learning model should I use?
  - Tools: toolshed.g2.bx.psu.edu/repos/paulo_lyra_jr/pycaret_model_comparison/PyCaret_Model_Comparison/2024.3.3.2+0
  - Datasets: Chowell_train_Response.tsv, Chowell_test_Response.tsv
- **loris_model-q02** — My goal is to build a model that can predict patient outcomes when ICB is chosen as the treatment, using a comprehensive dataset of patients. What are the key features that I should focus on?
  - Tools: toolshed.g2.bx.psu.edu/repos/paulo_lyra_jr/pycaret_model_comparison/PyCaret_Model_Comparison/2024.3.3.2+0
  - Datasets: Chowell_train_Response.tsv, Chowell_test_Response.tsv
- **loris_model-q03** — Which Galaxy tool should I use to compare the performance of different machine learning models for classification tasks, such as building a model to predict patient responses to ICB treatment?
  - Tools: toolshed.g2.bx.psu.edu/repos/paulo_lyra_jr/pycaret_model_comparison/PyCaret_Model_Comparison/2024.3.3.2+0
  - Datasets: Chowell_train_Response.tsv, Chowell_test_Response.tsv
- **loris_model-q04** — How can I use Galaxy to train a machine learning model to predict patient outcomes for ICB treatment, using a dataset with features such as TMB, Systemic Therapy History, Albumin, Cancer Type, NLR, Age, and Response?
  - Tools: toolshed.g2.bx.psu.edu/repos/paulo_lyra_jr/pycaret_model_comparison/PyCaret_Model_Comparison/2024.3.3.2+0
  - Datasets: Chowell_train_Response.tsv, Chowell_test_Response.tsv
