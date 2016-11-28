# Selenium Surfer
#
# This script will use Selenium to get into LenderX's webpage and download the
# AppraiserPerformance file
#
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time 

import re
import urllib
from bs4 import BeautifulSoup

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

browser.get("https://app.lenderx.com/?view=/view/report")

def login_entry(username, password):
    login_email = browser.find_element_by_name('email')
    login_email.send_keys(username)
    login_password = browser.find_element_by_name('password')
    login_password.send_keys(password)
    #login_password.submit()  <-- this produces errors. Why?
    submit_elem = browser.find_element_by_name('submit')
    submit_elem.click()

# temporary variables; to be imported via login module later
login_entry('', '')

time.sleep(10) # necessary for entire page markup to load; see how quick you can get it
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
#reports_element = browser.find_element_by_xpath("//*[contains(text(), 'Reports')]").click() # "click" not working
#reports_element = browser.find_element_by_xpath("//*[contains(text(), 'Reports')]").send_keys(Keys.ENTER) # "click" not working

# This is the error I'm getting in the console:
# selenium.common.exceptions.ElementNotVisibleException: Message: Element is not visible
# See this StackOverflow question for potential workaround: http://stackoverflow.com/q/27927964/3856609
