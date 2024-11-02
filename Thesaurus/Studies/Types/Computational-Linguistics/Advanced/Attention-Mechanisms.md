# Attention Mechanisms

Attention mechanisms allow models to focus on specific parts of the input when generating each part of the output, improving performance on tasks where context is important.

## Concepts

- **Alignment**: Calculating the relevance between input and output elements.
- **Context Vector**: Weighted sum of input features, where weights are determined by attention scores.
- **Self-Attention**: Mechanism where attention is applied within a single sequence.

## Types

- **Additive Attention**: Uses a feedforward network to compute attention weights.
- **Multiplicative (Dot-Product) Attention**: Computes the similarity between queries and keys via dot product.


## Related Topics

- [Neural Networks in NLP](Neural-Networks-in-NLP.md)
- [Transformers](Transformers.md)
- [Large Language Models](Large-Language-Models.md)

## External Links

- [Attention Mechanisms in NLP](https://medium.com/syncedreview/a-brief-overview-of-attention-mechanism-13c578ba9129)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

## References

- Bahdanau, D., Cho, K., & Bengio, Y. (2015). "Neural Machine Translation by Jointly Learning to Align and Translate." *Proceedings of the International Conference on Learning Representations*.
- Vaswani, A., et al. (2017). "Attention is All You Need." *Advances in Neural Information Processing Systems*, 5998–6008.

---

[Back to Computational Linguistics](README.md)
