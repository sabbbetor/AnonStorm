#!/usr/bin/python2.7
# AnonStorm twitterstorm bot
#
# Updated version v2 by sabbbet for @StopICMS only
# This version uses tweepy as the older version uses old twitter API.
# This version also handles multiple accounts efficiently.
#
# This script, as it sits will pull from an online file.
# It will pull a random tweet from the hosted file, and tweet every 2 minutes a new random tweet.
# 
# You MUST run the auth.py script first to obtain your access_token_key and your access_token_secret. This will authorize the app with your twitter account.
# Once you verify the pin, auth.py automatically updates the appropriate strings access_token_key and access_token_secret in TOKENS_SECRETS.conf.
# You can run auth.py for as many accounts you want to use the storm for.
#
#
# A VERY special thanks to The, Happyface, Prophet and kyzersane for their work on its original script.
#
#
# Version 2.0

import time, datetime, sched, random
import urllib2
import tweepy
import sys
import re

print('\n Welcome to AnonStorm v2.0 | This is developed for @StopICMS only, Happy Tweeting!')

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY='5VuZ39FbuRfFdr0CpNf3zg'
CONSUMER_SECRET='5FPi40pwS3buTMFMXm8URXoRSCubw0LqM5KtTPkdo'

print '\n Getting ACCESS_TOKEN_KEY and ACCESS_TOKEN_SECRET of multiple accounts. from TOKENS_SECRETS.txt'

file_read = open("TOKENS_SECRETS.conf","rU")
lines = file_read.read()
matches = re.findall(r'KEY = ([\w\-\w]+) SECRET = ([\w\-\w]+)',lines)
looper = len(matches)
if looper == 0:
    print "\n\n\n You will have to run auth.py so that it can store your ACCESS_TOKEN_KEY and ACCESS_TOKEN_SECRET of one or more accounts in TOKENS_SECRETS.conf file."
    print "\n This is done in order to use multiple account at once for a better storm."
    print "\n You can run auth.py for as many accounts you want to use the storm for."
    print "\n\n\n GoI beware, a storm is comming!"
    sys.exit(1)
loopy = 0

contents = []
s  = sched.scheduler(time.time, time.sleep)

stat = ""
LINK_TO_OP_TWEET_FILE = "http://pastebin.com/raw.php?i=hmW17JgF"

def tweet(sc):
    global stat, loopy, looper, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    response = urllib2.urlopen(LINK_TO_OP_TWEET_FILE)
    contents = response.readlines()
    stat = contents[random.randrange(0,len(contents))]
    status = stat[:-2]
    loopy = looper

    while True:
        while loopy > 0:
            for keys_ in matches:
                try:
                    ts = time.time()
                    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    if len(status) > 140:
                        print '\nThis [',status[:20],'...',status[-20:],'] Tweet has more than 140 characters! \n\n Please contact the owner of the paste, TheDentist on #opindia at anonops.\n'
                        stat = contents[random.randrange(0,len(contents))]
                        status = stat[:-2]
                    else:
                        ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET = keys_
                        print "\n Tweeting ... for account", loopy
                        print "\tat", st
                        stat = contents[random.randrange(0,len(contents))]
                        status = stat[:-2]
                        print "", status
                        loopy = loopy - 1
                        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
                        api = tweepy.API(auth)
                        result = api.update_status(status)
                except tweepy.error.TweepError as e:
                    print "\nTwitter error received...", e.message
                    print "Trying again..."
                    stat = contents[random.randrange(0,len(contents))]
        break
        if loopy == 0:
            loopy = looper

       
    sc.enter(120, 1, tweet, (sc,)) #Edit the "120" if you wish to speed or slow down the tweets. Time is in seconds. IE: 120 = 2 minutes

s.enter(0, 1, tweet, (s,))
s.run()

