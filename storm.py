# AnonStorm twitterstorm bot
#
# Updated version v1.1 by sabbbet for @StopICMS only
# This version uses tweepy as the older version uses old twitter API.
#
# This script, as it sits will pull from an online file.
# It will pull a random tweet from the hosted file, and tweet every 2 minutes a new random tweet.
# 
# You MUST run the auth.py script first to obtain your access_token_key and your access_token_secret. This will authorize the app with your twitter account.
# Once you verify the pin, you MUST update the appropriate strings access_token_key and access_token_secret with the key and secret auth.py gives you.
#
# A VERY special thanks to The, Happyface, Prophet and kyzersane for their work on its original script.
#
#
# Version 1.1

import time, datetime, sched, random
import urllib2
import tweepy
     
print('Welcome to AnonStorm v1.1 | This is developed for @StopICMS only, Happy Tweeting!')

ACCESS_TOKEN_KEY='YOUR ACCESS TOKEN HERE'
ACCESS_TOKEN_SECRET='YOUR ACCESS SECRET HERE'
CONSUMER_KEY='5VuZ39FbuRfFdr0CpNf3zg'
CONSUMER_SECRET='5FPi40pwS3buTMFMXm8URXoRSCubw0LqM5KtTPkdo'

contents = []
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
s  = sched.scheduler(time.time, time.sleep)

stat = ""
LINK_TO_OP_TWEET_FILE = "http://pastebin.com/raw.php?i=hmW17JgF"

def do_something(sc):
        global stat
        response = urllib2.urlopen(LINK_TO_OP_TWEET_FILE)
        contents = response.readlines()
        stat = contents[random.randrange(0,len(contents))]
        status = stat[:-2]

        while True:
                try:
                    if len(status) > 140:
                        print 'This [',status[:20],'...',status[-20:],'] Tweet has more than 140 characters! \n\n Please contact the owner of the paste, TheDentist on #opindia at anonops.\n'
                        stat = contents[random.randrange(0,len(contents))]
                        status = stat[:-2]
                    else:
                        print "\nTweeting...", st
                        print "", status
                        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
                        api = tweepy.API(auth)
                        result = api.update_status(status)
                        break
                except tweepy.error.TweepError as e:
                        print("\nTwitter error received...", e.message)
                        print("Trying again...")
                        stat = contents[random.randrange(0,len(contents))]
 
        sc.enter(120, 1, do_something, (sc,)) #Edit the "120" if you wish to speed or slow down the tweets. Time is in seconds. IE: 120 = 2 minutes
 
s.enter(0, 1, do_something, (s,))
s.run()

