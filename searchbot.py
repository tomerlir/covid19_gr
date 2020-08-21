import time
import tweepy
from os import environ


class SearchBot:
    def __init__(self):
        CONSUMER_KEY = environ['CONSUMER_KEY']
        CONSUMER_SECRET = environ['CONSUMER_SECRET']
        ACCESS_KEY = environ['ACCESS_KEY']
        ACCESS_SECRET = environ['ACCESS_SECRET']
        
        def OAuth():
            try:
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                return auth
            except tweepy.TweepError as e:
                return e.reason

        oauth = OAuth()
        api = tweepy.API(oauth)

        hashtag = '#Covid19gr'
        nrTweets = 5
        tweets = tweepy.Cursor(api.search, hashtag).items(nrTweets)

        def searchBot():
            for tweet in tweets:
                try:
                    tweet.favorite()
                    print('Tweet liked Successfully')
                    time.sleep(5)
                except tweepy.TweepError as e:
                    print(e.reason)
                    time.sleep(2)

        searchBot()
