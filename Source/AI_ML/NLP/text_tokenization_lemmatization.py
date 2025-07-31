# Tokenization	Break text into units (words/sentences)
# Lemmatization	Reduce words to meaningful base forms

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

text = "Cats are running faster than the mice."
tokens = word_tokenize(text)
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token.lower(), pos="v") for token in tokens]
print("Tokens:", tokens)
print("Lemmatized:", lemmatized)

