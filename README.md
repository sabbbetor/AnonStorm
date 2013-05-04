# Welcome to AnonStorm v2.0
========================================

AnonStorm is a simple TwitterStorm script written in Python.
This tool is to make life easier for participants of activist related twitter storms.
It's design automates your tweets using a hosted text file so you don't have to copy/paste manually.

You will also need to run "auth.py" and allow access of the application to your twitter account,
"auth.py" will give you a URL, copy then paste that URL into your web browser, authorize the application.
Your web browser will then give you a __"Pin Code"__ from twitter, enter this Pin Code into the auth.py script,
The script will then provide you with 2 things, an Access Token Key and an Access Token Secret, these are 
basically encrypted versions of your user name and password. This step better protects you as the script
will not send plaintext information.

You will have to run auth.py first so that it can store your ACCESS_TOKEN_KEY and ACCESS_TOKEN_SECRET key of one or more accounts in TOKENS_SECRETS.conf file.
This is done in order to use multiple account at once for a better storm.
You can run auth.py for all the accounts you have.
When done with auth.py, storm.py will automatically take care of things.

If you have any issues running this application speak to __sabbbet__ in AnonOps IRC.

GoI beware, a storm is comming!


## Cautions 

_Dont use this on a account that you care for._

_Use this bot on an indian twitter account._

## Setup:

### Linux Users

Run the following commands :

* sudo apt-get install python python-dev
* sudo apt-get install python-pip

If you want to run this script in a virtualenv then you could use :
* sudo pip install virtualenv
* virtualenv AnonStorm --distribute (Run this when in the AnonStrom directory to create a virtualenv.)

Then install all the dependencies with :

* sudo pip install -r requirements.txt
  or
* pip install -r requirements.txt (When in an vitualenv)

-------------------------------------------

### Windows Users

Windows user will have to go about it as follows :

> Replace XX with your python version number. Example: Python10, Python27, Python31, etc*

> Read this: https://python-guide.readthedocs.org/en/latest/starting/install/win.html

> Install Python

> Create scripts folder in C:\PythonXX -> "C:\PythonXX\Scripts"

### Pip & Distribute setup

> Save http://python-distribute.org/distribute_setup.py to scripts folder (You do not need virtualenv)

> Set environment variables. Change the system variable "path" and add ";C:\Python27\;C:\Python27\Scripts\"

> Open CMD

> cd C:\PythonXX

> execute easy_install pip

> Let it run the setup and wait for it to finish

### Install dependencies

> execute pip install httplib2

> execute pip install oauth

> execute pip install oauth2

> execute pip install python-twitter

> execute pip install tweepy

----------------------------------------------

### Dependencies

* httplib2==0.8
* oauth==1.0.1
* oauth2==1.5.211
* python-twitter==0.8.7
* tweepy==2.0

--------------------------------------------


__sabbbet__
