# BLEU Score

The BLEU (Bilingual Evaluation Understudy) score is a metric for evaluating the quality of text that has been machine-translated from one language to another. It compares the candidate translation against one or more reference translations and measures the correspondence of n-grams.

## Calculation

The BLEU score is calculated using the formula:

BLEU = BP * exp(Σ (w_n * log(p_n)) for n=1 to N)

Where:
- **BP** is the brevity penalty.
- \( p_n \) is the precision for n-grams.
- \( w_n \) is the weight assigned to each n-gram.

## Why It’s Used

The BLEU score is mainly used for:
- Evaluating machine translation by checking how closely the generated text matches human reference translations.
- Assessing text generation models, like those used for summarization, although the ROUGE score is often preferred for that specific task.

## Additional Resources

- [BLEU Score - Wikipedia](https://en.wikipedia.org/wiki/BLEU)
- [BLEU Article](https://aclanthology.org/P02-1040.pdf)

---

[Back to Evaluation and Metrics](README.md)
