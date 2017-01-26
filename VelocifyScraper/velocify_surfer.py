# Velocify Surfer
#
# This script will use Selenium to get into Velocify's webpage and access the
# DialIQDashboard
#
# Client ID: LmGuaranteedRate
# Agent ID: 1698
#
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

# ~~~ FUNCTIONS ~~~
def login_entry(username, password):
    login_email = browser.find_element_by_id('UserName')
    login_email.send_keys(username)
    login_password = browser.find_element_by_id('Password')
    login_password.send_keys(password)
    submit_elem = browser.find_element_by_xpath("//button[contains(text(), 'Log in')]")
    submit_elem.click()

def tab_navigation():
    time.sleep(20) # REPLACE WITH: a timer that waits until the page finishes loading
    navigate_to_Logs = browser.find_element_by_link_text('Logs')
    navigate_to_Logs.click()
    time.sleep(3)
    navigate_to_Distribution_by_Agent = browser.find_element_by_link_text('Distribution by Agent')
    navigate_to_Distribution_by_Agent.click()

#def header_form_fill(client_id, agent_id, start_date, end_date):

# ~~~ PROCEDURE ~~~
browser.get("https://dialiqdashboard.velocify.com/Login")
login_entry('Velocify1', 'bw6IWWjElVQBXtF') # temporary variables; to be imported via login module later
tab_navigation()

#browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
#time.sleep(5)
#browser.switch_to_frame(browser.find_element_by_tag_name('iframe'))
#time.sleep(5)

#surfer_output = open('surfer_output.txt', 'w')
#surfer_output.write(repr(browser.page_source))
#surfer_output.close()
