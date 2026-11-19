Title: AI SFT Dataset
Slug: opensource-ai-sft-dataset
Save_as: opensource/ai-sft-dataset.html
Artifact_group: Datasets
Artifact_order: 121
Summary: 2,729,918 supervised examples across 12 research tasks, combining code generation, code summaries, paper extraction, scientific questions, and review analysis.
Template: resource
Url: opensource/ai-sft-dataset.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 121

- [AlgorithmicResearchGroup/ai-sft](https://huggingface.co/datasets/AlgorithmicResearchGroup/ai-sft)

<!-- resource-details -->

## A shared format for research tasks

AI SFT brings **2,729,918 supervised examples** from 13 public ARG source collections into a common instruction-and-target schema. The release contains **2,593,122 training records** and **136,796 validation records**. Its [build statistics](https://huggingface.co/datasets/AlgorithmicResearchGroup/ai-sft/blob/main/stats.json) also record 199,678 rejected examples, which are published separately with rejection reasons and source payloads.

This is a mixture of research tasks, rather than a single question-answer dataset. The largest groups are paper structure extraction (983,157 examples), research code generation (778,152), and code summarization (777,655). Other families cover paper critique, review structuring, metric lookup, model and dataset descriptions, grounded paper questions, issue triage, repository feasibility, and identifying an odd model out.

The sources include ArXivDLInstruct, research-code function summaries, S2ORC CS Enriched, OpenReview-derived collections, and ARG benchmark datasets. That provenance connects the mixture back to the papers, code, and research tasks from which its examples were constructed.

## What travels with each example

The [canonical schema](https://huggingface.co/datasets/AlgorithmicResearchGroup/ai-sft#canonical-fields) includes an identifier, task family, instruction, optional context and answer choices, target, and target format. It also retains a grounding flag, source dataset, source keys, and a loss weight. The full export adds split labels, root identifiers, rendered inputs, and quality flags.

These fields give a training pipeline room to handle different output types—such as Python and text—and to select examples by task or source. The repository also publishes a [mixture recipe](https://huggingface.co/datasets/AlgorithmicResearchGroup/ai-sft/blob/main/mixture_recipe.yaml) with task-family weights.

## Choose the export you need

`train.parquet` is approximately **9.83 GB**, and `val.parquet` is about **534 MB**. The repository’s roughly 34.3 GB total also includes full, canonical, and rejected exports; it is not the size of the training split alone. The [file listing](https://huggingface.co/datasets/AlgorithmicResearchGroup/ai-sft/tree/main) distinguishes these downloads.

The collection is intended for supervised fine-tuning experiments involving research code and scientific information. Source identifiers and mixture weights let you select a task family, rebalance the blend, or study the contribution of a particular source. Because some inputs come from benchmark collections, check source overlap when designing an independent evaluation; the published validation split supports development within this mixture.
