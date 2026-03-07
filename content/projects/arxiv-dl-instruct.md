Title: ArXivDLInstruct: 778K Research Code Functions for Instruction Tuning
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A benchmark suite for evaluating AI agents on real machine learning research tasks — including task definitions, a baseline agent, and evaluation infrastructure.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/ArXivDLInstruct
Featured: true

# Introducing ArXivDLInstruct: 778K Research Code Functions for Instruction Tuning

There's a scarcity of high-quality, deep learning-specific datasets for training language models on code generation. General code datasets like The Stack are massive but dilute — most functions have nothing to do with ML research. If you want a model that can write PyTorch training loops, implement custom loss functions, or build neural network architectures, you need data that's concentrated in that domain.

ArXivDLInstruct is our answer: **778,152 functions extracted from research code published on arXiv**, each paired with a detailed instruction prompt and a short description. The full dataset is 2.26 GB of prompt-response pairs, released under an MIT license on [HuggingFace](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct).

## What's in the Dataset

Each entry contains:

- **prompt** — a detailed instruction for generating the function
- **description** — a short summary of what the function does
- **function** — the actual source code
- **function_name** — the name of the function or class
- **function_summary** — a 2-3 sentence explanation
- **repo** — the source repository name
- **file** — the file path within the repository

The functions range from simple utilities (version parsing, config loading) to complex neural network modules (policy networks with recurrent layers, custom distribution classes, multi-layer perceptrons with configurable initialization). The code comes from real research repositories — the kind of code that actually gets used in published papers.

## How We Built It

The dataset was created through a multi-step pipeline:

1. **Parse GitHub links from arXiv papers.** We extracted all repository URLs referenced in arXiv publications.
2. **Download and parse repositories.** Each repository was cloned and parsed into individual functions and classes.
3. **Filter for ML/DL library usage.** We kept only functions that use machine learning and deep learning libraries — PyTorch, TensorFlow, and related tools.
4. **Generate instruction prompts.** Using GPT-4o-mini, we generated detailed prompts based on the ground truth code, creating natural instruction-response pairs suitable for fine-tuning.

This pipeline ensures that every function in the dataset is grounded in real research code rather than synthetic examples, and that the instruction prompts accurately describe what the code does.

## Use Cases

ArXivDLInstruct is designed for several applications:

**Instruction tuning.** Fine-tune language models to follow natural language instructions for writing research-grade ML code. The prompt-response format maps directly to the instruction tuning paradigm.

**Retrieval-Augmented Generation.** Use the dataset as a retrieval corpus for RAG systems that help researchers write code. The function summaries and descriptions provide natural language anchors for semantic search.

**Code completion.** Train or evaluate code completion models on research-specific code patterns — architectures, training loops, data processing pipelines, and evaluation scripts.

**R&D coding agents.** Build agents that can write and modify ML research code by training on the patterns and conventions found in published research repositories.

## Get the Data

The dataset is available now:

- **Full dataset:** [huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct)
- **Intermediate pipeline datasets:** [huggingface.co/AlgorithmicResearchGroup](https://huggingface.co/AlgorithmicResearchGroup)

We're excited to see what the community builds with this. If you're working on code generation, research agents, or ML-specific language models, ArXivDLInstruct gives you a concentrated, high-quality training signal that general code datasets can't match.