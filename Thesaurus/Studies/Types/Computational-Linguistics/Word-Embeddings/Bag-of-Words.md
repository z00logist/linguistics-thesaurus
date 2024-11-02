# Bag of Words (BoW)

The Bag of Words model is a simplifying representation used in natural language processing where a text is represented as an unordered collection of words, disregarding grammar and word order but keeping multiplicity.

## Characteristics

- **Vector Representation**: Each document is represented as a vector of word counts or frequencies.
- **Vocabulary Size**: The dimensionality of the vector equals the size of the vocabulary.
- **Simplicity**: Easy to implement and use for text classification tasks.

## Applications

- **Text Classification**: Spam detection, sentiment analysis.
- **Information Retrieval**: Document similarity measures.
- **Topic Modeling**: Identifying topics within a corpus.

## Limitations

- **Lack of Context**: Ignores word order and semantics.
- **High Dimensionality**: Can lead to computational inefficiency.
- **Sparsity**: Most entries in the vector are zero.

## Enhancements

- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Weighs words based on their importance.
- **Dimensionality Reduction**: Techniques like Latent Semantic Analysis (LSA).

## Related Topics

- [Word Embeddings](Word-Embeddings/README.md)
- [N-gram Models](../N-gram-Models.md)

## External Links

- [Bag-of-Words Model - Wikipedia](https://en.wikipedia.org/wiki/Bag-of-words_model)
- [Understanding Bag of Words](https://machinelearningmastery.com/gentle-introduction-bag-words-model/) (Machine Learning Mastery)

## References

- Jurafsky, D., & Martin, J. H. (2020). *Speech and Language Processing*. Prentice Hall.
- Harris, Z. S. (1954). "Distributional Structure." *Word*, 10(2-3), 146-162.

---

[Back to Computational Linguistics](README.md)
