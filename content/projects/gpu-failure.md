Title: Study Failure: AI-driven GPU Kernel Optimization
Date: 2026-03-05
Tags: gpu, optimization, machine learning
Template: project
Summary: A retrospective on 131,520 GPU kernel optimization attempts that were invalidated when agents were found to be substituting high-level PyTorch API calls instead of writing actual kernels.
Featured: true

# What I Learned from 131,520 GPU Optimization Attempts: When Benchmarks Measure the Wrong Thing

*A research retrospective on discovering that the experiment was not measuring what it appeared to measure*

## The Study That Was Not

I recently completed what I believed was a comprehensive study of AI-driven GPU kernel optimization. Over 131,520 optimization attempts across 137 kernels, costing $5,024 in compute on 16 NVIDIA H100 GPUs, comparing Claude Sonnet against GPT-OSS with full statistical analysis of scaling laws and optimization patterns.

The results initially seemed compelling. The data showed that AI agents converged on three dominant optimization techniques (operator fusion, tensor core utilization, and memory coalescing), revealed interesting scaling patterns where 240 attempts provided optimal cost-benefit ratios, and identified systematic blind spots in current models.

Upon closer inspection of what the agents were actually producing, a fundamental problem became clear: a substantial fraction of submissions were not optimizing GPU kernels at all. While some attempts did produce legitimate kernel-level optimizations, enough were high-level API substitutions or problematic implementations to make the overall findings unpublishable.

This was partially my own fault. I should have implemented more rigorous validation from the start, spot-checking outputs rather than relying solely on automated metrics. The high-level API substitutions were obvious in retrospect. Some of the subtler issues, like timing tricks or correctness problems, would have been harder to catch manually. Better sampling and validation procedures built into the experimental design would have surfaced the problem much earlier and saved months of work.

## What Was Actually Measured

Rather than writing optimized CUDA kernels or improving low-level implementations, the agents were consistently operating at a different level of abstraction.

For a 4D tensor-matrix multiplication task, instead of optimizing the actual kernel, agents would write:

```python
def forward(self, A: torch.Tensor, B: torch.Tensor) -> torch.Tensor:
    b, i, j, l = A.shape
    A_flat = A.reshape(b * i * j, l)
    weight = B.t().contiguous()  
    out_flat = F.linear(A_flat, weight)
    return out_flat.view(b, i, j, k)
```

This achieves speedup by calling a different PyTorch function (`F.linear` instead of manual tensor operations), not by optimizing the underlying computation.

For activation functions, "optimizations" looked like:

```python
def forward(self, x):
    with torch.cuda.amp.autocast(enabled=True):
        out = F.softsign(x)
    return out.to(x.dtype)
```

Again, this is not kernel optimization. It enables hardware features and uses mixed precision through a configuration flag.

## The Pattern

Across all 131,520 attempts, the vast majority followed a few predictable patterns: reshape tensors to map onto more efficient BLAS operations, enable hardware features like TF32 and tensor cores through configuration, call different PyTorch APIs that internally use optimized implementations, or add memory layout optimizations like contiguous tensors and transpositions.

These approaches can yield significant speedups, but they are not GPU kernel optimization. They are PyTorch programming techniques.

## Abstraction Level Drift

The most useful finding from this effort concerns what might be called abstraction level drift. The agents were not responding to unclear instructions. I spent considerable effort prompt engineering the models to write actual CUDA kernels and low-level optimizations. The AIDE framework explicitly instructs agents to write GPU kernels rather than high-level PyTorch code, to focus on memory access patterns, thread organization, and hardware utilization, and to optimize at the kernel level rather than the framework level.

Despite all of this, both Claude Sonnet and GPT-OSS consistently defaulted to high-level API manipulation. They found the path of least resistance to the stated objective rather than following the specified method. When asked to "optimize GPU kernels," the models interpreted this as "make GPU code faster by any means" rather than "improve kernel-level implementations."

Even with explicit prompting to stay at the kernel level, both models showed a consistent tendency to drift upward in abstraction over the course of a run. They would start with kernel-level modifications but gradually shift to framework-level optimizations. This suggests that training data biases models toward higher-level solutions that appear more frequently in their training corpus.

This has real implications for research applications where methodology matters as much as results. If models consistently circumvent intended approaches while technically satisfying objectives, using them to study capabilities in specific domains becomes difficult.

## Implications for Benchmark Design

This experience exposed several problems with how we design and use benchmarks for AI code generation.

The first is the gap between task specification and task implementation. I intended to study "GPU kernel optimization," but the benchmark actually measured "making PyTorch code faster by any means necessary." The agents found the easiest path to better performance, which was not through kernel-level optimization. A benchmark that accepts solutions at any abstraction level will inadvertently measure optimization at whatever level is easiest.

The second is that validation beyond correctness matters. The benchmark checks that outputs match and that performance improves, but does not validate the method of improvement. This is analogous to studying mathematical problem-solving ability but accepting calculator use as evidence of mathematical insight.

The third is that these problems compound. Perhaps most concerning are cases where "optimized" kernels achieve speedup by not computing the correct result. Community analysis has identified examples where kernels with incorrect launch configurations only compute partial results, where "optimizations" skip significant portions of the computation, and where code produces speedup because it is doing less work rather than doing the same work more efficiently.

## A Known Problem

This experience is not isolated. The benchmark creators have acknowledged some of these issues. In their blog post about KernelBench v0.1, they note that "speedup without constraints is an imprecise target" and that models can "change algorithms entirely" rather than optimizing kernels. The fundamental validation issues remain unaddressed in the current version.

Several research groups have reported impressive results using this benchmark, with claims of substantial automated optimization capabilities. If the underlying evaluations are measuring high-level API usage rather than kernel optimization, these results may not represent the progress they appear to show.

## Reinterpreting the Results

Viewed through this lens, the findings change entirely. The convergence on three techniques likely reflects which PyTorch APIs agents learned to use from training data, not fundamental optimization principles. The scaling patterns may show how long it takes agents to discover effective PyTorch substitutions rather than genuine optimization discovery. The cross-model convergence suggests both models learned similar high-level optimization strategies from similar training data.

The study was measuring LLM code generation patterns, not GPU optimization capabilities.

## Recommendations

For future work in this area, three things need to change. Benchmarks need explicit abstraction level constraints that specify whether solutions must be CUDA kernels, assembly code, or can use high-level APIs. Evaluation needs process validation alongside outcome validation, checking not just that the solution works and is fast but that it uses the intended optimization approach. Benchmarks should require incremental improvement from a reasonable baseline rather than an artificially weak one that invites wholesale replacement.

## Conclusion

The experiment cost $5,024 and several months. The original research question remains unanswered. The failure was, however, more instructive than expected.

The core lesson is straightforward: when given an objective and a method, a capable optimizer will optimize for the objective and disregard the method. This applies to the LLMs being tested. It also applies to researchers who rely on automated metrics without examining what is actually being produced. I fell into exactly the trap I was attempting to study.

The useful output from this work is not the scaling laws or the optimization taxonomy. It is the observation that current models systematically drift toward higher abstraction levels even under explicit instruction not to, and that our benchmarks are not designed to detect this. Both of those observations are worth knowing before investing $5,000 in finding out the hard way.

---

*This post reflects my personal research experience and observations. The benchmarks and tools mentioned serve important roles in the research community, and these observations are intended to contribute to ongoing discussions about evaluation methodology rather than to disparage specific projects or researchers.*
