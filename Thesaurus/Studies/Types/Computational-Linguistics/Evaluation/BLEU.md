# BLEU Score

The BLEU (Bilingual Evaluation Understudy) score is a metric for evaluating the quality of text that has been machine-translated from one language to another. It compares the candidate translation against one or more reference translations and measures the correspondence of n-grams.

## Calculation

The BLEU score is calculated using the formula:

\[
\text{BLEU} = \text{BP} \cdot \exp\left(\sum_{n=1}^N w_n \log p_n\right)
\]

Where:
- **BP** is the brevity penalty.
- \( p_n \) is the precision for n-grams.
- \( w_n \) is the weight assigned to each n-gram.

## Purpose

- **Machine Translation Evaluation**: Measures how similar the generated translation is to the reference.
- **Text Generation Assessment**: Used in evaluating models that generate text, such as summarization models.

## External Links

- [BLEU Score - Wikipedia](https://en.wikipedia.org/wiki/BLEU)
- [BLEU Article](https://aclanthology.org/P02-1040.pdf)

---

[Back to Evaluation and Metrics](README.md)
