#!/usr/bin/python3.6

"""
Web parser to collect job listing on basis of attributes 
recieved via the GUI
"""

import bs4 as bs
import urllib

# Site link
URL = "https://internshala.com/internships/computer%20science-internship"

# Fake user agent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

request = urllib.request.Request(URL, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)

# Bs4 object
soup = bs.BeautifulSoup(response, 'lxml')

# Job Texts and Links for each job application portal
texts = []
links = [ tag.get('href') for tag in soup.find_all('a', {'class':'view_detail_button'}) ]
count = 0
for div in soup.find_all('div', class_ = 'internship_meta'):
    txtLst = (str(div.text)) .split()
    texts.append(" ".join(txtLst) )    
    count += 1

# texts contains a list of all the parsed text divs
print(texts)

# Seperating 
for i in text:
    title = findTitle(i)


