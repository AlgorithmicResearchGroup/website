Title: ArXivDLInstruct: 778K Research Code Functions for Instruction Tuning
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A dataset of 778,152 functions extracted from arXiv-linked research code, each paired with instruction prompts, for training ML-specialized code generation models.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/ArXivDLInstruct
Featured: true

# ArXivDLInstruct: 778K Research Code Functions for Instruction Tuning

High-quality, deep learning-specific datasets for training language models on code generation remain scarce. General code datasets like The Stack are massive but dilute: most functions have no relationship to ML research. Training a model that can write PyTorch training loops, implement custom loss functions, or build neural network architectures requires data concentrated in that domain.

ArXivDLInstruct addresses this gap: **778,152 functions extracted from research code published on arXiv**, each paired with a detailed instruction prompt and a short description. The full dataset is 2.26 GB of prompt-response pairs, released under an MIT license on [HuggingFace](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct).

## Dataset Contents

Each entry contains:

- **prompt**: a detailed instruction for generating the function
- **description**: a short summary of what the function does
- **function**: the actual source code
- **function_name**: the name of the function or class
- **function_summary**: a 2-3 sentence explanation
- **repo**: the source repository name
- **file**: the file path within the repository

The functions range from simple utilities (version parsing, config loading) to complex neural network modules (policy networks with recurrent layers, custom distribution classes, multi-layer perceptrons with configurable initialization). All code comes from real research repositories associated with published papers.

## Construction Pipeline

The dataset was created through a multi-step pipeline:

1. **Parse GitHub links from arXiv papers.** We extracted all repository URLs referenced in arXiv publications.
2. **Download and parse repositories.** Each repository was cloned and parsed into individual functions and classes.
3. **Filter for ML/DL library usage.** We retained only functions that use machine learning and deep learning libraries (PyTorch, TensorFlow, and related tools).
4. **Generate instruction prompts.** Using GPT-4o-mini, we generated detailed prompts based on the ground truth code, creating natural instruction-response pairs suitable for fine-tuning.

This pipeline ensures that every function in the dataset is grounded in real research code rather than synthetic examples, and that the instruction prompts accurately describe what the code does.

## Use Cases

ArXivDLInstruct supports several applications:

**Instruction tuning.** Fine-tune language models to follow natural language instructions for writing research-grade ML code. The prompt-response format maps directly to the instruction tuning paradigm.

**Retrieval-Augmented Generation.** Use the dataset as a retrieval corpus for RAG systems that assist researchers in writing code. The function summaries and descriptions provide natural language anchors for semantic search.

**Code completion.** Train or evaluate code completion models on research-specific code patterns: architectures, training loops, data processing pipelines, and evaluation scripts.

**R&D coding agents.** Build agents that can write and modify ML research code by training on the patterns and conventions found in published research repositories.

## Availability

The dataset is available now:

- **Full dataset:** [huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct)
- **Intermediate pipeline datasets:** [huggingface.co/AlgorithmicResearchGroup](https://huggingface.co/AlgorithmicResearchGroup)

For researchers working on code generation, research agents, or ML-specific language models, ArXivDLInstruct provides a concentrated, high-quality training signal that general code datasets cannot match.
