from selenium import webdriver
import time

url = 'www.example.com'
driver = webdriver.Chrome()

def login_entry(username, password, browser):
    login_email = browser.find_element_by_id('UserName')
    login_email.send_keys(username)
    login_password = browser.find_element_by_id('Password')
    login_password.send_keys(password)
    submit_elem = browser.find_element_by_xpath("//button[contains(text(), 'Log in')]")
    submit_elem.click()
    
def record_source_code(file_name, browser):
    time.sleep(5)
    file_destination = open(file_name, 'w')
    file_destination.write(repr(browser.page_source))
    file_destination.close()

driver.get(url)
time.sleep(3) # Let the user actually see something!
login_entry('username', 'password', driver)

record_source_code('chrome_selenium_test_source_output.html', driver)

time.sleep(5) # Let the user actually see something!
driver.quit()
