Title: ML Research Benchmark: Can AI Agents Do Real ML Research?
Date: 2025-01-01
Tags: agent-evaluation, benchmarks, python
Summary: A benchmark suite for evaluating AI agents on real machine learning research tasks — including task definitions, a baseline agent, and evaluation infrastructure.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/ML-Research-Agent
Featured: true

# Can AI Agents Do Real ML Research? We Built a Benchmark to Find Out

AI agents are getting remarkably good at writing code, browsing the web, and completing complex tasks. But can they do something harder — can they actually *do machine learning research*? Not just run a training script, but make the kinds of decisions a researcher makes: choosing architectures, tuning hyperparameters, iterating on failed experiments, and pushing toward state-of-the-art results?

To answer that question, we built the **ML Research Benchmark (MLRB)** — a suite of 7 competition-level challenges drawn directly from recent ML conference tracks at NeurIPS, ICML, and CoNLL. We then pointed two frontier AI agents at them and watched what happened.

## Why Conference Competitions?

Existing agent benchmarks like MLAgentBench focus on canonical ML tasks — CIFAR-10 classification, Kaggle regression challenges, and the like. These are useful, but they don't capture the difficulty of the work that capabilities researchers actually do day-to-day.

Conference competition tracks are different. They represent the current frontier of applied ML research: training efficient models under strict compute budgets, compressing large language models for edge devices, translating informal math proofs into formal verification languages. These are hard problems where top human researchers compete, and winning solutions often get published.

Crucially, competition tasks also resist the saturation problem that plagues binary benchmarks. There's always room for improvement, which means the benchmark can grow with agent capabilities rather than becoming obsolete.

## The Seven Challenges

MLRB spans the core activities of ML research:

**Pretraining:** The *MiniPile Challenge* asks agents to pretrain the best possible language model on a moderate-sized dataset and evaluate on SuperGLUE. The *BabyLM Challenge* goes further — train from scratch on just ~10 million words and evaluate on BLiMP.

**Fine-tuning under constraints:** The *LLM Efficiency Challenge* (1 LLM + 1 GPU + 1 Day) requires fine-tuning an approved base model to maximize MMLU performance within 24 hours on a single A100.

**Model compression:** The *Edge LLM Compression* track tasks agents with compressing Microsoft's Phi-2 model to fit in 12GB DRAM — no quantization allowed, only structural compression techniques like pruning.

**Training from scratch for edge:** The *Edge LLM Training* track demands training a model from scratch that fits in just 1GB of DRAM while performing well on SuperGLUE.

**Model merging:** The *LLM Merging Competition* challenges agents to combine multiple expert models into a single generalist that performs well on MMLU.

**Domain-specific reasoning:** The *Auto-Formalization* track requires training a model to translate natural language mathematical proofs into formal Lean 3 code — bridging informal reasoning and machine-verifiable proofs.

All tasks share the same constraints: a single A100 40GB GPU, 24-hour time limit, and no starter code provided. Agents must figure out the approach from the task description alone.

## The Agent Setup

We built a baseline agent with a supervisor-worker architecture. The supervisor manages task instructions and progress; the worker executes using a modular toolkit including Python/Bash execution, file management, GitHub access, and academic paper search. The agent uses a ReAct-style reasoning loop, recording intermediate thoughts and actions.

We evaluated two configurations: one powered by **GPT-4o** and one by **Claude 3.5 Sonnet**, running each agent 5 times per task.

## Results: Baseline Success, Research Failure

The headline finding is a clear gap between *producing baselines* and *doing research*.

Both agents could follow complex multi-step instructions, set up training pipelines, and produce working models. The Claude 3.5 Sonnet agent was more consistent overall, outperforming GPT-4o on 5 of 7 tasks. On MiniPile, Claude succeeded in 4 of 5 runs (averaging 0.541 on SuperGLUE) versus GPT-4o's single successful run (0.457). On Edge LLM Compression, Claude's pruning approach pushed MMLU to 0.551 in its best run.

But neither agent demonstrated what we'd call non-trivial research iteration. They didn't explore multiple architectural approaches, ablate their design choices, or meaningfully improve upon their initial solutions. When the Claude agent trained a custom GPT-2 variant for the BabyLM challenge — 6 layers, 12 heads, 768-dim embeddings, ~82M parameters — it arrived at reasonable hyperparameters, but it didn't experiment with alternatives or iterate based on evaluation feedback.

The Math Reasoning task was especially revealing. Both agents failed to produce any compilable Lean 3 code across all runs. GPT-4o's fine-tuned Flan-T5 achieved marginally better BLEU/ROUGE scores, while Claude's LoRA fine-tuning of Mistral-7B showed more ambition but no better results. The task requires bridging informal and formal mathematical reasoning — something that demands genuine research insight, not just pipeline assembly.

Time management was another weak point. Agents frequently chose models or training configurations that couldn't converge within the 24-hour window, and sometimes failed to checkpoint their work, losing hours of compute to a single error.

## What This Tells Us

MLRB makes visible a capability threshold that matters enormously for AI safety and acceleration: the difference between an agent that can *implement* a known approach and one that can *discover* a better one.

Current frontier agents sit firmly on the implementation side. They're remarkably good at translating a task description into a working pipeline — choosing a model, writing training code, handling tokenization edge cases, running evaluation. That's valuable. But the research loop — hypothesize, experiment, analyze, iterate — remains out of reach.

At roughly $43 per run and $300 per full benchmark evaluation, the economics are also worth noting. As agents improve, the cost-performance tradeoff of automated ML research will become increasingly important.

## What's Next

Five runs per task limits statistical confidence, and both the agent scaffolds and underlying models are rapidly evolving. The benchmark itself will need to expand — more tasks, more diverse ML subfields, and eventually tasks that require longer research horizons.

But the framework is in place. MLRB provides a gradient of difficulty that won't saturate quickly, grounded in the actual work of ML research rather than synthetic tasks. As agents get better, we'll be able to measure exactly *how* they're getting better — and where the remaining gaps lie.

The code is available at [github.com/AlgorithmicResearchGroup/ML-Research-Agent](https://github.com/AlgorithmicResearchGroup/ML-Research-Agent).

---

*This work was supported by Open Philanthropy, with valuable feedback from Ajeya Cotra, Tom Davidson, and Eli Lifland.*