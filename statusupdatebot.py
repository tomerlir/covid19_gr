import bs4
import requests
import tweepy
from os import environ


class StatusUpdateBot:
    def __init__(self):
        res = requests.get('https://www.worldometers.info/coronavirus/country/greece/')
        soup = bs4.BeautifulSoup(res.text, "lxml")
        newPost = soup.select('.news_post')
        tweetToPost = newPost[0].getText().replace('[source]', '')
        tweetToPost = tweetToPost.replace('\"', '')
        print(tweetToPost)  # Works in getting the proper text

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

        def updateStatus():
            api.update_status(tweetToPost + " #covid19gr #covid19greece #coronavirusgreece #GreeceNews")
            print("Tweet has been successfully posted")

        updateStatus()
