Title: ArXiv QA BEIR Datasets
Slug: opensource-arxiv-qa-beir
Save_as: opensource/arxiv-qa-beir.html
Artifact_group: Datasets
Artifact_order: 080
Summary: Two arXiv generated-query releases containing BEIR-style relevance tables: 1,480,132 query–document rows in the 500K variant and 296,327 in the 100K variant.
Template: resource
Url: opensource/arxiv-qa-beir.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 080

- [AlgorithmicResearchGroup/arxiv-beir-500k-generated-queries](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-beir-500k-generated-queries)
- [AlgorithmicResearchGroup/arxiv-beir-100k-generated-queries](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-beir-100k-generated-queries)

<!-- resource-details -->

## Linking research queries to documents

These releases provide **BEIR-style relevance tables** for generated queries associated with arXiv material. They are published in two variants: the **500K release contains 1,480,132 rows**, and the **100K release contains 296,327 rows**. Each row connects a query identifier to a corpus identifier and a relevance score. The dataset names describe the variants; the row counts describe the released query–document associations. [500K release](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-beir-500k-generated-queries), [100K release](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-beir-100k-generated-queries).

## The retrieval format

The 500K dataset card explains the three components of a BEIR-style retrieval dataset. A **corpus** contains document identifiers, titles, and text. A **query set** supplies identifiers and query text. A **qrels table** connects queries to relevant documents using `query-id`, `corpus-id`, and `score`.

The released Parquet tables correspond to that third component. Their schema stores `query-id` as text and the corpus identifier and score as integers. Both repositories expose a single `train` split. This structure makes the associations easy to join to the corresponding query and document collections when those are available. [Documented format](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv-beir-500k-generated-queries/blob/main/README.md).

## What is included in these downloads

The published repositories currently contain a README and a Parquet shard of relevance rows. They do **not** include the corpus text or query text described in the 500K card's format example. Running a retrieval experiment therefore requires the matching text collections; a relevance table alone cannot supply the passages to search or the questions to encode. The download links lead to these available relevance tables.

## Generated queries and documentation

The release names identify generated queries, and the 500K card describes an English dataset derived from arXiv. It leaves the collection and curation procedure unspecified, including the query-generation model and any human review of relevance. The 100K card contains schema and size metadata only. These releases should consequently be understood as generated-query retrieval artifacts, without assuming expert-authored queries or independently verified relevance judgments.
