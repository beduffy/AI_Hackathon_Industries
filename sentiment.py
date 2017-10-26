from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def process_sentiment(text):

    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

    #print(blob.sentiment)

    return blob.sentiment
