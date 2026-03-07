Title: Learning to Rank Architectures: A Small Model That Guides Neural Architecture Search
Date: 2026-03-04
Tags: nas, architecture search, machine learning
Template: project
Summary: I trained a tiny recursive reasoning model to rank architectures by predicted performance, then used it to guide search. It achieved 8-10x sample efficiency over random search, finding a 94.37% accuracy architecture in roughly 25 evaluations instead of 210. And the predictor, trained only on CIFAR-10 data, transferred zero-shot to CIFAR-100 and ImageNet16-120 with almost no loss in ranking quality.
Repo: https://github.com/AlgorithmicResearchGroup/NAS-public 
Featured: true

Most neural architecture search methods are expensive. You define a search space, evaluate thousands of architectures by training each one to convergence, and hope the best one justifies the compute bill. The core inefficiency is obvious: the vast majority of those evaluations are wasted on architectures that were never going to be competitive.

I wanted to see if a small model could learn to predict which architectures are worth evaluating and skip the rest. Not as a research project I planned to publish — more as an excuse to poke at NAS-Bench-201 and see whether ranking-oriented training objectives actually matter in practice.

The short version: I trained a tiny recursive reasoning model to rank architectures by predicted performance, then used it to guide search. It achieved **8-10x sample efficiency** over random search, finding a 94.37% accuracy architecture in roughly 25 evaluations instead of 210. And the predictor, trained only on CIFAR-10 data, transferred zero-shot to CIFAR-100 and ImageNet16-120 with almost no loss in ranking quality. That last part surprised me.

Here's how it went.

## Getting a Baseline Predictor Working

The setup is straightforward. NAS-Bench-201 contains 15,625 architectures with pre-computed accuracies on CIFAR-10, CIFAR-100, and ImageNet16-120. I sampled 900 architectures for training and 100 for testing. Each architecture is encoded as a token sequence representing its operations (skip_connect, conv_3x3, conv_1x1, avg_pool), fed through a small transformer with Adaptive Computation Time (TinyRecursiveReasoningModel_ACTV1), and mapped to a scalar performance prediction via a linear regression head trained with MSE loss.

The first training run produced garbage. R² of -61.3, Spearman correlation of -0.18, predictions collapsed to near zero. Worse than predicting the mean for every architecture.

The culprit was a single line in the data loader:

```python
batch = {k: v.astype(np.int32) for k, v in batch.items()}
```

This cast everything to int32, including the float32 labels. An accuracy of 0.946 became 0. An accuracy of 0.992 became 0. The model was training on a dataset where 98% of labels were zero. Classic.

After fixing the dtype handling, the model achieved Spearman 0.71 and MAE of 0.039 — predictions within about 4% of true accuracy on average. The R² was only 0.10, but for NAS, ranking matters more than regression. If you can correctly order architectures, you can find good ones efficiently even if your absolute predictions are off.

## Ranking Loss Makes the Predictor Better at What Matters

The baseline predictor optimizes MSE — it tries to get the absolute numbers right. But for architecture search, I don't care whether the predictor says an architecture will achieve 94.2% vs 93.8%. I care whether it correctly identifies which of two architectures is better.

Pairwise ranking loss directly optimizes for this. For each pair of architectures (a, b) where a outperforms b, the model is penalized if it doesn't predict a higher score for a by at least some margin. I implemented this as a margin-based loss, sampling 64 pairs per batch to avoid the O(n²) cost of all pairs, and combined it 50/50 with the original MSE loss.

The results confirmed the hypothesis:

| Metric | MSE Only | 50% Ranking + 50% MSE | Change |
|--------|:--------:|:---------------------:|:------:|
| Spearman ρ | 0.712 | **0.779** | +9.4% |
| Kendall τ | 0.554 | **0.617** | +11.3% |
| R² | 0.100 | 0.017 | -83% |
| MAE | 0.039 | 0.076 | +97% |

Ranking metrics improved substantially. Regression metrics got worse. This is the expected and desired trade-off. The model now correctly orders 78% of architecture pairs, up from 71%. It pays for this by making larger absolute errors — some predictions even exceed 1.0, which is physically impossible for an accuracy value. But none of that matters for search.

The design choices that mattered: the 0.01 margin was small enough to distinguish architectures with similar performance (the accuracy range in NAS-Bench-201 spans roughly 0.85 to 1.0), and 64 sampled pairs per batch provided sufficient gradient signal without the 500x cost of exhaustive pairing.

## Predictor-Guided Architecture Search

With a ranking-capable predictor in hand, I built a simple search algorithm:

1. Evaluate 10 random architectures to seed the search
2. For each of 40 iterations: sample 100 random candidates, score them with the predictor, evaluate the top 5 against ground truth
3. Track the best architecture found

Total budget: 210 evaluations. I compared this against pure random search with the same budget.

| Method | Best Accuracy | Evals to 94% |
|--------|:------------:|:------------:|
| Predictor-Guided | **94.37%** | ~25 |
| Random Search | 93.78% | 210+ |

The predictor-guided search found its best architecture in about 25 evaluations. Random search needed all 210 and still fell short. That's roughly 8x sample efficiency — in a real NAS setting where each evaluation requires hours of GPU training, this translates directly to an 87.5% reduction in compute cost.

The distribution of evaluated architectures tells the story. The predictor-guided search concentrated 90% of its evaluations on architectures above 90% accuracy. Random search spread evaluations across the full range, wasting many on architectures below 70%. The predictor functions as a filter: it can't tell you exactly how good an architecture is, but it can reliably tell you which ones aren't worth training.

## Zero-Shot Transfer Across Datasets

This was the part I didn't expect to work as well as it did. I took the predictor — trained exclusively on CIFAR-10 architectures — and used it to guide search on CIFAR-100 and ImageNet16-120 without any retraining.

**Predictor ranking quality (zero-shot):**

| Dataset | Spearman ρ | Training Data? |
|---------|:----------:|:--------------:|
| CIFAR-10 | 0.779 | Yes (in-domain) |
| CIFAR-100 | **0.785** | No (zero-shot) |
| ImageNet16-120 | **0.770** | No (zero-shot) |

The ranking quality barely degraded. On CIFAR-100, it actually improved slightly. The absolute prediction errors got worse (MAE jumped from 0.076 to 0.205 on ImageNet16-120), and R² went deeply negative (-0.68), but the relative ordering held. The predictor doesn't know what accuracy an architecture will achieve on ImageNet16-120. It does know which architectures are structurally better than others, and that property transfers.

**Search results (zero-shot):**

| Dataset | Predictor-Guided | Random Search | Improvement |
|---------|:----------------:|:-------------:|:-----------:|
| CIFAR-10 | 94.37% | 93.78% | +0.59% |
| CIFAR-100 | **73.20%** | 71.16% | **+2.87%** |
| ImageNet16-120 | **46.50%** | 45.37% | **+2.50%** |

The improvement was actually larger on the transfer datasets than on the original. Harder datasets have wider performance spreads, so effective filtering saves more wasted evaluations.

One detail I liked: architecture #13714 was the best found on both CIFAR-10 and CIFAR-100. Certain architectural motifs appear to be genuinely universal.

## Why This Works

The transfer result makes sense once you think about it. All three datasets share the same NAS-Bench-201 architecture space — same operations, same cell topology, same 15,625 possible designs. The predictor learns structural properties: skip connections enable gradient flow, convolution diversity improves feature extraction, efficient topologies reduce overfitting. These properties don't depend on whether the downstream task is 10-class or 100-class classification.

The pairwise ranking loss is critical to this. A model trained with pure MSE learns the absolute mapping from architecture to CIFAR-10 accuracy. That mapping doesn't transfer — CIFAR-100 accuracies live in a completely different range. But the relative ordering does transfer, and ranking loss optimizes directly for ordering.

## What I'd Do Differently

I only used 900 of the 15,625 available architectures for training. Scaling to the full dataset would almost certainly improve predictor quality. The search algorithm is also deliberately simple — random sampling plus top-k filtering. Evolutionary mutations or Bayesian optimization could squeeze more out of each evaluation.

The model has no notion of uncertainty. It produces point estimates with no indication of confidence. I prototyped a variance head but didn't fully evaluate it. In principle, uncertainty-aware search would let you selectively evaluate architectures where the predictor is least sure, which should improve both search efficiency and predictor quality over time.

And the transfer experiments are all within NAS-Bench-201, where datasets share the same architecture space. Transfer across different search spaces would be a much harder and more interesting test.

## Takeaways

A few things I found useful from this exercise:

**Ranking is the right objective for NAS.** Spearman 0.78 — achieved by a model with near-zero R² — is sufficient to drive 8-10x sample efficiency gains. If you're building architecture predictors, optimize for ordering, not regression.

**Small models can learn useful architectural priors.** This predictor is a tiny transformer with 256 hidden dimensions and 2 layers. It trains in 3 minutes on 2 GPUs. The representations it learns transfer across datasets with no fine-tuning.

**Data bugs can be catastrophic and subtle.** The int32 truncation bug produced a model that appeared to train normally but learned nothing useful. Without systematic evaluation metrics, I would have spent days debugging the wrong things.

**Zero-shot transfer changes the economics.** One predictor trained on 900 CIFAR-10 architectures guided effective search on three datasets. That's a meaningful reduction in total NAS cost if you're searching across multiple tasks.

I'm not planning to follow this up further — it was mainly a way to build intuition about predictor-guided search and see whether the ranking-vs-regression distinction holds up empirically. It does. If you're doing NAS on a tabular search space, a small ranking predictor trained on your cheapest dataset is probably worth the 3 minutes it takes to train.