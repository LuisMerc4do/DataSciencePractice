import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

#Download Packaging to use NLTK
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("vader_lexicon")

# Unstructured data
post = "This smartphone is so bad, i hate it"

# Converting the post into tokens
tokens = word_tokenize(post)
print(f"Tokens: {tokens}")

# Calling the token analyzer and calculate sentiment intensity
sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(post)
print(f"Sentiment Score: {sentiment_score}")

