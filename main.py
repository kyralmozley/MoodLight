#!/usr/bin/env python
from statistics import mode

import tweepy
import config
import helper
import sentiment
import hue_control

#---------------------------
# Authorise API
#---------------------------
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token_key
access_token_secret = config.access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#---------------------------
# Get Trending
#---------------------------

trends1 = api.trends_place(23424975) #uk code
trends = set([trend['name'] for trend in trends1[0]['trends']])
print(trends)
trendsEmotions = []

#find tweets with trending #
for trend in trends:

    #directory of emotions
    emotions = {
        'anger': 0, 'fear': 0, 'anticipation': 0, 'surprise': 0, 'sadness': 0, 'joy': 0, 'disgust': 0,
        'negative': 0, 'positive': 0
    }

    search_results = api.search(q=trend + '-filter:retweets', count=10, lang='en')
    for tweet in search_results:
        #clean tweet, get sentiment, add it to emotion
        text = tweet.text
        text = helper.clean_tweet(text)
        emotion = sentiment.getSentiment(text)
        if not emotion == '':
            emotions[emotion] = emotions.get(emotion) + 1
    trendsEmotions.append(max(emotions, key=emotions.get)) #emotion with most tweets wins

#change colour of hue
hue_control.controlHue(mode(trendsEmotions))
