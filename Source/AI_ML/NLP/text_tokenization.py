
# Tokenization is the process of breaking text into smaller units, usually words or sentences.
# Word Tokenization: Break into words
# Sentence Tokenization: Break into sentences
# Character Tokenization: Break into individual characters

from nltk.tokenize import word_tokenize

text = "NLP is fun!"
tokens = word_tokenize(text)
print(tokens)  # Output: ['NLP', 'is', 'fun', '!']
