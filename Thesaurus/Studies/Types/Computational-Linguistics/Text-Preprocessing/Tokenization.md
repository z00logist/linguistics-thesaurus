# Tokenization

Tokenization is the process of dividing text into smaller units called tokens. These tokens can be words, characters, or subwords, serving as the basic building blocks for various natural language processing tasks.

## What is Token?

A token is the smallest unit produced by tokenization, which can include words and punctuation. A corpus is a structured set of texts used for language processing. A lexeme refers to a basic unit of meaning that may include different inflected forms. The distinction between type and token is important: "type" refers to unique tokens, while "token" refers to each occurrence.

## Methods and Techniques

### Word Tokenization

This method splits text into individual words using spaces and punctuation as boundaries. Common techniques include:
- Whitespace tokenization, which uses spaces and newline characters to divide text.
- Punctuation-based tokenization, which splits text at punctuation marks.

### Subword Tokenization

Subword tokenization breaks words into smaller units like prefixes, suffixes, or syllables. Techniques include:
- Byte Pair Encoding (BPE), which merges the most frequent pairs of bytes or characters.
- WordPiece, used in models like BERT, which creates a subword vocabulary.
- Unigram Language Model, a probabilistic approach for generating subwords.

### Character Tokenization

Character tokenization splits text into individual characters. This approach is useful for handling languages without clear word boundaries or for managing misspellings.

## Related Topics

- [Natural Language Processing](Natural-Language-Processing.md)
- [Morphology](../../Language/Inner-Structure/Morphology/README.md)
- [Computational Linguistics](README.md)
- [Word Segmentation](Word-Segmentation.md)

## Additional Resources

- [Tokenization on Wikipedia](https://en.wikipedia.org/wiki/Tokenization_(lexical_analysis))
- [Text Preprocessing Techniques](https://www.nltk.org/api/nltk.tokenize.html)
- [Stanford NLP Tokenizer](https://nlp.stanford.edu/software/tokenizer.html)

## Sources

- Jurafsky, D., & Martin, J. H. (2020). *Speech and Language Processing*. Pearson.
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval*. Cambridge University Press.
- Kudo, T. (2018). "Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates." *arXiv preprint arXiv:1804.10959*.

---

[Back to Computational Linguistics](README.md)
