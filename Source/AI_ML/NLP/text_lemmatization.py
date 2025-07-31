# Lemmatization is the process of reducing words to their base or root form (called a lemma), while ensuring the result is a valid word.
# For example,
# am, are, is → be
# running, ran → run
# better → good

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("running", pos="v"))  # Output: 'run'
print(lemmatizer.lemmatize("better", pos="a"))   # Output: 'good'
