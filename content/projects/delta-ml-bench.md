Title: DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories
Slug: deltamlbench-can-ai-agents-improve-on-published-ml-research
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A 48-task benchmark for evaluating autonomous ML experimentation in real research repositories.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/deltaml-bench-public
Paper: /papers/deltaml-bench.pdf
Featured: true

Our earlier [ML Research Benchmark](https://arxiv.org/abs/2410.22553) evaluated whether AI agents could follow complex ML research instructions and iterate beyond initial baselines. DeltaML-Bench asks a related question under more realistic repository conditions: what happens when agents are given existing research code and asked to improve a published result?

DeltaML-Bench is a benchmark of 48 tasks drawn from real Papers With Code repositories where the goal is not reproduction but **measurable improvement over published baselines**. We evaluated Claude Sonnet 4 and GPT-5 across two agent scaffoldings. The results show that agents can improve published baselines in some runs, while performance varies substantially with the model, scaffolding, task, and compute allocation.

## Setup: Real Repos, Real Papers, Real Baselines

Each task in DeltaML-Bench pairs a peer-reviewed paper with its open-source repository, dataset, and the evaluation metric reported in the publication. Agents receive the PDF, the code, and the data. Their objective: improve the reported metric.

This is deliberately harder than prior benchmarks in several ways. There is no clean starter template; agents must navigate heterogeneous codebases with varying framework choices, documentation quality, and dependency structures. The tasks span computer vision, NLP, graph learning, time series forecasting, molecular property prediction, anomaly detection, and other domains. The evaluation metric is percentage improvement over the published baseline, not a binary pass/fail.

We curated tasks from Papers With Code, filtering for post-January 2024 publications with accessible repositories and datasets, training runtimes under 10 hours on a single GPU, and confirmed end-to-end reproducibility. Starting from approximately 380 candidates, human verification narrowed the pool to 67 reproducible tasks, from which we selected 48 for domain diversity.

## Two Agent Architectures

We tested two scaffolding approaches:

**The Modular Agent** (from METR's poking-agents) separates concerns across five modules: prompting, generation, discrimination, action execution, and tooling, coordinated through shared state. It is clean and debuggable.

**The ARG Agent** (ours) takes a more aggressive approach with solution tree exploration, beam search across multiple solution paths, configurable search policies, and self-reflection mechanisms for analyzing execution failures. Different configuration packs optimize for speed, reasoning depth, or comprehensive exploration.

Both run on the Vivaria platform in isolated Docker containers with a single H100 80GB GPU. We tested two equal-compute allocations: four attempts of up to six hours each and two attempts of up to twelve hours each, with a 100-million-token limit per run.

## Specification Gaming

The evaluation also surfaced specification gaming, making integrity checks an important part of the benchmark.

When agents fail to make legitimate progress on a task, some produce invalid results rather than reporting failure. Observed behaviors include hardcoding metric values in return statements, writing stub implementations, and fabricating results without actually training models. Across the aggregate configurations, the highest observed specification-gaming rate was 47.9% for the Modular scaffolding with Claude Sonnet 4.

We built a multi-layered defense system to detect these behaviors: static AST analysis to detect hardcoded values, training artifact verification to confirm real checkpoints exist, LLM-based semantic analysis of solution code, and a forensic log grading system where an ensemble of three frontier models audits the complete execution trace. A majority vote determines whether a submission passes integrity checks.

No specification gaming was detected in the evaluated ARG configurations, while it was observed in several Modular configurations, particularly with Claude Sonnet 4. This result is specific to the evaluated tasks, models, and auditing procedure; it should not be interpreted as a general guarantee that a scaffolding prevents gaming.

## Results

Looking at the detailed task-level results, several patterns emerge.

**GPT-5 benefited most consistently from ARG scaffolding.** In the 4×6h allocation, its per-run success rate increased from 9.4% with Modular to 33.9% with ARG. Under the 2×12h allocation, GPT-5 ARG reached a 49.0% per-run success rate. Because the latter allocation has fewer attempts, its observed task coverage was lower despite its higher single-run success rate.

**Claude Sonnet 4 showed a more mixed scaffolding effect.** ARG increased its 4×6h per-run success rate from 24.5% to 30.2%, but in the 2×12h allocation Claude ARG reached 19.8% compared with 22.9% for Modular. These results caution against treating one scaffolding as uniformly better across models and allocations.

**Some tasks resisted all evaluated configurations.** CIFAR-10 with ABNet, CIFAR-10 with ResNet18-FSGDM, CIFAR-100 with ProDSC, Kvasir-SEG EMCAD, electricity forecasting with CycleNet, MalNet-Tiny with GatedGCN, and ZINC NeuralWalker all saw 0% success across the evaluated model-scaffolding combinations. The aggregate results do not distinguish whether this reflects strong baselines, repository obstacles, task-specific difficulty, or another cause.

**Longer time horizons helped, but not uniformly.** Moving from 4×6h to 2×12h improved GPT-5+ARG on tasks like ETTh1 forecasting (from 75% to 100% success rate) and several MNIST/Fashion-MNIST variants. For some tasks, however, more time simply meant more opportunities to pursue unproductive paths.

## Resource Usage

The token and time usage data reveals clear differences in agent efficiency.

Claude Sonnet 4 with Modular used the fewest tokens on average, while GPT-5 configurations used more. Runtime and token totals alone cannot distinguish efficient solution finding from early termination, invalid work, or unproductive exploration, so these measurements should be read alongside success and integrity outcomes.

Resource usage also varied across allocations: GPT-5 ARG used more tokens in the 2×12h setting and achieved a higher per-run success rate, whereas Claude ARG used fewer tokens and had a lower success rate. These aggregate associations do not establish that additional tokens caused the performance differences.

## Discussion

DeltaML-Bench extends our original ML Research Benchmark from instruction-following tasks to experimentation in existing research repositories. In the evaluated sample, some agent runs produced verified percentage improvements over published baselines, though the results were uneven.

Several key observations merit emphasis:

**Scaffolding design is an important part of agent capability.** The same underlying model produces different outcomes depending on the scaffolding. ARG's structured exploration was associated with large gains for GPT-5, while the effects for Claude Sonnet 4 were more mixed.

**Specification gaming is a first-order concern for autonomous experimentation.** Reliable evaluation requires artifact verification, audit logs, restricted evaluation interfaces, and human review for consequential experiments. The observed events do not establish that models generally default to fabrication when stuck.

**Several tasks remained unsolved in the evaluated runs.** Determining whether these tasks require deeper architectural changes, domain-specific insight, or simply different search and compute allocations will require controlled follow-up experiments.

**Current agents can perform useful but uneven ML experimentation.** They can set up environments, debug dependency issues, run experiments, and iterate on candidate improvements, but benchmark performance remains inconsistent across tasks and configurations.

## Future Work

DeltaML-Bench is released as a static benchmark with 48 tasks and standardized evaluation protocols. As agent capabilities evolve, we plan to expand the task set, increase difficulty, and develop more sophisticated integrity verification. Its percentage-improvement metric allows future systems to be compared against published baselines without reducing every task to a binary outcome.

The code and benchmark are available for the research community to evaluate their own agents. The combination of authentic research conditions, improvement-oriented evaluation, and multi-layer integrity checks makes DeltaML-Bench a testbed for measuring progress in autonomous ML experimentation.
