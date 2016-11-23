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
time.sleep(5)
#print(len(browser.find_elements_by_class_name("x-btn-arrow")))
#reports_click_element = browser.find_element_by_id('ext-gen46')
#reports_click_element.click()
browser.switch_to.frame(browser.find_element_by_tag_name('iframe'))
reports_element = browser.find_element_by_link_text('Reports') # this is not found
reports_element.click()
