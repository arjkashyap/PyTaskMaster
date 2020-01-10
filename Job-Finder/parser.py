#!/usr/bin/python3.6

"""
Web parser to collect job listing on basis of attributes 
recieved via the GUI
Usage:
    Run the following command
    ./scraper.py > jobs.txt
    To get a list of all the job listings undre computer science departement

    Results can be filtered using the grep command:
    
    Suppose I am looking for a job in Mumbai:
    Run: ./scrapper.py > jobs.txt
    Run: grep -i "mumbai" ./jobs.txt
"""

import bs4 as bs
import urllib.request
import re
import url

# Site link
URL = url.getUrl()

# Fake user agent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

request = urllib.request.Request(URL, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)

# Bs4 object
soup = bs.BeautifulSoup(response, 'lxml')


# Traverse through each job description to find the title
def findTitle(desc):
    res = []
    tmp = desc.split()
    for item in tmp:
        if item == "Location(s):":
            break
        else:
            res.append(item)
    return " ".join(res)

# Traverse through each job to find the locaton
def findLocation(desc):
    res = []
    tmp = desc.split()
    for index in range(tmp.index("Location(s):") + 1, tmp.index("Start")):
        res.append(tmp[index])
    return " ".join(res)

# Function contains Reg ex to find stipend
def findStipend(desc):
    regEx = re.compile(r'\d{4}\d?([-]\d{4}\d?)?')
    mo = regEx.search(desc)
    return mo.group()

# Function contains Reg ex to find the duration
def findDuration(desc):
    regEx = re.compile(r'\d\s(\w)*')
    mo = regEx.search(desc)
    return mo.group()
# Job Texts and Links for each job application portal
texts = []
links = [ tag.get('href') for tag in soup.find_all('a', {'class':'view_detail_button'}) ]
count = 0
for div in soup.find_all('div', class_ = 'internship_meta'):
    txtLst = (str(div.text)) .split()
    texts.append(" ".join(txtLst) )    
    count += 1

# texts contains a list of all the parsed text divs
#print(texts)

linkIndex = 0

# Seperating Variables
for i in texts:
    print("#" + str(linkIndex + 1))
    print( findTitle(i) )
    print("Location: " + str(findLocation(i)) )
    print("Stipend: " + str(findStipend(i)))
    print("Duration: " + str(findDuration(i)))
    print("Link: " + "https://internshala.com" + str(links[linkIndex]))
    linkIndex += 1
    print("\n")
