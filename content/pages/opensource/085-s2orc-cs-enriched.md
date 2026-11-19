Title: S2ORC CS Enriched
Slug: opensource-s2orc-cs-enriched
Save_as: opensource/s2orc-cs-enriched.html
Artifact_group: Datasets
Artifact_order: 085
Summary: 1,117,706 computer science papers from Allen AI’s S2ORC, with full text and LLM-generated fields for methods, results, models, datasets, limitations, and compute.
Template: resource
Url: opensource/s2orc-cs-enriched.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 085

- [AlgorithmicResearchGroup/s2orc-cs-enriched](https://huggingface.co/datasets/AlgorithmicResearchGroup/s2orc-cs-enriched) (54.7 GB)

<!-- resource-details -->

## A literature corpus you can query

S2ORC CS Enriched brings **1,117,706 computer science papers** into one collection with structured fields for what each paper does. The source is Allen AI’s [Semantic Scholar Open Research Corpus](https://github.com/allenai/s2orc). ARG adds LLM-generated metadata to help turn a large body of research into something you can filter and inspect.

The release has one `train` split, distributed across **1,118 Parquet files totaling approximately 54.7 GB**. The [published schema and split statistics](https://datasets-server.huggingface.co/info?dataset=AlgorithmicResearchGroup%2Fs2orc-cs-enriched) describe 58 columns. The rows retain titles, abstracts, full text, sections, figure descriptions, references, authors, publication information, citation counts, and source identifiers such as DOI and Semantic Scholar corpus ID. Paper-level license and open-access fields travel with those records.

## What the enrichment adds

Fourteen generated fields describe the paper’s summary, classification, methods, results, models, datasets, evaluation metrics, limitations, and training setup. This makes it possible to look for combinations of properties—for example, papers mentioning a particular model and dataset—without starting every search from unstructured text.

The compute fields distinguish **explicitly reported GPU hours** from **estimated GPU hours**. GPU count, hardware type, training details, and the reasoning behind compute estimates are stored separately. That distinction matters when comparing what authors actually report with what an extraction process infers. The [dataset card](https://huggingface.co/datasets/AlgorithmicResearchGroup/s2orc-cs-enriched#dataset-structure) documents the field definitions.

## Working with the collection

The structured records support literature discovery, mapping methods across a research area, and assembling candidate evidence for comparisons of datasets, metrics, or compute reporting. Retained paper identifiers and text provide a route from an extracted field back to the source.

The enrichment is generated metadata. Check important extracted claims against the retained paper text, particularly numerical results and compute estimates. Fields such as `methods`, `datasets`, and `metrics` are published as strings, so inspect their values before treating them as native lists. The Hugging Face streaming example lets you begin inspecting records without downloading the entire collection.
