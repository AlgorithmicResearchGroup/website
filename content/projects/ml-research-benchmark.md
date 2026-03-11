Title: ML Research Benchmark: Can AI Agents Do Real ML Research?
Date: 2025-01-01
Tags: agent-evaluation, benchmarks, python
Summary: A benchmark suite of 7 competition-level ML challenges for evaluating whether AI agents can perform genuine research iteration beyond baseline reproduction.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/ML-Research-Agent
Featured: true

# Can AI Agents Do Real ML Research? We Built a Benchmark to Find Out

AI agents have become remarkably capable at writing code, browsing the web, and completing complex tasks. Whether they can do something more difficult remains an open question: can they actually perform machine learning research? This means not just running a training script, but making the kinds of decisions a researcher makes: choosing architectures, tuning hyperparameters, iterating on failed experiments, and pushing toward state-of-the-art results.

To investigate this, we built the **ML Research Benchmark (MLRB)**, a suite of 7 competition-level challenges drawn directly from recent ML conference tracks at NeurIPS, ICML, and CoNLL. We then evaluated two frontier AI agents on these tasks.

## Why Conference Competitions?

Existing agent benchmarks like MLAgentBench focus on canonical ML tasks: CIFAR-10 classification, Kaggle regression challenges, and similar well-studied problems. These are useful but do not capture the difficulty of the work that capabilities researchers perform in practice.

Conference competition tracks are different. They represent the current frontier of applied ML research: training efficient models under strict compute budgets, compressing large language models for edge devices, translating informal math proofs into formal verification languages. These are problems where top human researchers compete, and winning solutions often get published.

Competition tasks also resist the saturation problem that plagues binary benchmarks. There is always room for improvement, which means the benchmark can grow with agent capabilities rather than becoming obsolete.

## The Seven Challenges

MLRB spans the core activities of ML research:

**Pretraining:** The *MiniPile Challenge* asks agents to pretrain the best possible language model on a moderate-sized dataset and evaluate on SuperGLUE. The *BabyLM Challenge* goes further: train from scratch on just ~10 million words and evaluate on BLiMP.

**Fine-tuning under constraints:** The *LLM Efficiency Challenge* (1 LLM + 1 GPU + 1 Day) requires fine-tuning an approved base model to maximize MMLU performance within 24 hours on a single A100.

**Model compression:** The *Edge LLM Compression* track tasks agents with compressing Microsoft's Phi-2 model to fit in 12GB DRAM, with no quantization allowed. Only structural compression techniques like pruning are permitted.

**Training from scratch for edge:** The *Edge LLM Training* track demands training a model from scratch that fits in just 1GB of DRAM while performing well on SuperGLUE.

**Model merging:** The *LLM Merging Competition* challenges agents to combine multiple expert models into a single generalist that performs well on MMLU.

**Domain-specific reasoning:** The *Auto-Formalization* track requires training a model to translate natural language mathematical proofs into formal Lean 3 code, bridging informal reasoning and machine-verifiable proofs.

All tasks share the same constraints: a single A100 40GB GPU, 24-hour time limit, and no starter code provided. Agents must determine the approach from the task description alone.

## Agent Setup

We built a baseline agent with a supervisor-worker architecture. The supervisor manages task instructions and progress; the worker executes using a modular toolkit including Python/Bash execution, file management, GitHub access, and academic paper search. The agent uses a ReAct-style reasoning loop, recording intermediate thoughts and actions.

We evaluated two configurations: one powered by **GPT-4o** and one by **Claude 3.5 Sonnet**, running each agent 5 times per task.

## Results: Baseline Success, Research Failure

The central finding is a clear gap between producing baselines and performing research.

Both agents could follow complex multi-step instructions, set up training pipelines, and produce working models. The Claude 3.5 Sonnet agent was more consistent overall, outperforming GPT-4o on 5 of 7 tasks. On MiniPile, Claude succeeded in 4 of 5 runs (averaging 0.541 on SuperGLUE) versus GPT-4o's single successful run (0.457). On Edge LLM Compression, Claude's pruning approach pushed MMLU to 0.551 in its best run.

Neither agent, however, demonstrated what we would characterize as non-trivial research iteration. They did not explore multiple architectural approaches, ablate their design choices, or meaningfully improve upon their initial solutions. When the Claude agent trained a custom GPT-2 variant for the BabyLM challenge (6 layers, 12 heads, 768-dim embeddings, ~82M parameters), it arrived at reasonable hyperparameters but did not experiment with alternatives or iterate based on evaluation feedback.

The Math Reasoning task was especially revealing. Both agents failed to produce any compilable Lean 3 code across all runs. GPT-4o's fine-tuned Flan-T5 achieved marginally better BLEU/ROUGE scores, while Claude's LoRA fine-tuning of Mistral-7B showed more ambition but no better results. The task requires bridging informal and formal mathematical reasoning, something that demands genuine research insight rather than pipeline assembly.

Time management was another weak point. Agents frequently chose models or training configurations that could not converge within the 24-hour window, and sometimes failed to checkpoint their work, losing hours of compute to a single error.

## Discussion

MLRB makes visible a capability threshold that matters for both AI safety and acceleration research: the difference between an agent that can implement a known approach and one that can discover a better one.

Current frontier agents sit firmly on the implementation side. They are remarkably good at translating a task description into a working pipeline: choosing a model, writing training code, handling tokenization edge cases, running evaluation. This is valuable. The research loop, however (hypothesize, experiment, analyze, iterate), remains out of reach.

At roughly $43 per run and $300 per full benchmark evaluation, the economics are also worth noting. As agents improve, the cost-performance tradeoff of automated ML research will become increasingly important.

## Future Work

Five runs per task limits statistical confidence, and both the agent scaffolds and underlying models are rapidly evolving. The benchmark itself will need to expand with more tasks, more diverse ML subfields, and eventually tasks that require longer research horizons.

The framework is in place. MLRB provides a gradient of difficulty that will not saturate quickly, grounded in the actual work of ML research rather than synthetic tasks. As agents improve, we will be able to measure exactly how they are improving and where the remaining gaps lie.

The code is available at [github.com/AlgorithmicResearchGroup/ML-Research-Agent](https://github.com/AlgorithmicResearchGroup/ML-Research-Agent).

---

*This work was supported by Open Philanthropy, with valuable feedback from Ajeya Cotra, Tom Davidson, and Eli Lifland.*
