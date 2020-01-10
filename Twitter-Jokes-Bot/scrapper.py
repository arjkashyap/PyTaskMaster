#!/usr/bin/python3.6

"""
                --- Web Scrapper ---
This module when executed, scrappes the defined website for jokes and stores them in a list in jokes.py.
When the list becomes empty, i;e all the jokes are posted, this script is automatically executed and stores
the  jokes in the list.
"""

import bs4 as bs
import config
import urllib
import re


