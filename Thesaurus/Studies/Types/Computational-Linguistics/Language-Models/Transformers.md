# Transformers

Transformers are a type of neural network architecture that use self-attention mechanisms and do not rely on recurrence or convolution. First introduced by Vaswani et al. in 2017, they have become a cornerstone in the field of NLP.

## Components of Transformers

Transformers include several important features:
- Self-attention allows the model to assign importance to different words within a sequence.
- Positional encoding provides the model with information about the order of words in a sequence.
- The architecture includes an encoder-decoder structure, built from multiple stacked layers.

Transformers Architecture:  
![transformer](../../../../assets/transformer.png)

## Why They Are Effective

Transformers offer significant advantages:
- They support parallelization, enabling faster training by processing entire sequences at once.
- They are effective at capturing long-range dependencies between words, improving their understanding of context.
- Transformers have set the benchmark for state-of-the-art performance and are the foundation for models like BERT and GPT.

## Examples of Notable Models of Transformers Architecture

Several well-known models are based on the transformer architecture:
- BERT (Bidirectional Encoder Representations from Transformers) is pre-trained on large text corpora and fine-tuned for various NLP tasks.
- GPT (Generative Pre-trained Transformer) is designed with a focus on generating human-like text.
- T5 (Text-to-Text Transfer Transformer) provides a unified approach to handling a wide range of NLP tasks using a text-to-text format.

## Additional Resources

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Transformers on Hugging Face](https://huggingface.co/transformers/)

## Sources

- Vaswani, A., et al. (2017). "Attention is All You Need." *Advances in Neural Information Processing Systems*, 5998–6008.
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics*, 4171–4186.

---

[Back to Computational Linguistics](../README.md)
