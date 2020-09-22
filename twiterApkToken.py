import os
#import flask
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
from os.path import join, dirname
from dotenv import load_dotenv
import sys
#app = flask.Flask(__name__)

dotenv_path = join(dirname(__file__), 'tweet.env')
load_dotenv(dotenv_path)

consumer_key=os.environ["KEY"]
consumer_secret=os.environ["KEY_SECRET"]
access_token=os.environ["TOKEN"]
access_token_secret=os.environ["TOKEN_TOKEN"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



auth_api = API(auth)
account_list = "@Spotify "
user = auth_api.get_user(account_list)
screen_name = user.screen_name
user_name = user.name
description = user.description
user_tweets = auth_api.user_timeline(account_list)
end_date = datetime.now() - timedelta(days=30)
tweet_list = []
tweet_time = []
for twitt in user_tweets:
  if twitt.created_at < end_date:
    break
  tweet_list.append(twitt.text)
  tweet_time.append(twitt.created_at)
  
  list_len = len(tweet_list)
  time_len = len(tweet_time)
  for i in range(0,list_len):
    print(twitt.text)
    print(twitt.created_at)
    print(screen_name)
    print(user_name)
    print(description)
    print(tweet_list[i])
    print(tweet_time[i])
    