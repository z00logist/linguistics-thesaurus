# Introduction to Linguistics

Welcome to the **Introduction to Linguistics** repository!

This repository is a comprehensive, structured, and detailed resource for students, language enthusiasts, and NLP engineers alike. It covers a wide range of linguistic concepts, structures, and studies, making it a perfect companion for both academic and practical learning. From the intricacies of phonetics to the nuances of computational linguistics, this repository serves as an extensive linguistic thesaurus.

## Why Use This Repository?

- Dive deep into the multiple **subfields** of linguistics, from the **foundational structures** of language to specialized studies.
- Follow an **organized** pathway that takes you through the basics to advanced topics in various areas of linguistics.
- Useful for both **theoretical** linguistics and **applied** fields such as NLP and language processing.

### **Important Note**:
Throughout this repository, you will find links to Wikipedia for additional reference. Enhance your study experience by using the [Wiki-Helper](https://github.com/z00logist/wiki-helper) widget, which allows you to interactively ask questions about Wikipedia articles for in-depth understanding.

## Table of Contents

### 1. [Language](Thesaurus/Language/README.md)
Explore the fundamental elements of language, including its structures, types, and the complex components that form it.

- **[Types of Languages](Thesaurus/Language/Types/README.md)**

  - [Core](Thesaurus/Language/Types/Core/README.md)
    - Major Thesaurus/language classifications based on their grammatical and morphological structures.
  - [Other](Thesaurus/Language/Types/Other/README.md)
    - Unique and special Thesaurus/language types.

- **[Inner Structure](Thesaurus/Language/Inner-Structure/README.md)**
  - [Phonetics](Thesaurus/Language/Inner-Structure/Phonetics/README.md)
    - Explore the sounds of human speech.
  - [Phonology](Thesaurus/Language/Inner-Structure/Phonology/README.md)
    - Understand the systematic organization of sounds.
  - [Morphology](Thesaurus/Language/Inner-Structure/Morphology/README.md)
    - Delve into the structure of words.
    - Study sentence structures and rules.
  - [Semantics](Thesaurus/Language/Inner-Structure/Semantics/README.md)
    - Learn how meaning is constructed in language.

### 2. [Studies](Thesaurus/Studies/README.md)
Explore the various disciplines within linguistics that analyze different aspects of language in use, cognition, and technology.

- **[Types of Studies](Thesaurus/Studies/Types/README.md)**
  - **[Sociolinguistics](Thesaurus/Studies/Types/Sociolinguistics/README.md)**
    - Investigate how language varies and changes across different social groups and contexts.
  - **[Psycholinguistics](Thesaurus/Studies/Types/Psycholinguistics/README.md)**
    - Explore the cognitive processes involved in language acquisition, comprehension, and production.
  - **[Cognitive Linguistics](Thesaurus/Studies/Types/Cognitive-Linguistics/README.md)**
    - Study the relationship between language and the human mind, examining how language reflects cognitive processes.
  - **[Corpus Linguistics](Thesaurus/Studies/Types/Corpus-Linguistics/README.md)**
    - Analyze language data using corpora to uncover patterns and trends in language use.
  - **[Computational Linguistics](Thesaurus/Studies/Types/Computational-Linguistics/README.md)**
    - Learn how computational methods are applied to the analysis and processing of language, covering everything from [Language Models](Thesaurus/Studies/Types/Computational-Linguistics/Language-Models/README.md) to [Text Preprocessing](Thesaurus/Studies/Types/Computational-Linguistics/Text-Preprocessing/README.md).


## Setup and Usage

This repository now includes a comprehensive CLI tool with database integration for advanced linguistic data management and search capabilities.

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- Docker and Docker Compose

### Quick Start

1. **Initialize the project with uv:**
   ```bash
   uv init
   uv sync
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings if needed
   ```

3. **Start the database services:**
   ```bash
   docker-compose up -d
   ```
   This will start:
   - **MongoDB** (port 27017) - Document storage for linguistic content
   - **Weaviate** (port 8080) - Vector database for semantic search
   - **MinIO** (port 9000/9001) - Object storage for assets and media

4. **Run the demo script:**
   ```bash
   ./scripts/demo.sh
   ```
   Or use the CLI directly:
   ```bash
   python main.py --help
   ```

### Available CLI Commands

- `python main.py setup` - Initialize database schemas and storage buckets
- `python main.py ingest <directory>` - Ingest markdown files into the knowledge base
- `python main.py query <criteria>` - Query documents by metadata
- `python main.py semantic-search <query>` - Perform semantic search using embeddings
- `python main.py update <criteria> --updates <changes>` - Bulk update documents
- `python main.py delete <document_id>` - Soft delete documents
- `python main.py undelete <document_id>` - Restore deleted documents

### Database Architecture

- **MongoDB**: Stores structured linguistic content with metadata
- **Weaviate**: Provides vector search capabilities for semantic queries
- **MinIO**: Manages assets like images, diagrams, and media files

### Example Workflows

1. **Semantic Search**: Find content related to specific linguistic concepts
2. **Metadata Queries**: Filter content by tags, difficulty level, or topic
3. **Content Management**: Add, update, or organize linguistic resources
4. **Asset Management**: Store and retrieve multimedia educational content

## Contribution

Contributions to this repository are welcome! If you have suggestions, corrections, or new content to add, please feel free to create a pull request or reach out.


