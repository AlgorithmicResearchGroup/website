Title: ARIA Benchmark
Slug: opensource-aria-benchmark
Save_as: opensource/aria-benchmark.html
Artifact_group: Code & Benchmarks
Artifact_order: 020
Summary: A toolkit for generating AI research knowledge benchmarks from Papers with Code exports and evaluating them with Inspect AI. Nine task builders cover papers, methods, datasets, research areas, and evaluation metrics.
Template: resource
Url: opensource/aria-benchmark.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 020

- [AlgorithmicResearchGroup/aria-public](https://github.com/AlgorithmicResearchGroup/aria-public)

<!-- resource-details -->

ARIA turns structured research metadata into questions about the machine learning landscape. Can a model identify a dataset's modality, describe a method, name the metrics used for a task, or recognize a model that does not belong in a group? These are concrete pieces of knowledge a research assistant needs before it can make useful experimental decisions.

The public toolkit connects two stages: generating benchmark datasets from **Papers with Code exports**, then evaluating model responses with **Inspect AI**. The source export remains visible, so a benchmark can be regenerated from a particular snapshot of the research record.

## What the toolkit covers

The current [benchmark generator](https://github.com/AlgorithmicResearchGroup/aria-public/blob/master/benchmark_generation/generate_benchmarks.py) provides nine builders: metric identification, paper abstracts, model descriptions, research-area classification, odd-model-out selection, similar models, top models, dataset descriptions, and dataset modalities.

These builders use four kinds of input: evaluation tables, papers with abstracts, methods, and datasets. They produce JSONL records containing the model input and a reference answer. You can generate the whole collection or select only the tasks relevant to an experiment. Builders without the required input data are skipped.

## How evaluation works

Inspect task definitions load the generated files locally, with optional Hugging Face loading for published datasets. Dataset-modality and odd-model-out tasks use exact-match scoring. Other tasks use model grading; for example, the metrics task compares factual content and allows partial credit. The README documents how to choose the evaluated model and the grader.

That distinction belongs in any result: an exact-match score and a model-graded answer reflect different evaluation procedures. Similarly, an answer is judged against the supplied export, so rankings and research metadata reflect that snapshot.

## Try the full workflow locally

The repository includes a tiny sample export and a mock-model workflow that exercises generation and evaluation without API keys. Start there to inspect the records and task definitions, then supply a research export and provider-backed models for a scored experiment.

[The original ARIA study]({filename}/projects/aria-benchmark.md) describes the research motivation and earlier evaluation. The repository documents the current, expanded toolkit.
