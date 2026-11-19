Title: ML Research Benchmark
Slug: opensource-ml-research-benchmark
Save_as: opensource/ml-research-benchmark.html
Artifact_group: Code & Benchmarks
Artifact_order: 010
Summary: Seven competition-level machine learning tasks for evaluating research agents, spanning efficient training, limited-data pretraining, model merging, compression, and mathematical reasoning. Includes a tool-using baseline agent and a separate model evaluator.
Template: resource
Url: opensource/ml-research-benchmark.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 010

- [Baseline agent — mlrb-agent-public](https://github.com/AlgorithmicResearchGroup/mlrb-agent-public)
- [Model evaluator — mlrb-evals-public](https://github.com/AlgorithmicResearchGroup/mlrb-evals-public)
- [ML Research Benchmark paper](https://arxiv.org/abs/2410.22553)

<!-- resource-details -->

ML Research Benchmark puts an agent inside the work of machine learning research: writing code, training models, testing ideas, and producing an artifact that can be evaluated. The question is how far an agent can take an experiment once it has tools and a concrete research objective.

Introduced by Matthew Kenney in the [ML Research Benchmark paper](https://arxiv.org/abs/2410.22553), the suite draws seven competition-level tasks from machine learning conference tracks. It gives researchers a way to compare the model, tools, and workflow that make up an agent against the same practical challenges.

## Seven kinds of research work

The baseline supports **LLM efficiency, BabyLM, MiniPile, model merging, edge model compression, edge model training, and mathematical reasoning**. Together these cover building models with constrained resources, adapting existing models, and generating formal mathematical artifacts. Several tasks also have smaller variants for development runs.

This range matters: an agent that can assemble a training script still has to choose useful experiments, interpret feedback, and improve its solution. The original paper found that the tested agents could produce baseline results but struggled with non-trivial research iteration.

## An agent and an evaluator

The [baseline agent](https://github.com/AlgorithmicResearchGroup/mlrb-agent-public) includes tools for shell and Python execution, code editing, GitHub access, academic-paper search through Semantic Scholar, experiment notes, and memory. It supports OpenAI and Anthropic providers and can run in Docker.

The separate [Agent-Eval package](https://github.com/AlgorithmicResearchGroup/mlrb-evals-public) evaluates the resulting models. Depending on the task preset, it combines native measurements such as parameter count, latency, throughput, and perplexity with tasks from `lm-eval-harness`. Its mathematical reasoning workflow can generate Lean files and check them with an installed Lean toolchain.

## Start with a bounded run

Use the agent repository to explore or extend the research workflow, and the evaluator to measure a local model or a Hugging Face checkpoint. Agent-Eval defaults to quickstart-sized workloads; `--full_eval` selects the full workload. Record that setting alongside model and compute choices when comparing runs.

For the experimental context and original results, [read the studio research article]({filename}/projects/ml-research-benchmark.md).
