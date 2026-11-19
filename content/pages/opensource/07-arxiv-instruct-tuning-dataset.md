Title: ArXiv Instruct Tuning Dataset
Slug: opensource-arxiv-instruct-tuning
Save_as: opensource/arxiv-instruct-tuning.html
Artifact_group: Datasets
Artifact_order: 070
Summary: Three question-and-answer instruction-tuning releases—mathematics, computer science and machine learning, and physics—with 130,782 examples in a shared two-field format.
Template: resource
Url: opensource/arxiv-instruct-tuning.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 070

- [AlgorithmicResearchGroup/arxiv-math-instruct-50k](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-math-instruct-50k)
- [AlgorithmicResearchGroup/arxiv-cs-ml-instruct-tune-50k](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-cs-ml-instruct-tune-50k)
- [AlgorithmicResearchGroup/arxiv-physics-instruct-tune-30k](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-physics-instruct-tune-30k)

<!-- resource-details -->

## Three releases, one simple format

The ArXiv instruction-tuning collection provides **130,782 question-and-answer examples** across three separately downloadable releases. Their names identify mathematics, computer science and machine learning, and physics. All three use the same two text fields, `question` and `answer`, keeping the training format consistent across the collection.

The published counts are **50,488 examples** in the [mathematics release](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-math-instruct-50k), **50,063** in the [computer science and machine learning release](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-cs-ml-instruct-tune-50k), and **30,231** in the [physics release](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-physics-instruct-tune-30k).

## What you download

Each repository contains one Parquet shard and exposes a single `train` split through Hugging Face Datasets. Downloads are approximately 18.7 MB for mathematics, 20.0 MB for computer science and machine learning, and 11.1 MB for physics, according to the release metadata.

The shared schema makes the files straightforward to inspect, concatenate, or keep separate for training experiments. A question can become the input and its answer the target completion, with any chat or instruction formatting applied by the training pipeline. The released records do not include paper identifiers, source abstracts, subject annotations, or generation metadata alongside those two fields.

## Preparing a training experiment

The common format makes this a small, accessible collection for testing data loading, instruction formatting, and mixtures of scientific question-and-answer examples. Keep the release identifier alongside each row when combining the files, so the contribution of each source remains visible.

The cards do not document collection, answer generation, filtering, or human review, and there are no supplied validation or test splits. Inspect answer quality and subject coverage before choosing a training subset, and define a separate held-out evaluation for any fine-tuning comparison.
