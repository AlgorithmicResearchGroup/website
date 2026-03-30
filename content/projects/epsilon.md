Title: Epsilon: Infrastructure for Structured Agent Workloads
Date: 2026-03-30
Tags: agents, orchestration, infrastructure
Template: project
Summary: An open-source runtime for structured agent workloads with seven orchestration topologies, ZeroMQ-backed task brokering, deterministic reducers, and a population search mode for recursive improvement loops.
Repo: https://github.com/AlgorithmicResearchGroup/epsilon
Featured: true

# Epsilon: Infrastructure for Structured Agent Workloads

[GitHub →](https://github.com/AlgorithmicResearchGroup/epsilon)

\#agents \#orchestration \#infrastructure

# Epsilon: Infrastructure for Structured Agent Workloads

Most AI agent tooling is built around one prompt, one model call, and one output. That works for demos. It breaks down when you need to split work across many agents, retry failures without restarting the whole job, keep intermediate artifacts machine-readable, selectively escalate only the cases that need deeper reasoning, or mix LLM steps with deterministic aggregation and validation.

Epsilon is a runtime for workloads that are too structured for a chat app and too judgment-heavy for a plain data pipeline. It gives you explicit orchestration topologies, a real message broker with leases and heartbeats, deterministic reducers for the parts of your pipeline where consistency matters more than open-ended reasoning, and a population search mode for recursive improvement loops.

We built it to run our own research. Now it is open source under Apache 2.0.

## The Core Idea

The architecture is a clean split between four components:

**Orchestrators** decide how work gets decomposed and coordinated. They select a topology, manage dependencies between tasks, and decide when to retry, reduce, or escalate follow-up work.

**Workers** execute the leaves of a topology. Depending on the workload, a leaf can be an LLM-driven agent task, a deterministic reducer, a local executor, or a custom agent plugged in via the BYOA (Bring Your Own Agent) adapter path.

**The broker** handles task assignment, lease management, heartbeats, renewals, redelivery, and dead-letter protection. It is built on ZeroMQ and provides at-least-once delivery semantics. This is real distributed systems infrastructure, not "hope the API call works."

**Shared workspace artifacts** keep intermediate state on disk rather than hiding it in an internal state machine. Every intermediate output is explicit and inspectable. This matters for reproducibility, for reducer and finalizer handoff, and for post-run debugging.

## Eight Orchestration Topologies

Epsilon ships with eight topology patterns, each designed for a different class of workload:

**dag.** Parallel build work with QA and fix loops. The orchestrator decomposes a task into a typed DAG, executes nodes in dependency-ordered waves, runs a QA agent, assigns failures back to responsible agents, and repeats until QA passes or the wave budget is exhausted.

**tree.** Hierarchical team-style decomposition. Large tasks get broken into 2-8 teams, each with its own sub-orchestrator and git branch. Teams run in parallel, branches merge, and an integration QA pass runs on the merged result.

**pipeline.** Staged delivery. Work flows through sequential stages with gates between them.

**supervisor.** Adaptive retries and task splitting. The supervisor monitors progress and can dynamically split failing tasks into smaller pieces or reassign them.

**work_queue.** Flat pull-based worker execution. Workers pull tasks from a shared queue and execute them independently. Simple and effective for embarrassingly parallel workloads.

**sharded_queue.** Very large independent item sets. Manifest-backed: you provide a list of items and Epsilon fans them out across workers. Designed for workloads with tens of thousands of independent tasks.

**map_reduce.** Hierarchical aggregation. Fan-out to many workers, then structured reduction of results. Also manifest-backed, designed for workloads where the aggregation step matters as much as the individual task execution.

**population_search.** Recursive improvement loops. Multiple agents optimize the same task in parallel, a deterministic scorer evaluates every candidate, a generation brief captures what worked, and the next generation gets the best solutions as context. This is the topology most directly relevant to studying recursive self-improvement.

The `sharded_queue`, `map_reduce`, and `population_search` topologies are intentionally manifest-backed. They are designed for explicit high-scale workloads, not free-form decomposition from a single natural-language prompt.

## Why The Split Matters

Epsilon is not just "many agents." The useful architectural properties are:

**Topology is explicit.** You choose how work gets decomposed. The system does not guess at structure from a natural language prompt. This makes behavior predictable and debuggable.

**Agent work and deterministic work can be mixed.** In the same job, some leaves can be LLM-driven and others can be pure functions. Use agents where judgment helps. Use reducers where you need consistency.

**Failure handling is isolated.** When a leaf fails, only that leaf gets retried or reassigned. The rest of the job continues. This is essential for workloads with hundreds or thousands of tasks where individual failures are expected.

**Second-pass reasoning is targeted.** Instead of rerunning everything, you can identify the ambiguous or failed cases and send only those to a second wave of agents. This is how our Benchmark Scout and Entity Graph demos work: agents extract, reducers flag problems, a second wave adjudicates only the flagged cases.

**Intermediate artifacts are inspectable.** Because everything goes to disk in structured form, you can pause a run, inspect what happened, and resume or reprocess. No black-box internal state.

## The Broker

The messaging layer provides the reliability semantics that real workloads require:

At-least-once delivery for work queue tasks. Lease-based task ownership so that if a worker dies mid-task, the work gets reassigned. Heartbeat-driven liveness eviction for detecting dead workers. Dead-letter protection for poison tasks that fail repeatedly. Bounded retries for explicit task failure. Broadcast and directed messaging between agents. Last-value cache replay for topic state.

The protocol is split into three planes: a transport plane (ZeroMQ sockets move bytes), a topology plane (routing policy decides delivery), and a coordination plane (heartbeats, leases, renewals, and redelivery).

## BYOA: Bring Your Own Agent

You do not have to use Epsilon's built-in agent runtime. The BYOA adapter path lets you plug in your own agent process without changing orchestrators. This works two ways:

A function-entrypoint path where you point Epsilon at a Python function and it handles the rest. Or a stdin/stdout action-protocol path where your agent communicates through a simple JSON action protocol (log, send_message, check_messages, done, fail).

This means you can use Epsilon's orchestration, brokering, and topology management with whatever agent implementation you already have.

## Demos

Epsilon ships with working demos that exercise the system at realistic scale:

**Population Search CSV.** Multiple agents optimize the same CSV aggregation function in parallel. Epsilon scores every candidate deterministically, captures what worked in a generation brief, and feeds the best solutions as context to the next generation. This is recursive improvement in miniature: a small, self-contained loop where you can watch the system improve across generations.

**HF Entity Graph.** Agents summarize and extract entities from raw document clusters. Reducers detect ambiguous entities across documents. A second wave of agents adjudicates only the ambiguous cases. This demonstrates the two-pass pattern that makes Epsilon practical for noisy, real-world extraction tasks.

Additional demos exist for benchmark harvesting across paper corpora and other research workflows. Some rely on local research data and are not featured in the top-level README.

## What You Can Build

The system is general enough to support a range of workloads:

Software builds with decomposition, QA, and fix loops. Document extraction and curation workflows. Benchmark and result harvesting across large corpora. Manifest-backed workloads that fan out to hundreds or thousands of agent tasks. Recursive improvement experiments with population search. Custom agent systems using the BYOA adapter path.

## Configuration

Epsilon is configured through a combination of `manifest.json` (model selection, iteration budgets, delegate LLM allowlists) and environment variables (API keys, broker addresses, executor backend, wave budgets). It supports OpenAI, Anthropic, and any provider accessible through LiteLLM. Docker execution is supported as an alternative to host-based execution, with published images available via GHCR.

## Availability

Epsilon is available now under Apache 2.0:

- **Repository:** [github.com/AlgorithmicResearchGroup/epsilon](https://github.com/AlgorithmicResearchGroup/epsilon)
- **Documentation:** Architecture overview, technical reference, and release notes are in the `docs/` directory.

This is the infrastructure we use to run our own research. The population search topology is directly relevant to our work on recursive self-improvement. The sharded queue and map reduce topologies are what we use to process large corpora for our datasets. The DAG and tree topologies are what we use for multi-agent software builds and evaluation runs.

We are releasing it because infrastructure for structured agent workloads should not be something every team builds from scratch.