# Backus-Naur Form (BNF)

Backus-Naur Form (BNF) is a formal notation for specifying the syntax of programming languages and other formal languages. It defines rules and structures for constructing valid sentences in a language and is widely used in compiler design and formal language theory.

## Purpose

- **Syntax Definition**: Provides a concise way to define the syntax of a language.
- **Parser Development**: Used in developing parsers for programming languages.
- **Formal Language Description**: Allows precise description of programming languages, query languages, and protocols.

## Components of BNF

1. **Non-Terminals**: Symbols that represent language elements, such as expressions or statements. Typically written in angle brackets (e.g., `<expression>`).
2. **Terminals**: The actual symbols or tokens (e.g., keywords, literals) that appear in the language.
3. **Production Rules**: Rules defining how non-terminals can be composed of terminals and other non-terminals.
4. **Start Symbol**: The initial non-terminal from which all valid sentences of the language can be derived.

## Syntax of BNF

- **Rule Definition**: Each rule is defined with a non-terminal, followed by `::=`, and then a sequence of terminals and/or non-terminals.
- **Alternation**: Multiple options are separated by a `|` symbol, indicating that one of the options can be chosen.
- **Recursion**: Non-terminals can appear within their own definitions, enabling recursive structures.

### Example

A simple BNF for arithmetic expressions:

<expression> ::= <term> | <expression> "+" <term> <term> ::= <factor> | <term> "*" <factor> <factor> ::= <number> | "(" <expression> ")" <number> ::= "0" | "1" | "2" | ... | "9"

This example defines a language for arithmetic expressions with addition and multiplication.

## Extended BNF (EBNF)

Extended BNF (EBNF) is a variation that includes additional symbols, such as:

- **`[ ... ]`**: Denotes optional elements.
- **`{ ... }`**: Denotes repetition (zero or more times).
- **`( ... )`**: Groups elements for readability.

### EBNF Example

An EBNF for the same arithmetic expressions:

<expression> ::= <term> { "+" <term> } <term> ::= <factor> { "*" <factor> } <factor> ::= <number> | "(" <expression> ")" <number> ::= "0" | "1" | "2" | ... | "9"


## Applications

- **Programming Language Design**: Used to define the grammar of programming languages.
- **Compiler Construction**: Aids in building parsers for language syntax checking.
- **LLM Instruction Design**: BNF structures are increasingly used to instruct large language models by creating format constraints, structured responses, and rule-driven outputs, ensuring consistency and adherence to predefined syntax.
- **Documentation**: Provides clear language rules for users and developers.

## Related Topics

- [LLMs](Large-Language-Models.md)
- [Computational Syntax](Computational-Syntax.md)

## External Links

- [Backus-Naur Form - Wikipedia](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
- [BNF and EBNF](https://www.cs.cmu.edu/~fp/courses/15122-f10/lectures/19-ebnf.pdf)

## References

- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools*. Pearson.
- Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation*. Pearson.

---

[Back to Computational Linguistics](README.md)
