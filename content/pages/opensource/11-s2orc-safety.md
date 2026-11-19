Title: S2ORC Safety Dataset
Slug: opensource-s2orc-safety-dataset
Save_as: opensource/s2orc-safety-dataset.html
Artifact_group: Datasets
Artifact_order: 60
Summary: 16,806 safety-relevant papers selected from S2ORC, with structured threat models, evaluation details, reproduction steps, and links to research code.
Template: resource
Url: opensource/s2orc-safety-dataset.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 060

- [AlgorithmicResearchGroup/S2ORC-Safety](https://huggingface.co/datasets/AlgorithmicResearchGroup/s2orc-safety)

<!-- resource-details -->

## A map of safety-relevant research

S2ORC Safety collects **16,806 papers** from an S2ORC computer science corpus, preserving the upstream paper content while adding information about safety questions, experiments, and reproduction requirements. It builds on Allen AI’s [Semantic Scholar Open Research Corpus](https://github.com/allenai/s2orc), which includes research beyond arXiv.

The scope is deliberately broad. The [release’s metadata summary](https://huggingface.co/datasets/AlgorithmicResearchGroup/s2orc-safety/blob/main/paper_metadata_summary_normalized.json) includes adversarial robustness, model security, harmful-content evaluation, fairness, privacy attacks, alignment, interpretability, and agent safety. A paper can carry more than one label.

## How the collection was assembled

The documented pipeline begins with local embeddings and clustering. GPT-5.4 mini assists with cluster screening and individual paper labeling, followed by another labeling pass over suspicious exclusions. Structured metadata is extracted for accepted papers. The final release removes 304 rows that lacked both a parsed title and an abstract. The [dataset card](https://huggingface.co/datasets/AlgorithmicResearchGroup/s2orc-safety#s2orc-safety) describes that selection process.

The main `train` split contains **95 columns in 17 Parquet shards**, totaling approximately **736.6 MB**. Alongside titles, abstracts, paper text, authors, and references, it includes threat models, attack or defense categories, target systems, harm types, benchmarks, baselines, metrics, and reported results. Reproduction fields capture setup requirements, procedural steps, training or evaluation recipes, artifact availability, and compute requirements.

Separate files provide metadata-only records and a paper-to-code join table. Normalized GitHub links and mirror-path fields help connect papers to their implementations, while artifact-availability fields support checking what is accessible for a replication attempt.

## From discovery to a replication shortlist

The fields could support literature triage by threat model, comparisons of evaluation practices, or a shortlist of experiments with accessible code and stated setup requirements. Those applications still need the original papers: selection and extraction are LLM-assisted annotations, rather than verified judgments about every result or a complete census of AI safety.

Many structured fields are JSON serialized into strings. Missing lists use empty JSON arrays, while missing categorical values use `None specified`. Name normalization merges obvious spelling variants but does not resolve every synonymous model, dataset, or metric. The [live schema](https://datasets-server.huggingface.co/info?dataset=AlgorithmicResearchGroup%2Fs2orc-safety) is useful when preparing a loader.
