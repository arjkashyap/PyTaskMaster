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

from selenium import webdriver
from time import sleep
import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tweetFilter

username = config.username
password = config.pswd

tweet = tweetFilter.finalTweet

# Driver object
driver = webdriver.Firefox(executable_path = "./geckodriver")

driver.get("https://twitter.com/")
sleep(2)

tweetBox = "//div[@aria-labelledby='Tweetstorm-tweet-box-0-label Tweetstorm-tweet-box-0-text-label']//div"

driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input").send_keys(password)
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(5)

autotw1 = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='tweet-box-home-timeline']")))
autotw1.send_keys(tweet)

tweet = driver.find_element_by_xpath("//span[@class='add-tweet-button ']//following-sibling::button[contains(@class,'tweet-action')]")
tweet.click()
