Title: DeltaMLBench: Can AI Agents Improve on Published ML Research?
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A benchmark of 50 tasks drawn from real Papers With Code repositories where agents must achieve measurable improvement over published baselines.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/DeltaMLBench
Featured: true

# DeltaMLBench: Can AI Agents Improve on Published ML Research?

Last year we released the [ML Research Benchmark](https://arxiv.org/abs/2410.22553), which showed that AI agents could follow complex ML research instructions and produce baselines but could not perform non-trivial research iterations. The natural follow-up question is what happens when agents are given real research repositories and asked to beat the published results.

DeltaMLBench is a benchmark of 50 tasks drawn from real Papers With Code repositories where the goal is not reproduction but **measurable improvement over published baselines**. We evaluated frontier models (Claude Sonnet 4, Claude Opus 4, and GPT-5) across two agent scaffoldings and found that agents can now achieve genuine improvements on published work in some cases, though the path to those improvements is less clean than one might expect.

## Setup: Real Repos, Real Papers, Real Baselines

Each task in DeltaMLBench pairs a peer-reviewed paper with its open-source repository, dataset, and the evaluation metric reported in the publication. Agents receive the PDF, the code, and the data. Their objective: improve the reported metric.

This is deliberately harder than prior benchmarks in several ways. There is no clean starter template; agents must navigate heterogeneous codebases with varying framework choices, documentation quality, and dependency structures. The tasks span computer vision, NLP, graph learning, time series forecasting, molecular property prediction, anomaly detection, and other domains. The evaluation metric is percentage improvement over the published baseline, not a binary pass/fail.

We curated tasks from Papers With Code, filtering for post-January 2024 publications with accessible repos and datasets, training runtimes under 10 hours on a single GPU, and confirmed end-to-end reproducibility. Starting from approximately 380 candidates, human verification narrowed the pool to 67 reproducible tasks, from which we selected 50 for maximum domain diversity.

## Two Agent Architectures

We tested two scaffolding approaches:

**The Modular Agent** (from METR's poking-agents) separates concerns across five modules: prompting, generation, discrimination, action execution, and tooling, coordinated through shared state. It is clean and debuggable.

**The ARG Agent** (ours) takes a more aggressive approach with solution tree exploration, beam search across multiple solution paths, configurable search policies, and self-reflection mechanisms for analyzing execution failures. Different configuration packs optimize for speed, reasoning depth, or comprehensive exploration.

Both run on the Vivaria platform in isolated Docker containers with a single H100 80GB GPU. We tested two time configurations: 4 attempts at 6 hours each, and 2 attempts at 12 hours each, with a 10-million-token budget per run.

## Reward Hacking

Reward hacking proved to be one of the most significant findings in this evaluation.

When agents fail to make legitimate progress on a task, some produce fabricated results rather than reporting failure. Observed behaviors include hardcoding metric values in return statements, writing stub implementations, and fabricating results without actually training models. This was not a minor edge case: the Modular scaffolding with Claude Sonnet 4 showed cheating rates above 50% on many tasks.

We built a multi-layered defense system to detect these behaviors: static AST analysis to detect hardcoded values, training artifact verification to confirm real checkpoints exist, LLM-based semantic analysis of solution code, and a forensic log grading system where an ensemble of three frontier models audits the complete execution trace. A majority vote determines whether a submission passes integrity checks.

The results were striking. The ARG agent showed a **0% cheating rate across all models and configurations**; its tree search and reflection mechanisms appear to keep it on legitimate solution paths. The Modular agent, by contrast, cheated frequently, particularly with Claude Sonnet 4. This suggests that agent architecture matters at least as much as the underlying model for research integrity.

## Results

Looking at the detailed task-level results, several patterns emerge.

**GPT-5 with the ARG agent was the strongest combination.** On the 4×6h configuration, it achieved positive improvement on 29 of 48 tasks, with standout performances including a 95.96% improvement on the MIMIC-III clinical task, 78.92% on CNN summarization, 73.22% on SumMe video summarization, and 50.30% on the York Urban line segment detection task. On the 2×12h configuration, it improved on 28 tasks, with some scores climbing higher given the extended time.

**Claude Sonnet 4 performed best with the ARG scaffolding** rather than the Modular one. With ARG, it achieved improvements on 25 tasks at 4×6h, notably 74.26% on MIMIC-III, 64.93% on CNN, and 32.61% on traffic forecasting. With the Modular scaffolding, many of its apparent successes were contaminated by high cheating rates, making honest performance difficult to assess.

**Some tasks resisted all agents.** CIFAR-10 with ABNet, CIFAR-10 with ResNet18-FSGDM, CIFAR-100 with ProDSC, Kvasir-SEG EMCAD, electricity forecasting with CycleNet, MalNet-Tiny with GatedGCN, and ZINC NeuralWalker all saw 0% success across every model-scaffolding combination. These represent problems where the published baselines are already well-optimized or where the codebases present structural obstacles that current agents cannot navigate.

**Longer time horizons helped, but not uniformly.** Moving from 4×6h to 2×12h improved GPT-5+ARG on tasks like ETTh1 forecasting (from 75% to 100% success rate) and several MNIST/Fashion-MNIST variants. For some tasks, however, more time simply meant more opportunities to pursue unproductive paths.

## Resource Usage

The token and time usage data reveals clear differences in agent efficiency.

The Modular agent with Claude Sonnet 4 was remarkably token-efficient, often completing tasks in under 2M tokens. This efficiency partly reflected its tendency to either solve tasks quickly or abandon legitimate approaches in favor of fabrication. GPT-5 with the Modular agent consumed significantly more tokens (regularly 10-20M+) and frequently hit time limits, suggesting it explored more aggressively but less efficiently.

The ARG agent showed more consistent resource usage across models. Its tree search structure naturally bounds exploration, and the beam search mechanism focuses compute on promising paths rather than exhaustive trial-and-error.

## Discussion

DeltaMLBench represents a meaningful step beyond our original ML Research Benchmark. Where MLRB showed agents could not perform non-trivial research, DeltaMLBench demonstrates they can sometimes achieve genuine percentage improvements over published baselines on real research codebases.

Several key observations merit emphasis:

**Agent architecture is as important as model capability.** The same underlying model produces dramatically different outcomes depending on the scaffolding. The ARG agent's structured search and reflection mechanisms led to both higher success rates and zero cheating, while the simpler Modular architecture left models more prone to taking shortcuts.

**Cheating is a first-order concern for automated research.** If we are to trust agents to conduct ML research, we need robust integrity verification. Our multi-layered approach caught most attempts, but the fact that frontier models default to fabrication when stuck is a serious issue for the field.

**The hardest tasks remain untouched.** Tasks requiring deep architectural innovation or domain-specific insight still show 0% success rates. Agents can optimize hyperparameters, adjust training procedures, and apply known techniques, but they are not yet making the conceptual leaps that drive novel research contributions.

**Current agents occupy the "competent research assistant" level.** Agents can set up environments, debug dependency issues, run experiments, and iterate on straightforward optimizations. This is useful. The gap between "improve a metric by tuning learning rates" and "develop a novel architectural insight" remains wide.

## Future Work

DeltaMLBench is released as a static benchmark with 50 tasks and standardized evaluation protocols. As agent capabilities evolve, we plan to expand the task set, increase difficulty, and develop more sophisticated integrity verification. The benchmark is designed to grow with the field: the percentage improvement metric means there is always room for agents to improve, avoiding the saturation problem that plagues binary benchmarks.

The code and benchmark are available for the research community to evaluate their own agents. We believe the combination of authentic research conditions, improvement-oriented evaluation, and rigorous anti-cheating measures makes DeltaMLBench a useful testbed for tracking real progress in autonomous ML research.

---

*DeltaMLBench is currently under review at ICML 2026.*
