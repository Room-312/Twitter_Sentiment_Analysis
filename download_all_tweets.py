
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:58:32 2017
@author: Hüseyin
"""

import tweepy

def download_all_tweets( screen_name ): 
    consumer_key = 'Ch8M3zRiiJkOHjA041jInHlYn'
    consumer_secret = 'UUSHilvM1yuaSnM5fgDhkqikcNXc3nEt5CpxWe6NrrQXBu7UUY'

    access_token = '1055905105-NDWgwwVKsnlDDzFE2K7MctxS7cPzjJmu8honno1'

    access_token_secret = 'MBJ3QCoyQD6qDMxyqg6hngHwAknjTKxYSzONeBp7NMMVA'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    api = tweepy.API(auth)
    allTweets = []
    lastTweetID = 0,


    new_tweets = api.user_timeline(screen_name, count =200)
    allTweets.extend(new_tweets)


    lastTweetID = (allTweets[-1]).id - 1
    print(lastTweetID)

    while (len(new_tweets) > 0):

        new_tweets = api.user_timeline(user,max_id = lastTweetID,count =200)
        allTweets.extend(new_tweets)

        lastTweetID = (allTweets[-1]).id - 1
        print ("...%s tweets downloaded so far" % (len(allTweets)))

    #to see the date of the last tweet
    print(allTweets[-1].created_at)
