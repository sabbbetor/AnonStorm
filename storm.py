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
import sys
import re

print('\nWelcome to AnonStorm v3.0 | This is developed for @StopICMS only, Happy Tweeting!')

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY='5VuZ39FbuRfFdr0CpNf3zg'
CONSUMER_SECRET='5FPi40pwS3buTMFMXm8URXoRSCubw0LqM5KtTPkdo'

print '\nGetting ACCESS_TOKEN_KEY and ACCESS_TOKEN_SECRET of multiple accounts. from TOKENS_SECRETS.txt'

file_read = open("TOKENS_SECRETS.txt","rU")
lines = file_read.read()

matches = re.findall(r'KEY = ([\w\-\w]+) SECRET = ([\w\-\w]+)',lines)

print matches
looper = len(matches)

contents = []
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
s  = sched.scheduler(time.time, time.sleep)

stat = ""
LINK_TO_OP_TWEET_FILE = "http://pastebin.com/raw.php?i=hmW17JgF"

def tweet(sc):
        global stat, looper, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
        response = urllib2.urlopen(LINK_TO_OP_TWEET_FILE)
        contents = response.readlines()
        stat = contents[random.randrange(0,len(contents))]
        status = stat[:-2]
        loop = looper

        while True:
            while loop != 0:
                for keys_ in matches:
                    print "Generating ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET for your account ... "
                    ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET = keys_
                    loop = loop - 1
                    try:
                        if len(status) > 140:
                            print 'This [',status[:20],'...',status[-20:],'] Tweet has more than 140 characters! \n\n Please contact the owner of the paste, TheDentist on #opindia at anonops.\n'
                            stat = contents[random.randrange(0,len(contents))]
                            status = stat[:-2]
                        else:
                            print "\nTweeting...", st
                            print "", status
                            """
                            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                            auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
                            api = tweepy.API(auth)
                            result = api.update_status(status)
                            """
                            break
                    except tweepy.error.TweepError as e:
                        print("\nTwitter error received...", e.message)
                        print("Trying again...")
                        stat = contents[random.randrange(0,len(contents))]
            sc.enter(60, 1, tweet, (sc,)) #Edit the "120" if you wish to speed or slow down the tweets. Time is in seconds. IE: 120 = 2 minutes



s.enter(0, 1, tweet, (s,))
s.run()

