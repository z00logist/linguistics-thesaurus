# Bag of Words (BoW)

The Bag of Words model is a simple representation used in natural language processing. It represents text as an unordered collection of words, ignoring grammar and word order but keeping track of word frequency.

## Objective

In the Bag of Words model, each document is represented as a vector that counts word occurrences. The dimensionality of this vector matches the size of the vocabulary. This approach is easy to implement and is widely used for text classification tasks. However, it has limitations, such as ignoring word order and context, leading to a lack of semantics. It can also result in high-dimensional vectors that are often sparse, with most entries being zero.

### Bag of Words Matrix Example

|      Word      | Document 1 | Document 2 | Document 3 |
|:--------------:|:----------:|:----------:|:----------:|
| the            |      2     |      2     |      2     |
| cat            |      1     |      1     |      1     |
| sat            |      1     |      0     |      1     |
| on             |      1     |      0     |      1     |
| mat            |      1     |      0     |      1     |
| dog            |      0     |      1     |      0     |
| barked         |      0     |      1     |      0     |
| at             |      0     |      1     |      0     |
| was            |      0     |      0     |      1     |
| by             |      0     |      0     |      1     |


## Common Enhancements

To improve the Bag of Words model, techniques like TF-IDF (Term Frequency-Inverse Document Frequency) are used to weigh words based on their importance. Dimensionality reduction methods, such as Latent Semantic Analysis (LSA), can also help manage the high dimensionality.

## Additional Resources

- [Bag-of-Words Model on Wikipedia](https://en.wikipedia.org/wiki/Bag-of-words_model)
- [Understanding Bag of Words](https://machinelearningmastery.com/gentle-introduction-bag-words-model/) (Machine Learning Mastery)

## Sources

- Jurafsky, D., & Martin, J. H. (2020). *Speech and Language Processing*. Prentice Hall.
- Harris, Z. S. (1954). "Distributional Structure." *Word*, 10(2-3), 146-162.

---

[Back to Computational Linguistics](../README.md)
