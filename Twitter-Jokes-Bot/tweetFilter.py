#!/usr/bin/python3.6

"""
This module will is responsible for filtering twittes which 
are, -- TOO DARK
Selective key words are picked from the from the credentials.py and
matched against the incoming string.
If found, the tweet will be discarded and next tweet will be used.

Secoundly: It will keep maintain a permanent variable in by the name of tweetNum in a seperate file to make sure that tweets do not repeat.
"""

import os
import scrapper
import config

finalTweet = None

def checkTweet(key_words, tweet):
    tweet = tweet.split()
    for key_word in config.denied:
        for tweet_word in tweet:
            if str(key_word) == str(tweet_word):
                return False
    return True

# All the tweets are stored in list named all_content
# Create a file named tweetNum.txt if not present


if not(os.path.isfile("./tweetNum.txt")):
    tweetNumFile = open("tweetNum.txt", "w+")
    tweetNumFile.write("Tweet Index = 1")
    tweetNumFile.close()
    print("Dir setup complete. \nPlease Relaunch the program")
else:
    tweetFile = open("./tweetNum.txt", "r")
    contentLst = tweetFile.read().split()
    tweetIndex = int(contentLst[-1])
    tweet = scrapper.all_content[1]
    
    for tweet in range(tweetIndex, len(scrapper.all_content)):
        if checkTweet(config.denied, scrapper.all_content[tweetIndex]):
            finalTweet = scrapper.all_content[tweetIndex]
            break
    tweetIndex += 1
    tweetNumFile = open("tweetNum.txt", "w")
    tweetNumFile.write("Tweet Index = " + str(tweetIndex))
    tweetNumFile.close()

print(finalTweet)

