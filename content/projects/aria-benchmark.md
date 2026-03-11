Title: ARIA Benchmark: How Much Machine Learning Do AI Models Actually Know?
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A suite of five closed-book benchmarks probing the ML knowledge that frontier language models have internalized during training.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/ARIA
Featured: true

# ARIA Benchmarks: How Much Machine Learning Do AI Models Actually Know?

Large language models are trained on vast amounts of text, including a substantial body of machine learning research. The question of how much of that knowledge they actually retain is worth investigating directly. Can they recall which modality a dataset belongs to, identify which evaluation metrics were used in a specific paper, or detect the odd model out in a list of architectures?

ARIA (AI Research Intelligence Assessment) is a suite of five closed-book benchmarks designed to probe the ML knowledge that frontier models have internalized during training. No retrieval, no web search, no chain-of-thought scaffolding. The evaluation isolates the model and its embedded understanding of the field.

The benchmarks and evaluation framework are open source at [github.com/AlgorithmicResearchGroup/ARIA](https://github.com/AlgorithmicResearchGroup/ARIA).

## The Five Tasks

Each benchmark targets a different dimension of ML knowledge:

**Dataset Modality QA.** Given a dataset name, predict its modality (Audio, Computer Vision, Graphs, NLP, Reinforcement Learning, or Sequential). This tests basic familiarity with the datasets that populate ML research: whether the model recognizes that CIFAR-10 is images and SQuAD is text.

**Model Modality QA.** Given a model name, predict its primary modality or application area. This evaluates whether models have internalized the landscape of ML architectures: knowing that BERT is NLP and ResNet is vision.

**Odd Model Out.** Given a list of ML models, identify which one does not belong. This is the most nuanced task, requiring the model to understand subtle categorical relationships between architectures, training paradigms, and application domains.

**PWC Metrics.** Given a specific paper title, model name, and dataset, predict which evaluation metrics were reported. This tests knowledge of evaluation conventions: which metrics are standard for which tasks and domains.

**PWC Metrics:Result.** The most difficult task. Same setup as above, but the model must also recall the specific numerical results reported in the paper. This requires detailed, granular knowledge of state-of-the-art performance figures.

All benchmarks were constructed from Papers With Code data, with automatically generated natural language questions, carefully curated answer choices, and validation for accuracy and balance across ML subfields.

## Models Evaluated

We tested a broad cross-section of frontier models:

**Proprietary:** GPT-4o, GPT-4, GPT-3.5-Turbo, Claude 3 Opus, Claude 3 Sonnet, Claude 3 Haiku, and Gemini Pro.

**Open source:** Mistral-7B (v0.1 and v0.3), Intel neural-chat-7b, openchat_3.5, zephyr-7b-beta, Meta-Llama-3-8B-Instruct, and Phi-3-medium-4k-instruct.

## Results

The results reveal a clear hierarchy with several notable patterns:

| Benchmark | GPT-4o | GPT-4 | GPT-3.5-Turbo | Claude Opus | Claude Sonnet | Claude Haiku | Gemini Pro |
|-----------|:------:|:-----:|:-------------:|:-----------:|:-------------:|:------------:|:----------:|
| Dataset Modality QA | 68.5% | 62.0% | 47.7% | **71.9%** | 69.9% | 71.6% | 45.8% |
| Model Modality QA | **85.3%** | 82.0% | 73.1% | 79.8% | 74.8% | 78.8% | 75.6% |
| Odd Model Out | **56.2%** | 45.6% | 35.4% | 45.1% | 36.9% | 30.7% | 37.1% |
| PWC Metrics | **53.0%** | 46.6% | 39.2% | 49.7% | 42.2% | 27.3% | 37.3% |
| PWC Metrics:Result | 2.5% | 3.0% | **8.5%** | 6.5% | 2.0% | 2.5% | 5.5% |

**GPT-4o was the strongest model overall**, leading on three of five tasks: Model Modality QA (85.3%), Odd Model Out (56.2%), and PWC Metrics (53.0%). Its broad ML knowledge and ability to make fine-grained distinctions between models and metrics produced a consistent advantage.

**Claude Opus achieved the highest score on Dataset Modality QA** at 71.9%, with Claude Haiku close behind at 71.6%. The Claude family generally showed strong dataset recognition, outperforming GPT-4o on this particular task.

**The Odd Model Out task was difficult for all models.** GPT-4o's leading score of 56.2% means it identified the outlier incorrectly nearly half the time. Most models hovered around 30-45%, suggesting that nuanced categorical reasoning about ML architectures remains a consistent weakness.

**Recalling specific numerical results is nearly impossible at current capability levels.** On PWC Metrics:Result, no model exceeded 8.5% accuracy. GPT-3.5-Turbo scored highest at 8.5%, possibly due to its training data composition or a tendency to produce numerical outputs that happen to be correct more often. Across the board, models cannot reliably recall that a particular ResNet achieved 76.3% top-1 accuracy on ImageNet in a specific paper. The required knowledge granularity exceeds what current training procedures retain.

**Open source models lagged but showed promise in specific areas.** On Model Modality QA, several open-source 7B-8B models cleared 70% accuracy, not far behind some proprietary models. The gap widened on harder tasks, particularly Odd Model Out and PWC Metrics, where scale and training data breadth appear to matter more.

## Interpretation

ARIA reveals a stratified picture of ML knowledge in language models. At the coarsest level, recognizing that a model or dataset belongs to a particular domain, even small models perform reasonably well. This is the kind of knowledge that appears frequently in training data and requires only surface-level pattern matching.

At the intermediate level, knowing which metrics are standard for a given task or recognizing subtle groupings among model architectures, performance drops significantly. This requires more structured, relational knowledge about the ML ecosystem.

At the finest level, recalling specific numbers from specific papers, models essentially fail. This is unsurprising; these facts would require something closer to memorization of individual papers, and the sheer volume of ML research makes reliable recall implausible.

For practitioners building AI research agents or ML coding assistants, these findings have practical implications. Models possess solid high-level ML knowledge that can inform architectural choices and evaluation strategies. They should not be trusted to recall specific benchmark numbers or make fine-grained distinctions between similar approaches without retrieval support.

## Reproducibility

The benchmark creation scripts and evaluation framework are publicly available. We use the [UK AI Safety Institute's Inspect framework](https://inspect.ai-safety-institute.org.uk/) for standardized evaluation, ensuring consistent results across research groups. The full code is at [github.com/AlgorithmicResearchGroup/ARIA](https://github.com/AlgorithmicResearchGroup/ARIA).

## Limitations

ARIA tests closed-book recall, not reasoning. A model might score poorly on recalling specific metrics but excel at using metric results when provided in context. The multiple-choice format also constrains evaluation: it cannot capture the nuance of a model's reasoning process or partial knowledge. The underlying Papers With Code data carries its own biases toward well-known papers and popular subfields, which inevitably shapes what the benchmarks measure.

Future versions could incorporate open-ended questions, multilingual evaluation, and time-stratified tasks to test awareness of recent developments versus foundational knowledge.
