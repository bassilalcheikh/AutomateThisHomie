# Selenium Surfer
#
# This script will use Selenium to get into LenderX's webpage and download the
# AppraiserPerformance file
#
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

browser.get("https://app.lenderx.com/?view=/view/report")

def login_entry(username, password):
    login_email = browser.find_element_by_name('email')
    login_email.send_keys(username)
    login_password = browser.find_element_by_name('password')
    login_password.send_keys(password)
    submit_elem = browser.find_element_by_name('submit')
    submit_elem.click()

# temporary variables; to be imported via login module later
login_entry('blake.harrison@rate.com', 'qxm7g4k0+')

time.sleep(10) # necessary for entire page markup to load; see how quick you can get it
elements = browser.find_elements_by_xpath("//button[contains(text(), 'Reports')]") #element="7cf0097f-88ae-47c4-b15e-e20fe4e08eb7"
#for i in elements: i.click()
elements[0].click()

#surfer_output = open('surfer_output.txt', 'w')
#surfer_output.write(repr(browser.page_source))
#surfer_output.close()
