# N-gram Models

N-gram models are probabilistic language models that predict the next item in a sequence based on the n-1 previous items. They are foundational in computational linguistics for tasks like speech recognition and text prediction.
  An n-gram is a contiguous sequence of n items from a given sample of text or speech:

- **Unigram (n=1)**
- **Bigram (n=2)**
- **Trigram (n=3)**

## Probability Estimation

The probability of a word given the previous words:

**P(wₙ | wₙ₋₁, wₙ₋₂, ..., wₙ₋₍ₙ₋₁₎)**

In bigram models:

**P(w₂ | w₁) = Count(w₁ w₂) / Count(w₁)**

## Related Topics

- [Probabilistic Models](Probabilistic-Models.md)
- [Language Modeling](Language-Modeling.md)
- [Neural Networks in NLP](Neural-Networks-in-NLP.md)

## Additional Resources

- [N-gram Models - Wikipedia](https://en.wikipedia.org/wiki/N-gram)
- [Language Modeling Tutorial](https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf) (Stanford)

## Sources

- Jurafsky, D., & Martin, J. H. (2020). *Speech and Language Processing*. Prentice Hall.
- Manning, C. D., & Schütze, H. (1999). *Foundations of Statistical Natural Language Processing*. MIT Press.

---

[Back to Computational Linguistics](../README.md)
