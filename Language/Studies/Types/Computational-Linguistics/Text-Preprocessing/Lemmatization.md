# Lemmatization

Lemmatization is the process of reducing words to their base or dictionary form, known as a lemma, by considering their morphological analysis and context.

## Purpose

- **Canonical Form**: Maps inflected forms to their base form.
- **Contextual Awareness**: Considers the part of speech and meaning.
- **Improved Accuracy**: Provides more accurate base forms compared to stemming.

## Approaches

- **Rule-Based Methods**: Utilize language-specific morphological rules.
- **Dictionary-Based Methods**: Use vocabulary lists to find lemma forms.
- **Statistical Methods**: Employ machine learning to predict lemmas.

## Examples

- **Running** → **Run**
- **Better** → **Good**
- **Studies** → **Study**

## Advantages over Stemming

- **Accuracy**: Produces valid words.
- **Contextual Understanding**: Differentiates between words based on context.

## Limitations

- **Computational Complexity**: More resource-intensive than stemming.
- **Language Dependency**: Requires language-specific resources.

## Related Topics

- [Stemming](Stemming.md)
- [Part-of-Speech Tagging](../Probabilistic-Models.md#part-of-speech-tagging)
- [Text Preprocessing](Text-Preprocessing.md)

## External Links

- [Lemmatization - Wikipedia](https://en.wikipedia.org/wiki/Lemmatisation)
- [SpaCy Lemmatization](https://spacy.io/usage/linguistic-features#lemmatization)
- [Russian Lemmatization](https://pymorphy2.readthedocs.io/en/stable/)

## References

- Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media.

---

[Back to Text Preprocessing](README.md)
