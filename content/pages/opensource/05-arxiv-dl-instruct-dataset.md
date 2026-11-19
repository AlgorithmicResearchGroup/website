Title: ArXiv DL Instruct Dataset
Slug: opensource-arxiv-dl-instruct
Save_as: opensource/arxiv-dl-instruct.html
Artifact_group: Datasets
Artifact_order: 050
Summary: 778,152 Python research-code functions paired with generation prompts, short descriptions, and their surrounding source files for code instruction tuning.
Template: resource
Url: opensource/arxiv-dl-instruct.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 050

- [AlgorithmicResearchGroup/ArXivDLInstruct](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct) (2.26 GB)

<!-- resource-details -->

## From research code to instructions

ArXivDLInstruct turns Python research code into function-level instruction examples. Each example pairs an existing function with a prompt describing what to write and a short description of its purpose. The release contains **778,152 examples**, bringing the implementation and its requested behavior together in a form intended for code-model instruction tuning. The source code comes from GitHub research repositories referenced by arXiv papers. [Original dataset card](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct).

## Inside an example

The central fields are `prompt`, `description`, and `function`: the instruction, a one-sentence description, and the corresponding code. Additional fields retain `function_name`, `function_summary`, and `file_number`. Repository and file identifiers connect the example to its source, while `full_code` preserves the surrounding file rather than leaving every function isolated from its imports, neighboring definitions, and other context.

The release also includes file length, average and maximum line length, and file-extension metadata. These fields make it possible to inspect or filter the corpus before assembling a training set—for example, by selecting examples with manageable source-file lengths or retaining full-file context alongside the target function. The complete schema is recorded in the [release metadata](https://huggingface.co/datasets/AlgorithmicResearchGroup/ArXivDLInstruct/blob/main/README.md).

## Working with the release

The dataset ships as a single `train` split in Parquet, with an approximately **2.26 GB download**. It can be loaded through Hugging Face Datasets using `AlgorithmicResearchGroup/ArXivDLInstruct`.

A direct training setup pairs `prompt` with `function`; a context-aware setup can additionally supply `full_code`. These are ways to use the published fields, rather than evaluated recipes supplied with the release. There is no separate validation or test split. The card describes the instruction examples but does not specify how their prompts and descriptions were produced or independently checked. It also notes that the underlying public GitHub code may retain sensitive information, including credentials, so corpus inspection remains part of preparing a training run.
