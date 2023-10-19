# TDT4117 Information Retrieval - Autumn - Norwegian University of Science and Technology

This repository contains Python scripts and documentation for Assignment 3 and Assignment 4 of the TDT4117 Information Retrieval course. The assignments involve various text analysis and indexing tasks.

## Assignment 3: Text Analysis and Retrieval

This part of the project focuses on text analysis and retrieval. It includes the following tasks:

### Text Preprocessing

- Tokenization: The text is split into individual words, and punctuation is removed.
- Stopword Removal: Common stopwords are removed from the text to focus on meaningful content.

### TF-IDF and LSI Analysis

- The script calculates Term Frequency-Inverse Document Frequency (TF-IDF) scores for words in the text.
- Latent Semantic Indexing (LSI) analysis is performed to extract latent topics from the text.

### Information Retrieval

- Users can enter a query, and the script calculates the TF-IDF weights for the query terms.
- The script retrieves and ranks the most relevant documents based on these weights.

### Topic Analysis

- The script also analyzes the most significant topics and relevant paragraphs for a given query, providing insights into the text's content.

## Assignment 4: Text Indexing and Analysis

This part of the project focuses on text indexing and analysis. It includes the following tasks:

### Text Indexing

- The script loads a document and splits it into lines.
- Punctuation is removed, and all letters are made lowercase.
- For an inverted file/list, words are split into tokens, and a dictionary is created where the term has an index corresponding to the line where it's found.
- To create an inverted list with block addressing, the text is split into blocks of 4 words, and a dictionary is created with the term's index corresponding to the block it's assigned.
- Suffix tree analysis views texts as a single long string, uniquely identifying all text positions by their index points.
- Posting inverted lists assign each document in the collection a unique number, creating a dictionary linking terms to the document numbers where they appear.

### Index Analysis Using Lucene

- The script explores index analysis using Lucene.
- Elasticsearch, Logstash, and Kibana (ELK) stack is introduced for log aggregation, analysis, and visualization.
- Each text is divided into words to generate an inverted index. A list of pairs (document id, occurrences) is provided for each term, indicating where the term is found and its frequency.
- A comparison is made between the index implementation and ELK for various queries, and differences in results are discussed.
- The search results for different queries are presented, showing the documents returned for each query.

## Requirements

The scripts in this project require the following Python libraries:

- `random`
- `gensim`
- `string`
- `itertools`
- `re`
- `nltk.stem.porter`

Additionally, you may need to install Elasticsearch, Logstash, and Kibana for Assignment 4, depending on your setup.

## Usage

To use these scripts and explore the assignments, follow these steps:

1. Import the necessary Python libraries and ensure they are installed.
2. Place your text documents in the same directory as the scripts.
3. Run the scripts in your Python environment.

Feel free to explore the assignments, run queries, and analyze text data using the provided scripts.

## Author

The scripts and documentation for these assignments were prepared by Ilias Kalantzis.

## Acknowledgments

The scripts utilize various libraries and techniques for text analysis, information retrieval, and indexing. We acknowledge the authors and contributors of these libraries for their valuable work in the field of natural language processing and information retrieval.

