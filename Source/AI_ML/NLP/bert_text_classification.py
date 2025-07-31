# BERT for text classification
# BERT model to classify text as positive or negative sentiment (binary classification).

from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Load BERT sentiment analysis pipeline (binary classification)
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Example text
result = classifier("This product is amazing! I love it.")
print(result)
