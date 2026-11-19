Title: ArXiv LED Summarization Models
Slug: opensource-arxiv-led-summarization-models
Save_as: opensource/arxiv-led-summarization-models.html
Artifact_group: Models
Artifact_order: 100
Summary: Base and large Longformer Encoder–Decoder checkpoints for arXiv summarization, with 16,384-token input capacity and published test-set ROUGE results.
Template: resource
Url: opensource/arxiv-led-summarization-models.html
Author: Algorithmic Research Group
Origin: Algorithmic Research Group
Resource_order: 100

- [AlgorithmicResearchGroup/led_large_16384_arxiv_summarization](https://huggingface.co/AlgorithmicResearchGroup/led_large_16384_arxiv_summarization)
- [AlgorithmicResearchGroup/led_base_16384_arxiv_summarization](https://huggingface.co/AlgorithmicResearchGroup/led_base_16384_arxiv_summarization)

<!-- resource-details -->

## A longer view of the paper

These English-language checkpoints use Allen Institute for AI's Longformer Encoder–Decoder architecture to generate summaries of scientific papers. The release cards describe abstracts and full document text as inputs, with a text summary as the output. Both support an encoder input of up to **16,384 tokens**; this is a token budget, rather than a guarantee that every paper will fit.

The [base configuration](https://huggingface.co/AlgorithmicResearchGroup/led_base_16384_arxiv_summarization/blob/main/config.json) has six encoder layers, six decoder layers, and a hidden dimension of 768. The [large configuration](https://huggingface.co/AlgorithmicResearchGroup/led_large_16384_arxiv_summarization/blob/main/config.json) doubles the layer counts to twelve each and increases the hidden dimension to 1,024. Both use `LEDForConditionalGeneration`, with a 1,024-token encoder attention window and a 1,024-position decoder.

## Training provenance and recorded results

The checkpoints identify `allenai/led-base-16384` and `allenai/led-large-16384` as their respective source models. The cards associate the releases with `arxiv-summarization`, but do not provide a complete fine-tuning recipe: epoch counts, optimizer settings, and exact training subsets are not documented there. The underlying architecture comes from *Longformer: The Long-Document Transformer* by Iz Beltagy, Matthew E. Peters, and Arman Cohan.

Hugging Face's recorded evaluation metadata reports the following scores on the **`section` configuration, `test` split** of `ccdv/arxiv-summarization`. These are the published evaluation results, not a new benchmark run. Sources: [base model card](https://huggingface.co/AlgorithmicResearchGroup/led_base_16384_arxiv_summarization) and [large model card](https://huggingface.co/AlgorithmicResearchGroup/led_large_16384_arxiv_summarization).

| Checkpoint | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-LSUM |
| --- | ---: | ---: | ---: | ---: |
| LED base | 37.3255 | 10.8948 | 20.3875 | 33.3014 |
| LED large | 37.9472 | 11.3138 | 20.5557 | 33.8336 |

## Generating a summary

Load the selected checkpoint with `AutoTokenizer` and `AutoModelForSeq2SeqLM`, tokenize the paper text, generate a sequence, and decode it. The [Transformers LED documentation](https://huggingface.co/docs/transformers/en/model_doc/led) recommends global attention on the first input token for summarization and padding inputs on the right.

The saved configurations specify four-beam generation, a minimum length of 100, a maximum length of 512, and a three-token repetition constraint. These are generation settings, separate from the encoder's 16,384-token capacity. Set input truncation and output length deliberately when adapting the models to a collection. Extract text from PDFs before tokenization; document images and page layout are not model inputs.

Both releases specify Apache 2.0 licensing. Their published scores describe this arXiv evaluation setting; the cards do not establish performance across other scientific domains or languages.
