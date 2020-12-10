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
min_delay = 1    # delay after application

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

def applyAllJobs():
	"""
	Apply for all the jobs listed 
	on the currently opened page
	"""
	curr_url = browser.current_url    # store base url before navigating
	try:
		link_driver = browser.find_elements_by_xpath("//a[@class='view_detail_button']")   # list of all driver object contains all job links
		links = []   # html links 
		for l in link_driver:
			link = l.get_attribute('href')  # extract link from object
			links.append(link)

		# open link one by one and apply for internship
		for link in links:
			browser.get(link)
			apply_btn = browser.find_element_by_xpath('//button[normalize-space()="Apply now"]')
			apply_btn.click()
			
			apply_btn_proceed = browser.find_element_by_xpath('//button[normalize-space()="Proceed to application"]')
			apply_btn_proceed.click()

			text_fields_driver = browser.find_elements_by_xpath("//textarea")
			tf_index = 0   # index of the form field being filled
			for tf in text_fields_driver:
				tf.clear()
				if tf_index == 0:
					tf.send_keys(consts.app_letter)
				elif tf_index == 1:
					tf.send_keys("Yes")
				else: 
					tf.send_keys("Yes. www.github.com/bing101")

				tf_index += 1

			# Submit form for application
			submit_btn = browser.find_element_by_id("submit")
			submit_btn.click()

			time.sleep(navigation_delay)

	except Exception as e:
		print(e)
		pass

	browser.get(curr_url)

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
		applyAllJobs()
		gotoNextPage()
		curr_page += 1

if __name__ == "__main__":
	main()