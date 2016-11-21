# Selenium Surfer
#
# This script will use Selenium to get into LenderX's webpage and download the
# AppraiserPerformance file
#
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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

#print(len(browser.find_elements_by_class_name("x-btn-arrow")))
#reports_click_element = browser.find_element_by_id('ext-gen46')
#reports_click_element.click()


html = urllib.urlopen(browser.current_url)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)

for x in data:
    print str(x)



#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
