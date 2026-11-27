# Applied AI Intensive Class

A 140-day intensive class in applied AI: from data up to an open language model served locally. Theory first, one page a day, a consolidation project every 7 to 10 days.

**Site: https://akrambouznad789-cyber.github.io/applied-ai-intensive-class/**

**Progress: 3 days published out of 140.**

Sister class: the [AI Inference Intensive Class](https://github.com/akrambouznad789-cyber/ai-inference-intensive-class), run in parallel, on the same day number. Both classes start from the [home page of the path](https://akrambouznad789-cyber.github.io/roadmap-ia/).

## One day

Each day follows the same order:

1. **Notions**: theory first, through a diagram, a worked numeric example and pseudo-code, then the exact passage of a reference source.
2. **Demo**: an interactive page that shows the idea on a transportation case.
3. **Practice, in my words**: a notebook that redoes the calculation and produces a figure, then what was done and understood, in a few sentences.

## The route

| Phase | Days | Content | Status |
|---|---|---|---|
| 1 · Learning from data | 1 to 8 | loss and gradient descent, cross-entropy, trees and boosting, overfitting, leak-free validation, k-means and PCA | In progress |
| 2 · Neural networks and PyTorch | 9 to 26 | backpropagation, optimizers, tensors, training, regularization, embeddings, convolution, graphs | Upcoming |
| 3 · Language and the Transformer | 27 to 50 | BPE tokenization, attention, Transformer block, training and sampling a small GPT | Upcoming |
| 4 · Using an open LLM locally | 51 to 64 | local execution, prompting, structured outputs, tool calls | Upcoming |
| 5 · Evaluation | 65 to 78 | test sets, LLM as a judge, error analysis, A/B tests and causality | Upcoming |
| 6 · RAG | 79 to 92 | chunking, vector index, hybrid search, grounded answers | Upcoming |
| 7 · Agents | 93 to 112 | agent loop, tools, memory, guardrails, trajectory evaluation | Upcoming |
| 8 · Fine-tuning | 113 to 126 | fine-tuning data, SFT, LoRA and QLoRA, preferences, distributed training and diffusion in miniature | Upcoming |
| 9 · Serving and wrap-up | 127 to 140 | local API, monitoring, security, final project | Upcoming |

## Repository contents

| Folder | Contents |
|---|---|
| `docs/` | The site: the 140-day route, then one page, one notebook and figures per day (`docs/jours/`) |
| `gabarits/` | The template of a day page |
| `style/` | The figure style |
| `outils/`, `tests/` | The checks run on the pages before publishing and the capture of their rendering, with their tests |

## Data

Raw data is not versioned, only small results. Each source is credited on the page of its day.

Layout and demos: the AI assistant. Notebooks, figures and words: Akram; the English translation of his words: the AI assistant.
