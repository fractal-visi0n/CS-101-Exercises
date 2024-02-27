import tweepy
import os
from tweepy import OAuthHandler
import re

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user1 = raw_input('Give me User1: ')
tweets1 = api.user_timeline(screen_name=user1, count=10)
while len(tweets1) < 10:
	print 'User', user1, 'has less than 10 tweets. Please select another one.'
	user1 = raw_input('Give me User1: ')
	tweets1 = api.user_timeline(screen_name=user1, count=10)

user2 = raw_input('Give me User2: ')
tweets2 = api.user_timeline(screen_name=user2, count=10)
while len(tweets1) < 10:
	print 'User', user1, 'has less than 10 tweets. Please select another one.'
	user1 = raw_input('Give me User1: ')
	tweets1 = api.user_timeline(screen_name=user1, count=10)

regex = r"[^a-zA-Z0-9]"

sum1 = 0
for t in tweets1:
	sum1 += len(re.split(regex, t.text))

sum2 = 0
for t in tweets2:
	sum2 += len(re.split(regex, t.text))

print
if sum1 > sum2:
	print user1, 'has more words in his last ten tweets' 
elif sum1 < sum2:
	print user2, 'has more words in his last ten tweets'
else:
	print 'It\'s a draw!'