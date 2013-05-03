# Welcome to AnonStorm v1.1
========================================

AnonStorm is a simple TwitterStorm script written in Python.
This tool is to make life easier for participants of activist related twitter storms.
It's design automates your tweets using a hosted text file so you don't have to copy/paste manually.

## Setup:
------------------------------------------

Run the following commands :

* sudo apt-get install python python-dev
* sudo apt-get install python-pip
* sudo pip install -r requirements.txt

### Dependencies

* httplib2==0.8
* oauth==1.0.1
* oauth2==1.5.211
* python-twitter==0.8.7
* tweepy==2.0

--------------------------------------------

You will also need to run "auth.py" and allow access of the application to your twitter account,
"auth.py" will give you a URL, copy then paste that URL into your web browser, authorize the application.
Your web browser will then give you a __"Pin Code"__ from twitter, enter this Pin Code into the auth.py script,
The script will then provide you with 2 things, an Access Token Key and an Access Token Secret, these are 
basically encrypted versions of your user name and password. This step better protects you as the script
will not send plaintext information.

Once you have your Token information, you will need to edit "storm.py" and enter the Key and Secret
in the spots specified in the script, they are marked as __"YOUR_ACCESS_TOKEN_HERE"__ and __"YOUR_ACCESS_SECRET_HERE"__.

After you have everything set up there, you should have been provided with a link from either The in AnonOps
IRC, or by an operator of your Operation, which will have a link provided by The. You will need to paste that
link in place of __"LINK_TO_OP_TWEET_FILE"__. 

Once those are done, save the storm.py file and fire it up for your twitterstorms!

If you have any issues running this application speak to __sabbbet__ in AnonOps IRC.

Original source of AnonStorm v1.0 - https://github.com/somer4ndompunk/AnonStorm 

__sabbbet__
