# FastText

FastText is a library developed by Facebook's AI Research (FAIR) lab for efficient learning of word representations and sentence classification. It extends Word2Vec by considering subword information.

## Key Features

- **Subword Information**: Models words as n-grams of characters, capturing morphology.
- **OOV Words**: Can generate embeddings for out-of-vocabulary words by summing up subword vectors.
- **Efficiency**: Designed to be fast and scalable.

## Advantages

- **Handling Rare Words**: Better representations for rare and misspelled words.
- **Morphological Richness**: Particularly useful for morphologically rich languages.
- **Classification Tasks**: Provides efficient text classification capabilities.

## Applications

- **Text Classification**: Sentiment analysis, topic categorization.
- **Language Modeling**: Improved performance on languages with rich morphology.
- **Machine Translation**: Enhanced word representations.

## Related Topics

- [Word Embeddings](Word-Embeddings.md)
- [Word2Vec](Word2Vec.md)
- [GloVe](GloVe.md)

## External Links

- [FastText Website](https://fasttext.cc/)
- [FastText Tutorial](https://fasttext.cc/docs/en/tutorial.html)

## References

- Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). "Enriching Word Vectors with Subword Information." *Transactions of the Association for Computational Linguistics*, 5, 135–146.
- Joulin, A., Grave, E., Bojanowski, P., & Mikolov, T. (2017). "Bag of Tricks for Efficient Text Classification." *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics*, 427–431.

---

[Back to Word Embeddings](README.md)
