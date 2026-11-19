Title: DeltaMLBench
Slug: opensource-deltamlbench
Save_as: opensource/deltamlbench.html
Artifact_group: Code & Benchmarks
Artifact_order: 030
Summary: A benchmark for testing whether agents can improve published machine learning work. The Inspect release includes 35 task families, feedback-visible and feedback-hidden variants, paper baselines, and an audit of submitted code and reported metrics.
Template: resource
Url: opensource/deltamlbench.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 030

- [AlgorithmicResearchGroup/DeltaMLBench](https://github.com/AlgorithmicResearchGroup/deltaml-bench-inspect)
- [Paper (PDF)]({static}/papers/deltaml-bench.pdf)
- [Task papers, code snapshots, and datasets](https://huggingface.co/buckets/AlgorithmicResearchGroup/dmlb)

<!-- resource-details -->

DeltaMLBench starts with an existing research result and asks an agent to improve it. Each task connects a paper, a codebase, data, and a performance target. The experiment is about the additional progress an agent can make from that starting point.

The current public release runs through **Inspect AI**. It supports **35 active task families derived from Papers with Code**, each exposed in two forms, for 70 task variants. This page describes that supported release; the accompanying paper provides the broader research context.

## Feedback as an experimental variable

Each family has a `main` variant that exposes a scoring tool and a `hidden_score` variant that withholds intermediate scoring feedback. Both use the same scorer. “Hidden” describes the feedback available to the agent; it does not mean a separate hidden-label dataset.

That pairing makes it possible to investigate how access to evaluation feedback changes an agent's research process while holding the underlying task and scoring procedure fixed.

## How an improvement is scored

An agent submits code whose `solution.evaluate()` function reports the task metrics, together with execution evidence. The runtime checks the report against the submitted code and declared logs, then sends a redacted code-and-trajectory bundle to an integrity judge. Accepted metrics are compared with the checked-in paper baseline and task-specific constraints.

The [scoring protocol](https://github.com/AlgorithmicResearchGroup/deltaml-bench-inspect/blob/master/docs/SCORER_PROTOCOL.md) makes an important boundary explicit: this process audits agent-reported measurements; it does not independently rerun the model on a second hidden dataset. It also documents how code hashes, metric consistency checks, and judge decisions enter the result.

## What the release provides

The repository includes task manifests, setup and scoring code, Docker sandbox configuration, Inspect task wrappers, and the `modular-public` agent integration. Papers, repository snapshots, and datasets are fetched from ARG's public Hugging Face storage bucket. The supplied `doctor` command checks the objects required by active task manifests before a run.

Begin with the README's no-model smoke test to check installation, sandboxing, and scoring. Full research runs require task-appropriate compute and may need GPUs. The supported Inspect suite excludes archived tasks and the legacy `ai_rd_*` families; use the current task listing when designing comparisons.

[Read the DeltaMLBench research article]({filename}/projects/delta-ml-bench.md) for the study behind the benchmark.
