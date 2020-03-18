#!/usr/bin/python3.6

"""
        --- Get Latest Data on Positive Cases ---
This module scraps the site: https://www.mohfw.gov.in/ for positive cases of corona virus
and stores them in a csv file. Multiple files are made to keep a track how fast the virus
spreads througout various states in India

"""

import bs4 as bs
import urllib.request
import re
from datetime import date
import csv


# Function returns 2d array of confirmed cases in each state
def current_data():
    data = []
    URL = "https://www.mohfw.gov.in/"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    request = urllib.request.Request(URL, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)

    # BS4 object
    soup = bs.BeautifulSoup(response, 'lxml')

    # Data table
    table = soup.find('table')
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [r.text for r in td]
        data.append(row)
    del data[0]
    for i in data:
        print(i)
    print("Data Scrap: complete")
    return data


# Create csv file of current data parsed
def create_csv(data):
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")
    file_name = current_date + ".csv"

    # Write headers
    with open(file_name, 'w') as f:
        w = csv.writer(f)
        header = ['label', 'state', 'indian_confirmed', 'foreign_confirmed', 'cured', 'death']
        w.writerow(header)

        for row in data:
            w.writerow(row)
    print("File write Complete")

create_csv(current_data())


