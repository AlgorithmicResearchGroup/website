Title: ArXiv Semantic Search Models
Slug: opensource-arxiv-semantic-search-models
Save_as: opensource/arxiv-semantic-search-models.html
Artifact_group: Models
Artifact_order: 090
Summary: DistilBERT and DistilRoBERTa encoders trained on generated arXiv question–abstract pairs, producing 768-dimensional embeddings for scientific search and similarity.
Template: resource
Url: opensource/arxiv-semantic-search-models.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 090

- [AlgorithmicResearchGroup/arxiv-distilbert-base-v3-GenQ](https://huggingface.co/AlgorithmicResearchGroup/arxiv-distilbert-base-v3-GenQ)
- [AlgorithmicResearchGroup/arxiv-distilroberta-base-GenQ](https://huggingface.co/AlgorithmicResearchGroup/arxiv-distilroberta-base-GenQ)

<!-- resource-details -->

## Finding papers by meaning

These two models turn scientific sentences and paragraphs into 768-dimensional vectors. Encode a question and a collection of abstracts, then compare their embeddings to rank candidate papers by semantic similarity. Each input produces a vector that can be stored in a search index; the models do not generate an answer or a summary.

The releases share a Sentence Transformers interface and mean pooling over token representations. Their backbones differ: the [DistilBERT configuration](https://huggingface.co/AlgorithmicResearchGroup/arxiv-distilbert-base-v3-GenQ/blob/main/config.json) identifies `distilbert-base-uncased`, while the [DistilRoBERTa configuration](https://huggingface.co/AlgorithmicResearchGroup/arxiv-distilroberta-base-GenQ/blob/main/config.json) identifies `distilroberta-base`. Both have six transformer layers, twelve attention heads, and a hidden dimension of 768.

## Training on generated questions

The [DistilBERT model card](https://huggingface.co/AlgorithmicResearchGroup/arxiv-distilbert-base-v3-GenQ) and [DistilRoBERTa model card](https://huggingface.co/AlgorithmicResearchGroup/arxiv-distilroberta-base-GenQ) describe training on question–abstract pairs from the [arXiv generated-query corpus](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-beir-500k-generated-queries). Both record one training epoch, batches of 64, and `MultipleNegativesRankingLoss` with cosine similarity and a scale of 20. The optimizer was AdamW at a learning rate of `2e-5`, with linear warmup and weight decay of `0.01`.

The cards credit Matthew Kenney, 2023, and retain the original ArtifactAI names in their examples. The download links point to the current AlgorithmicResearchGroup repositories. Both model releases specify Apache 2.0 licensing.

## Working with the embeddings

Load either repository with `SentenceTransformer` and call `encode()` on a list of strings. A direct Transformers implementation needs the tokenizer, the encoder, and attention-mask-aware mean pooling; the cards include that alternative. Padding tokens should not contribute to the average.

Both saved Sentence Transformers configurations limit an input to **350 tokens**, even though the underlying encoders support longer sequences. Full papers therefore need an explicit passage-splitting or truncation strategy. Keep the same model and preprocessing for queries and indexed passages.

The cards document training settings but do not publish numerical retrieval scores or a controlled comparison between the two variants. They provide a starting point for scientific search, with retrieval quality to be measured against the queries and relevance judgments of the intended collection.
