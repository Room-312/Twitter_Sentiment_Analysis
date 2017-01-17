# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:20:43 2017

@author: Hüseyin
"""

from SentimentAnalysis import download_all_tweets
import textblob as tb

screen_name = input("Enter the screen name of the user you want to analyze: ")
user = screen_name
all_tweets= []
all_tweets = download_all_tweets(user)
sentiment_score = 0
for tweet in all_tweets:
    blob = tb.TextBlob(tweet.text)
    sentiment_score += float(blob.sentiment.polarity)
    
avg_polarity = sentiment_score / len(all_tweets)
print(sentiment_score)
print(avg_polarity)