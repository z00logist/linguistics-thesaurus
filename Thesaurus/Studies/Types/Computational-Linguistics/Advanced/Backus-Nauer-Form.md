# Backus-Naur Form (BNF)

Backus-Naur Form is a formal way to specify the syntax of programming and formal languages. It defines the structure of valid sentences in a language and is an essential tool in compiler design and formal language theory.

## Purpose of BNF

- Defines the syntax of a language in a concise and precise way.
- Helps in developing parsers for programming languages.
- Describes programming languages, query languages, and protocols with clarity.

## Components

1. Non-terminals represent elements of the language, such as expressions or statements, and are typically enclosed in angle brackets (e.g., `<expression>`).
2. Terminals are the actual tokens or symbols in the language, such as keywords or literals.
3. Production rules explain how non-terminals can be formed using terminals and other non-terminals.
4. The start symbol is the initial non-terminal from which the language's valid sentences can be generated.

## BNF Syntax

- A rule starts with a non-terminal, followed by `::=`, and then a sequence of terminals and non-terminals.
- The `|` symbol separates alternatives, indicating that any of the options can be chosen.
- Non-terminals can reference themselves, creating recursive structures.

### Simple Example

<expression> ::= <term> | <expression> "+" <term> <term> ::= <factor> | <term> "*" <factor> <factor> ::= <number> | "(" <expression> ")" <number> ::= "0" | "1" | "2" | ... | "9"

This statement defines a language for arithmetic expressions with addition and multiplication.

## Extended BNF (EBNF)

Extended BNF (EBNF) includes additional symbols, such as:

- **`[ ... ]`**: Denotes optional elements.
- **`{ ... }`**: Denotes repetition (zero or more times).
- **`( ... )`**: Groups elements for readability.

### EBNF Example

An EBNF for the same arithmetic expressions as above:

<expression> ::= <term> { "+" <term> } <term> ::= <factor> { "*" <factor> } <factor> ::= <number> | "(" <expression> ")" <number> ::= "0" | "1" | "2" | ... | "9"


## Additional Resources

- [Backus-Naur Form - Wikipedia](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
- [Short Intro to BNF](https://www.youtube.com/watch?v=MMxMeX5emUA)

## Sources

- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools*. Pearson.
- Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation*. Pearson.

---

[Back to Computational Linguistics](../README.md)
