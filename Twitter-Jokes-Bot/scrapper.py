#!/usr/bin/python3.6

"""
                --- Web Scrapper ---
This module when executed, scrappes the defined website for jokes and stores them in a list in jokes.py.
When the list becomes empty, i;e all the jokes are posted, this script is automatically executed and stores
the  jokes in the list.
"""

import bs4 as bs
import urllib.request
import re
import config
import url
import time

# Link to be parsed
URL = url.getUrl(3)

# Fake user agaent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

# List stores all the parsed text
all_content = []

# Function to extract jokes from the current page
def parsePage():
    
    request = urllib.request.Request(URL, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)

    # Bs4 Object
    soup = bs.BeautifulSoup(response, 'lxml')
    for div in soup.find_all('div', class_ = 'post-text'):
        #print(str(div.text))
        all_content.append(str(div.text))

# Find the maximum number of pages in the url
def findMaxPages():
    request = urllib.request.Request(URL, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)

    # Bs4 Object
    soup = bs.BeautifulSoup(response, 'lxml')
    pages = []
    for div in soup.find_all('span', class_ = 'item'):
        pages.append(int(div.text))
    maxPages = pages[-1]
    print("Max pages: " + str(maxPages))
    return maxPages



parsePage()

currentPage = 2
maxPages = findMaxPages()

resetUrl = URL
URL += "/page"

# Looping each page and parsing content
while currentPage <= maxPages:
    URL += "/"+str(currentPage)
    parsePage()
    URL = URL.split("/")
    del URL[-1]
    URL = "/".join(URL)
    currentPage += 1


print("all content is stored in this list")
print(all_content)
