# Word2Vec

Word2Vec is a group of related models that produce word embeddings using shallow neural networks. Developed by Tomas Mikolov and colleagues at Google in 2013, it includes two architectures: Continuous Bag-of-Words (CBOW) and Skip-Gram.

## Architectures

### Continuous Bag-of-Words (CBOW)

- **Objective**: Predict the target word based on surrounding context words.
- **Input**: Context words (surrounding words).
- **Output**: Target word.
- **Characteristics**: Faster to train, better for frequent words.

### Skip-Gram

- **Objective**: Predict surrounding context words given the target word.
- **Input**: Target word.
- **Output**: Context words.
- **Characteristics**: Performs better with infrequent words.

## Key Features

- **Efficiency**: Can be trained on large datasets quickly.
- **Semantic Relationships**: Captures linear relationships between words (e.g., "king" - "man" + "woman" ≈ "queen").
- **Dimensionality**: Typically uses 100-300 dimensions.


## Related Topics

- [Word Embeddings](Word-Embeddings.md)
- [Neural Networks in NLP](../Neural-Networks-in-NLP.md)
- [GloVe](GloVe.md)

## External Links

- [Word2Vec Explained](https://towardsdatascience.com/word2vec-explained-49c52b4ccb71) (Towards Data Science)
- [Gensim Word2Vec Tutorial](https://radimrehurek.com/gensim/models/word2vec.html)

## Sources

- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space." *arXiv preprint arXiv:1301.3781*.
- Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). "Distributed Representations of Words and Phrases and their Compositionality." *Advances in Neural Information Processing Systems*, 26, 3111–3119.

---

[Back to Word Embeddings](README.md)
