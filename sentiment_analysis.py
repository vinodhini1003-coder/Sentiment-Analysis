from textblob import TextBlob

text = input("Enter a review: ")

analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    sentiment = "Positive"
elif analysis.sentiment.polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Sentiment:", sentiment)
