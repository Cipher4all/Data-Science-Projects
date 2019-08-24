#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tweepy
from textblob import TextBlob
#copy keys and tokens from twitter api
consumer_key = 'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'

access_token = 'ACCESS_TOKEN_HERE'
access_secret = 'ACCESS_SECRET_HERE'

#authorize or login on twitter using auth function
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#retrieveing the tweets
public_tweets = api.search('kashmir')

for tweet in public_tweets:
    print(tweet.text)
    
    #perform sentiment analysis on tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")


# In[ ]:




