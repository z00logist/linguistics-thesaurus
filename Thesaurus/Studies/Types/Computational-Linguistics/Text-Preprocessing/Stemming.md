# Stemming

Stemming is the process of reducing inflected or derived words to their word stem or root form, typically by removing suffixes and prefixes.

## Purpose

- **Simplify Words**: Reduce words to a common base form.
- **Reduce Dimensionality**: Decrease the number of unique tokens.
- **Improve Search and Matching**: Enhance information retrieval and text mining tasks.

## Algorithms

- **Porter Stemmer**: One of the most widely used stemming algorithms.
- **Snowball Stemmer**: An improvement over the Porter Stemmer, supporting multiple languages.
- **Lancaster Stemmer**: An aggressive stemming algorithm, which can sometimes over-stem.

## Examples

- **Running** → **Run**
- **Connection** → **Connect**
- **Studies** → **Studi**

## Limitations

- **Over-stemming**: Different words may be reduced to the same stem erroneously.
- **Loss of Meaning**: The stemmed form may not be a valid word.

## Related Topics

- [Lemmatization](Lemmatization.md)
- [Text Preprocessing](Text-Preprocessing.md)
- [Tokenization](Tokenization.md)

## External Links

- [Stemming - Wikipedia](https://en.wikipedia.org/wiki/Stemming)
- [Porter Stemming Algorithm](https://tartarus.org/martin/PorterStemmer/)

## Sources

- Porter, M. F. (1980). "An Algorithm for Suffix Stripping." *Program*, 14(3), 130–137.

---

[Back to Text Preprocessing](README.md)
