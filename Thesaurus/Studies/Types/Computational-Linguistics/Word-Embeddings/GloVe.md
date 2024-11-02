# GloVe

GloVe (Global Vectors for Word Representation) is an unsupervised learning algorithm for generating word embeddings by aggregating global word-word co-occurrence statistics from a corpus.

## Key Features

- **Combines Count-Based and Predictive Methods**: Utilizes the advantages of both methods.
- **Word Co-occurrence Matrix**: Constructs a matrix where each element represents the number of times a word appears in the context of another word.
- **Objective Function**: Minimizes the difference between the dot product of word vectors and the logarithm of the words' probability of co-occurrence.

## Advantages

- **Semantic Relationships**: Captures linear substructures similar to Word2Vec.
- **Performance**: Competitive with or better than Word2Vec on various tasks.
- **Efficiency**: Training is faster for large corpora.

## Applications

- **Natural Language Understanding**: Improving the performance of NLP models.
- **Text Similarity**: Measuring the similarity between texts.
- **Downstream NLP Tasks**: Used as pre-trained embeddings for various applications.

## Related Topics

- [Word Embeddings](Word-Embeddings.md)
- [Word2Vec](Word2Vec.md)
- [Neural Networks in NLP](../Neural-Networks-in-NLP.md)

## External Links

- [GloVe Project Page](https://nlp.stanford.edu/projects/glove/)
- [GloVe Explained](https://medium.com/@sonicboom8/glove-global-vectors-for-word-representation-5a262012210d)

## References

- Pennington, J., Socher, R., & Manning, C. D. (2014). "GloVe: Global Vectors for Word Representation." *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing*, 1532–1543.

---

[Back to Word Embeddings](README.md)
