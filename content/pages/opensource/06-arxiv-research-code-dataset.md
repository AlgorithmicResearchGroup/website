Title: ArXiv Research Code Dataset
Slug: opensource-arxiv-research-code
Save_as: opensource/arxiv-research-code.html
Artifact_group: Datasets
Artifact_order: 060
Summary: 4,716,175 files collected from GitHub repositories referenced in arXiv papers, with source text, repository paths, and file-level metadata for code-model research.
Template: resource
Url: opensource/arxiv-research-code.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 060

- [AlgorithmicResearchGroup/arxiv_research_code](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv_research_code) (21 GB)

<!-- resource-details -->

## The code behind the papers

ArXiv Research Code collects the repository files behind published research into a corpus for code language models. The release contains **4,716,175 file-level examples**. Each row preserves the file's text together with its repository name, path, and basic size statistics, making it possible to work with research implementations at a scale larger than a hand-selected collection of projects. [Original dataset card](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv_research_code).

## How the corpus was assembled

The release card documents **34,099 active GitHub repository names** extracted from arXiv papers, covering papers from arXiv's inception through **July 21, 2023**. The collected repositories totaled 773 GB compressed before filtering and file extraction. That process produced the approximately 4.7 million files in the published dataset.

The card reports approximately **21.8 GB of downloadable data**; its metadata records about **63.4 GB of dataset content**. Those figures describe different representations of the release, rather than separate versions. The card does not give a detailed account of the filtering rules. [Collection description and release metadata](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv_research_code/blob/main/README.md).

## Files with their context intact

The `code` field contains the file text. The `repo` and `file` fields identify its repository and path; `extension_type` records the extension. `file_length` counts characters, while `avg_line_length` and `max_line_length` describe the file's lines. These fields support practical corpus inspection and filtering without first parsing every file.

The unit of this corpus is a source file. For function-level instructions built from research code, see [ArXivDLInstruct]({filename}/pages/opensource/05-arxiv-dl-instruct-dataset.md).

## Loading and using the data

All examples are supplied in one `train` split. The card documents both a full download and streaming through Hugging Face Datasets, so examples can be read incrementally without downloading the entire corpus first. No held-out evaluation split is provided. The original release also notes that files copied from public GitHub repositories may retain emails, IP addresses, or credentials; that is a concrete consideration when inspecting and preparing this source corpus.
