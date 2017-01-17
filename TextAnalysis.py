# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:20:43 2017

@author: Hüseyin
"""

from SentimentAnalysis import download_all_tweets
import textblob as tb
from textblob.sentiments import NaiveBayesAnalyzer


analyzer = NaiveBayesAnalyzer()
screen_name = input("Enter the screen name of the user you want to analyze: ")
user = screen_name
all_tweets= []
all_tweets = download_all_tweets(user)
sentiment_score_pos = 0
sentiment_score_neg = 0
for tweet in all_tweets:
    blob = tb.TextBlob(tweet.text, analyzer= analyzer)
    sentiment_score_pos += float(blob.sentiment.p_pos)
    sentiment_score_neg += float(blob.sentiment.p_neg)
    
print(sentiment_score_pos)
print(sentiment_score_neg)
