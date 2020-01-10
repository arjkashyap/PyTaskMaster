#!/usr/bin/python3.6

"""
Simply returns the link to the website to be parsed.
This link can be appended with various catogaries such as:
    animal-jokes
    dirty-jokes
    disabled-jokes
    general-jokes
    political-jokes
Refer full list for option
Based on the parameter given to the function, joke catogary will be changed accordingly
"""


lst = ["", "animal-jokes", "dirty-jokes", "disabled-jokes", "hilarious-jokes", "pick-up-lines", "pick-up-lines", "political-jokes", "racist-jokes", "racist-jokes", "relationship-jokes", "religious-jokes"]


# Pass the list index as a parameter to return url with selected catagory
def getUrl(cat):
    url = "http://www.funnyshortjokes.com/"+lst[cat]
    return url

