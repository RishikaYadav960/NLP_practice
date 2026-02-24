from textblob import TextBlob

text = "I enjoy learning NLP"
analysis = TextBlob(text)

print("Polarity:", analysis.sentiment.polarity)