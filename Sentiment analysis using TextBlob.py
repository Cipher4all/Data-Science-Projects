#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tweepy
from textblob import TextBlob
#copy keys and tokens from twitter api
consumer_key = '50JCszXvz7A0ik1rdgaGR1UmI'
consumer_secret = 'sY4u2EU2xOQU9PYt4lPAzmQjnCNPrZ6NINPe1FsHlTe4qMfJDI'

access_token = '830061358829989888-AANbaMDzDDDUpY7O4bnzNJDq1sVfi4k'
access_secret = 'xR8ZqHpDKJTrbTX9nY2mdYmMhT5a13RlBCx62IvOVuSzg'

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




