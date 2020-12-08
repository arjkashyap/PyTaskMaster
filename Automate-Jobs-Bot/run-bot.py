from selenium import webdriver
import os
import time
import consts

URL = "https://internshala.com/student/dashboard"
driver_path = os.path.join(os.getcwd(), "driver", "geckodriver.exe")
browser = webdriver.Firefox()

# Delay timers
login_delay = 8
navigation_delay = 3

def login():
	"""
	Function will log you into your 
	internshalla account
	"""
	mail_field = browser.find_element_by_id("email")
	pass_field = browser.find_element_by_id("password")
	login_btn = browser.find_element_by_id("login_submit")

	mail_field.send_keys(consts.mail)
	pass_field.send_keys(consts.password)
	login_btn.click()
	time.sleep(login_delay)

	link_main = browser.find_element_by_xpath('//*[@id="internships_new_superscript"]')
	link_main.click()

def gotoNextPage():
	"""
	Navigate to next page
	"""
	nxt_btn = browser.find_element_by_id("next")
	nxt_btn.click()
	time.sleep(navigation_delay)

def main():
	print(URL)
	browser.get(URL)
	time.sleep(navigation_delay)
	
	login()
	
	total_pages = int(browser.find_element_by_id("total_pages").get_attribute("innerHTML"))
	print(total_pages, " Pages Found . .")
	curr_page = 1
	while(curr_page <= total_pages):
		print("Current Page", curr_page)

		gotoNextPage()
		curr_page += 1

if __name__ == "__main__":
	main()