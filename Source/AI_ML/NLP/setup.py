# Natural language toolkit
# pip uninstall nltk
# pip install --no-cache-dir nltk

# pip install transformers
# pip install torch

import nltk
print(nltk.__version__)

nltk.download('punkt')        # For tokenization
nltk.download('punkt_tab')
nltk.download('wordnet')      # For lemmatization
nltk.download('omw-1.4')      # (Optional) WordNet lemmatizer support
nltk.download('averaged_perceptron_tagger')  # (Optional) POS tagging