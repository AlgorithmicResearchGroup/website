Title: Neural Architecture Search
Slug: opensource-neural-architecture-search
Save_as: opensource/neural-architecture-search.html
Artifact_group: Code & Benchmarks
Artifact_order: 040
Summary: A Tiny Recursive Model that predicts NAS-Bench-201 architecture performance and guides architecture search. Includes dataset builders, training and evaluation scripts, search comparisons, and a small CPU demo.
Template: resource
Url: opensource/neural-architecture-search.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 040

- [AlgorithmicResearchGroup/nas-public](https://github.com/AlgorithmicResearchGroup/nas-public)

<!-- resource-details -->

Training every candidate architecture is an expensive way to search. This project explores a different route: learn to predict architecture performance, then use that predictor to decide which candidates deserve attention.

The implementation trains a **Tiny Recursive Model (TRM)** on **NAS-Bench-201** and uses its predictions during architecture search. The public repository connects dataset preparation, predictor training, evaluation, and search, so each stage can be inspected or changed independently.

## From architecture data to guided search

The full workflow builds a dataset from the NAS-Bench-201 benchmark file, trains a predictor, and evaluates its outputs against benchmark targets. The default dataset is CIFAR-10, with configuration for alternatives such as CIFAR-100. Training supports a single device or a multi-GPU run.

Evaluation produces saved predictions and a predictions-versus-targets plot. The search workflow then uses a trained checkpoint and the real benchmark data to guide candidate selection, writing search results and comparison plots. Controls for initial candidates, search iterations, and candidate selection allow the search budget to be varied explicitly.

## A small, complete starting point

The repository includes a CPU demo that builds a tiny synthetic dataset, trains a small checkpoint, and evaluates it. It runs without the roughly 4.7 GB NAS-Bench-201 file, making it a useful first check of the installation and artifact flow.

The synthetic demo is an installation exercise. Benchmark-backed training and search require the actual NAS-Bench-201 data; the README provides the download location and expected file path. GPU training is the practical route for full experiments, while CPU execution is intended mainly for the demo and debugging.

## What to explore

The code provides a starting point for comparing predictor quality with search quality: does a model that predicts performance more accurately also find useful architectures earlier? Training data, checkpoint choice, and search budget can be varied through the supplied scripts.

NAS-Bench-201 supplies the benchmark observations, and this repository adds the recursive predictor and search workflow. [The accompanying research article]({filename}/projects/nas.md) discusses the experiments and reported results; [the repository README](https://github.com/AlgorithmicResearchGroup/nas-public#readme) documents how to run the public implementation.
