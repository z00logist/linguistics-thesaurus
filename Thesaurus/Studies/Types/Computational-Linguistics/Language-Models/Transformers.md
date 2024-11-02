# Transformers

Transformers are neural network architectures that rely entirely on self-attention mechanisms and dispense with recurrence and convolution. Introduced by Vaswani et al. (2017), they have become foundational in NLP.

## Key Components

- **Self-Attention**: Allows the model to weigh the relevance of different words in a sequence.
- **Positional Encoding**: Adds information about the position of words in the sequence.
- **Encoder-Decoder Structure**: Consists of stacked layers of encoders and decoders.

## Advantages

- **Parallelization**: Enables faster training by processing sequences in parallel.
- **Long-Range Dependencies**: Better at capturing relationships between distant words.
- **State-of-the-Art Performance**: Forms the basis of models like BERT and GPT.


## Notable Models

- **BERT (Bidirectional Encoder Representations from Transformers)**: Pre-trained on large corpora for downstream tasks.
- **GPT (Generative Pre-trained Transformer)**: Focuses on language generation tasks.
- **T5 (Text-to-Text Transfer Transformer)**: Unified framework for various NLP tasks.

## Related Topics

- [Attention Mechanisms](Attention-Mechanisms.md)
- [Neural Networks in NLP](Neural-Networks-in-NLP.md)
- [Large Language Models](Large-Language-Models.md)

## External Links

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Transformers - Hugging Face](https://huggingface.co/transformers/)

## References

- Vaswani, A., et al. (2017). "Attention is All You Need." *Advances in Neural Information Processing Systems*, 5998–6008.
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics*, 4171–4186.

---

[Back to Computational Linguistics](README.md)
