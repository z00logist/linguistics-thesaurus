# FastText

FastText is a library created by Facebook's AI Research (FAIR) lab for learning word representations and performing sentence classification efficiently. Unlike Word2Vec, FastText includes subword information in its modeling.

## Key Features

FastText models words using character n-grams, allowing it to capture word morphology. This approach enables it to generate embeddings for out-of-vocabulary (OOV) words by combining subword vectors. The library is known for its speed and scalability. FastText excels in handling rare and misspelled words, making it especially useful for morphologically rich languages. It also offers efficient text classification capabilities that are beneficial for various NLP tasks.

## Related Topics

- [Word Embeddings](Word-Embeddings.md)
- [Word2Vec](Word2Vec.md)
- [GloVe](GloVe.md)

## Additional Resources

- [FastText Official Website](https://fasttext.cc/)
- [FastText Tutorial](https://fasttext.cc/docs/en/tutorial.html)

## Sources

- Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). "Enriching Word Vectors with Subword Information." *Transactions of the Association for Computational Linguistics*, 5, 135–146.
- Joulin, A., Grave, E., Bojanowski, P., & Mikolov, T. (2017). "Bag of Tricks for Efficient Text Classification." *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics*, 427–431.

---

[Back to Computational Linguistics](../README.md)
