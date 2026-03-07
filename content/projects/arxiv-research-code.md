Title: ArXiv Research Code Dataset: 129K Research Repositories
Date: 2026-03-01
Tags: agent-evaluation, benchmarks, python
Summary: A benchmark suite for evaluating AI agents on real machine learning research tasks — including task definitions, a baseline agent, and evaluation infrastructure.
Template: project
Repo: https://github.com/AlgorithmicResearchGroup/ArXivResearchCode
Featured: true

# The ArXiv Research Code Dataset: 4.7 Million Files from 129K Research Repositories

Most code datasets are built from the general population of open-source software — web apps, CLI tools, infrastructure code. That's useful for training general-purpose code models, but it doesn't capture how researchers actually write code. Research code has its own conventions, its own library ecosystem, and its own structural patterns. If you want models that understand and generate research code, you need training data drawn from research repositories.

The ArXiv Research Code Dataset is a collection of **4,716,175 code files from 129,232 unique repositories** linked to computer science papers on arXiv. The full dataset is 21.6 GB and is available on [HuggingFace](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv_research_code).

## How We Built It

The dataset was created through a multi-stage pipeline:

1. **Extract GitHub URLs from arXiv papers.** We parsed metadata and full text from CS arXiv papers to identify those with linked GitHub repositories.
2. **Clone and process repositories.** Each repository was downloaded and decomposed into individual code files, focusing on common research-oriented programming languages.
3. **Compute file-level metrics.** For each file, we derived structural metadata including file length, average line length, and maximum line length.

The result is a snapshot of the code that accompanies published computer science research — not synthetic benchmarks or toy examples, but the actual implementations behind peer-reviewed work.

## What's in the Dataset

Each entry contains:

- **repo** — the repository name
- **file** — the file path within the repository
- **code** — the full file contents
- **file_length** — total number of lines
- **avg_line_length** — average characters per line
- **max_line_length** — longest line in the file
- **extension_type** — the file extension

## Language Distribution

The dataset reflects the programming language preferences of the CS research community. Python dominates at 17.5% of all files (827,135 files), followed by C/C++ at 15.8% (743,207 files) and Java at 13.0% (615,191 files). The full breakdown:

| Language | Files | Share |
|----------|------:|------:|
| Python | 827,135 | 17.54% |
| C/C++ | 743,207 | 15.76% |
| Java | 615,191 | 13.04% |
| HTML | 359,375 | 7.62% |
| C | 302,533 | 6.41% |
| Markdown | 201,196 | 4.27% |
| Objective-C | 170,582 | 3.62% |
| C++ | 162,715 | 3.45% |
| YAML | 142,877 | 3.03% |
| Go | 125,270 | 2.66% |
| Shell | 88,581 | 1.88% |
| TypeScript | 50,907 | 1.08% |
| Ruby | 34,739 | 0.74% |
| R | 25,311 | 0.54% |
| Rust | 24,026 | 0.51% |
| Scala | 23,478 | 0.50% |

The remaining languages (CSS, PHP, Perl, SQL, Lua, C#, Swift, JavaScript) each account for less than 0.4%.

## Deep Dive: The Python Subset

Given Python's central role in ML research, we did a focused analysis on the Python subset — roughly 827K files across 23,874 repositories. Some highlights:

**Library usage tells you what researchers actually depend on.** NumPy appears in 30.4% of all Python files, confirming its role as the bedrock of scientific computing. PyTorch follows at 19.8%, well ahead of TensorFlow at 3.9%. Pandas (4.3%), matplotlib (1.5%), and SciPy (1.2%) round out the top tier. About 24% of Python files use at least one ML/DL library.

| Library | Files | Share |
|---------|------:|------:|
| NumPy | 417,793 | 30.38% |
| PyTorch | 272,330 | 19.80% |
| Pandas | 59,505 | 4.33% |
| TensorFlow | 52,918 | 3.85% |
| Matplotlib | 20,844 | 1.52% |
| SciPy | 16,143 | 1.17% |
| Scikit-learn | 6,005 | 0.44% |
| Keras | 3,773 | 0.27% |
| NLTK | 2,970 | 0.22% |
| SpaCy | 1,362 | 0.10% |

**Code structure is modular and function-heavy.** The average Python file contains 7.6 import statements, 8.3 function definitions, and 1.3 class definitions. Files average 220 lines of code, with 2.9 for-loops and about 1 list comprehension per file. Error handling is moderate (0.46 try-except blocks per file), and there's light use of functional patterns (0.37 lambdas per file). The overall picture is modular, function-oriented code — which makes sense for research that needs to be iterated on quickly.

**Code quality is high.** 97.15% of Python files in the dataset are syntactically valid (1,375,548 valid out of 1,415,924 total). Average cyclomatic complexity across all repositories is 23.88, though the range is enormous — from single-function scripts to massive monolithic modules with complexity scores above 20,000.

**Repository sizes vary dramatically.** The largest repository (catboost) contains 22,994 Python files, while many repositories contain just a handful. This reflects the full spectrum of research software, from large collaborative frameworks to single-paper implementations.

## Limitations

A few things to keep in mind:

**ArXiv bias.** The dataset only covers papers posted to arXiv, which skews toward fields that use it as a primary preprint server (ML, AI, theoretical CS, physics-adjacent work). Research code from communities that publish elsewhere is underrepresented.

**GitHub only.** We collected code exclusively from GitHub. Repositories hosted on GitLab, Bitbucket, institutional servers, or kept private aren't captured.

**Static snapshot.** The dataset represents repositories at a single point in time. Research code evolves — bugs get fixed, experiments get added, dependencies change. The dataset doesn't capture that trajectory.

## Use Cases

The ArXiv Research Code Dataset is designed to support several downstream applications: LLM pretraining and fine-tuning on research code, retrieval-augmented generation for coding assistants, code completion models specialized for scientific computing, and training data for autonomous research agents. The combination of scale (4.7M files), domain specificity (CS research), and metadata (structural metrics per file) makes it a useful complement to general-purpose code datasets.

The dataset is available at [huggingface.co/datasets/AlgorithmicResearchGroup/arxiv_research_code](https://huggingface.co/datasets/AlgorithmicResearchGroup/arxiv_research_code).