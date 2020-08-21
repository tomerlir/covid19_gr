import tweepy
import time
from os import environ


class ReplyBot:
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

        FILE_NAME = 'last_seen.txt'

        def read_last_seen(FILE_NAME):
            file_read = open(FILE_NAME, 'r')
            last_seen_id = int(file_read.read().strip())
            file_read.close()
            return last_seen_id

        def store_last_seen(FILE_NAME, last_seen_id):
            file_write = open(FILE_NAME, 'w')
            file_write.write(str(last_seen_id))
            file_write.close()
            return

        def reply():
            tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
            for tweet in reversed(tweets):
                print(str(tweet.id) + ' - ' + tweet.full_text)
                api.update_status("@" + tweet.user.screen_name + " Thanks for the mention", tweet.id)
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                store_last_seen(FILE_NAME, tweet.id)

        while True:
            reply()
            time.sleep(15)
