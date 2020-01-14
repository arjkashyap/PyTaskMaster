#!/usr/bin/python3.6

"""
The bot in action..
Takes tweet from the tweet filter and passes it to the twitter and publishes.
Note:
    Please adjust the timeDelays. I recomend lowering it since I developed this 
    bot on a 10 years old laptop with 2 gigs of ram and a poor internet connection.

The file execturion is directed from crontab and set for 9.30 Pm everyday.
Adjust crons according to your needs.


Footnote:
    I am planning to add anther file which will render cron obselete and manage execution accordingly.
    Untlil then, edit your crontab accordingly.
"""

import config
import tweetFilter
import tweepyApi as tw
username = config.username
password = config.pswd

tweet = tweetFilter.finalTweet

tw.makeTweet(tweet)
