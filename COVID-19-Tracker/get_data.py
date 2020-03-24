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
from time import sleep
from selenium import webdriver

# Function returns 2d array of confirmed cases in each state
def current_data():
    # Driver for controlling browser
    driver = webdriver.Firefox()
    data = []
    URL = "https://www.mohfw.gov.in/"

    driver.get(URL)
    sleep(3)
    btn = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/strong/div[8]/button")
    btn.click()
    sleep(3)
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    request = urllib.request.Request(URL, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)

    # BS4 object
    soup = bs.BeautifulSoup(response, 'lxml')


    # Data table
    table =soup.select('table')[-1]
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [item.text.strip() for item in cols]
        data.append([item for item in cols if item])
    print(data)
    del data[-1]
    for i in data:
        print(i)
    print("Data Scrap: complete")
    return data


# Create csv file of current data parsed
def create_csv(data):
    csv_path = "data/"
    today = date.today()
    current_date = today.strftime("%d-%m-%Y")
    file_name = csv_path + current_date + ".csv"

    # Write headers
    with open(file_name, 'w') as f:
        w = csv.writer(f)
        header = ['label', 'state', 'indian_confirmed', 'foreign_confirmed', 'cured', 'death']
        w.writerow(header)

        for row in data:
            w.writerow(row)
    print("File write Complete")
    return 1
create_csv(current_data())
