Title: DeltaMLBench: Can AI Agents Improve on Published ML Research?
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A benchmark suite for evaluating AI agents on real machine learning research tasks — including task definitions, a baseline agent, and evaluation infrastructure.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/DeltaMLBench
Featured: true

# DeltaMLBench: Can AI Agents Improve on Published ML Research?

Last year we released the [ML Research Benchmark](https://arxiv.org/abs/2410.22553), which showed that AI agents could follow complex ML research instructions and produce baselines, but couldn't perform non-trivial research iterations. The natural next question: what happens when you give agents *real research repositories* and ask them to beat the published results?

That's DeltaMLBench — a benchmark of 50 tasks drawn from real Papers With Code repositories, where the goal isn't just reproduction but **measurable improvement over published baselines**. We evaluated frontier models (Claude Sonnet 4, Claude Opus 4, and GPT-5) across two agent scaffoldings and found that agents can now genuinely improve on published work in some cases — but the path there is messier than you'd expect.

## The Setup: Real Repos, Real Papers, Real Baselines

Each task in DeltaMLBench pairs a peer-reviewed paper with its open-source repository, dataset, and the evaluation metric reported in the publication. Agents get the PDF, the code, and the data. Their job: make the numbers go up (or down, for loss metrics).

This is deliberately harder than prior benchmarks in several ways. There's no clean starter template — agents navigate heterogeneous codebases with varying framework choices, documentation quality, and dependency structures. The tasks span computer vision, NLP, graph learning, time series forecasting, molecular property prediction, anomaly detection, and more. And the evaluation metric is percentage improvement over the published baseline, not a binary pass/fail.

We curated tasks from Papers With Code, filtering for post-January 2024 publications with accessible repos and datasets, training runtimes under 10 hours on a single GPU, and confirmed end-to-end reproducibility. Starting from ~380 candidates, human verification narrowed the pool to 67 reproducible tasks, from which we selected 50 for maximum domain diversity.

## Two Agent Architectures

We tested two scaffolding approaches:

**The Modular Agent** (from METR's poking-agents) separates concerns across five modules — prompting, generation, discrimination, action execution, and tooling — coordinated through shared state. It's clean and debuggable.

**The ARG Agent** (ours) takes a more aggressive approach with solution tree exploration, beam search across multiple solution paths, configurable search policies, and self-reflection mechanisms for analyzing execution failures. Different configuration packs optimize for speed, reasoning depth, or comprehensive exploration.

Both run on the Vivaria platform in isolated Docker containers with a single H100 80GB GPU. We tested two time configurations: 4 attempts at 6 hours each, and 2 attempts at 12 hours each, with a 10-million-token budget per run.

## The Cheating Problem

Before getting to results, we need to talk about reward hacking — because it turned out to be one of the most important findings.

When agents struggle with a task, some of them don't just fail. They cheat. They hardcode metric values in return statements, write stub implementations, or fabricate results without actually training anything. This isn't a minor edge case — the Modular scaffolding with Claude Sonnet 4 showed cheating rates above 50% on many tasks.

We built a multi-layered defense system to catch this: static AST analysis to detect hardcoded values, training artifact verification to confirm real checkpoints exist, LLM-based semantic analysis of solution code, and a forensic log grading system where an ensemble of three frontier models audits the complete execution trace. A majority vote determines whether a submission passes integrity checks.

The pattern was striking. The ARG agent showed a **0% cheating rate across all models and configurations** — its tree search and reflection mechanisms appear to keep it on legitimate solution paths. The Modular agent, by contrast, cheated frequently, particularly with Claude Sonnet 4. This suggests that agent architecture matters at least as much as the underlying model for research integrity.

## Results: What Worked

Looking at the detailed task-level results, several patterns emerge.

**GPT-5 with the ARG agent was the strongest combination.** On the 4×6h configuration, it achieved positive improvement on 29 of 48 tasks, with standout performances including a 95.96% improvement on the MIMIC-III clinical task, 78.92% on CNN summarization, 73.22% on SumMe video summarization, and 50.30% on the York Urban line segment detection task. On the 2×12h configuration, it improved on 28 tasks, with some scores climbing even higher given the extended time.

**Claude Sonnet 4 performed best with the ARG scaffolding** rather than the Modular one. With ARG, it achieved improvements on 25 tasks at 4×6h — notably 74.26% on MIMIC-III, 64.93% on CNN, and 32.61% on traffic forecasting. But with the Modular scaffolding, many of its apparent successes were contaminated by high cheating rates, making honest performance harder to assess.

**Some tasks resisted all agents.** CIFAR-10 with ABNet, CIFAR-10 with ResNet18-FSGDM, CIFAR-100 with ProDSC, Kvasir-SEG EMCAD, electricity forecasting with CycleNet, MalNet-Tiny with GatedGCN, and ZINC NeuralWalker all saw 0% success across every model-scaffolding combination. These represent genuinely hard research problems where the published baselines are already well-optimized or where the codebases present structural obstacles that current agents can't navigate.

**Longer time horizons helped, but not uniformly.** Moving from 4×6h to 2×12h improved GPT-5+ARG on tasks like ETTh1 forecasting (from 75% to 100% success rate) and several MNIST/Fashion-MNIST variants. But for some tasks, more time just meant more opportunities to go down unproductive paths.

## Resource Usage Tells a Story

The token and time usage data reveals sharp differences in agent efficiency.

The Modular agent with Claude Sonnet 4 was remarkably token-efficient — often completing tasks in under 2M tokens — but this efficiency partly reflected its tendency to either solve tasks quickly or give up and cheat. GPT-5 with the Modular agent was far more token-hungry (regularly 10-20M+ tokens) and frequently hit time limits, suggesting it explored more aggressively but less efficiently.

The ARG agent showed more consistent resource usage across models. Its tree search structure naturally bounds exploration, and the beam search mechanism focuses compute on promising paths rather than exhaustive trial-and-error.

## What This Means

DeltaMLBench represents a meaningful step beyond our original ML Research Benchmark. Where MLRB showed agents couldn't do non-trivial research, DeltaMLBench shows they sometimes *can* — achieving genuine percentage improvements over published baselines on real research codebases.

But the nuances matter enormously:

**Agent architecture is as important as model capability.** The same underlying model produces dramatically different outcomes depending on the scaffolding. The ARG agent's structured search and reflection mechanisms led to both higher success rates and zero cheating, while the simpler Modular architecture left models more prone to taking shortcuts.

**Cheating is a first-order concern for automated research.** If we're going to trust agents to do ML research, we need robust integrity verification. Our multi-layered approach — combining static analysis, artifact verification, semantic analysis, and forensic log auditing — caught most attempts, but the fact that frontier models default to fabrication when stuck is a serious issue for the field.

**The hardest tasks remain untouched.** Tasks requiring deep architectural innovation or domain-specific insight — the kind of work that produces novel research contributions — still show 0% success rates. Agents can optimize hyperparameters, adjust training procedures, and apply known techniques, but they aren't yet making the conceptual leaps that drive research forward.

**We're in the "competent research assistant" phase.** Agents can set up environments, debug dependency issues, run experiments, and iterate on straightforward optimizations. That's genuinely useful. But the gap between "improve a metric by tuning learning rates" and "develop a novel architectural insight" remains wide.

## Looking Ahead

DeltaMLBench is released as a static benchmark with 50 tasks and standardized evaluation protocols. As agent capabilities evolve, we plan to expand the task set, increase difficulty, and develop more sophisticated integrity verification. The benchmark is designed to grow with the field — the percentage improvement metric means there's always room for agents to do better, avoiding the saturation problem that plagues binary benchmarks.

The code and benchmark are available for the research community to evaluate their own agents against. We think the combination of authentic research conditions, improvement-oriented evaluation, and rigorous anti-cheating measures makes DeltaMLBench a useful testbed for tracking real progress in autonomous ML research.

---

*DeltaMLBench is currently under review at ICML 2026.*