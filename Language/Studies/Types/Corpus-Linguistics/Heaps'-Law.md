# Heaps' Law

Heaps' Law describes the relationship between the size of a corpus and the number of unique words (vocabulary size) it contains. It states that as the number of tokens (total words) increases, the number of types (unique words) increases, but at a diminishing rate.

## Formula

The relationship is often expressed as:

**V(N) = K * N^β**

- **V(N)**: Vocabulary size (number of unique words)
- **N**: Total number of words in the corpus
- **K**: Constant (varies by language and corpus)
- **β (beta)**: Typically between 0.4 and 0.6

## Implications

- **Vocabulary Growth**: New unique words continue to appear as more text is added.
- **Non-Finite Vocabulary**: Suggests that vocabulary is theoretically unlimited.
- **Corpus Design**: Important for estimating the required corpus size for studies.

## Comparison with Zipf's Law

- **Zipf's Law**: Describes the frequency distribution of words.
- **Heaps' Law**: Describes the growth of vocabulary size with corpus size.

## Applications

- **Information Retrieval**: Understanding the expected vocabulary size aids in indexing and storage optimization.
- **Language Modeling**: Helps in estimating the coverage of vocabulary in language models.

## Related Topics

- [Frequency Analysis](Frequency-Analysis.md)
- [Zipf's Law](Zipf's-Law.md)
- [Corpus Linguistics](Corpus-Linguistics.md)

## External Links

- [Heaps' Law - Wikipedia](https://en.wikipedia.org/wiki/Heaps%27_law)
- [Statistical Properties of Text](https://nlp.stanford.edu/IR-book/html/htmledition/heaps-law-1.html) (Stanford NLP)

## References

- Heaps, H. S. (1978). *Information Retrieval: Computational and Theoretical Aspects*. Academic Press.
- Baayen, R. H. (2001). *Word Frequency Distributions*. Kluwer Academic Publishers.

---

[Back to Corpus Linguistics](README.md)
