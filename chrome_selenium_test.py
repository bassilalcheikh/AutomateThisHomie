from selenium import webdriver
import time

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

def login_entry(username, password, browser):
    login_email = browser.find_element_by_id('UserName')
    login_email.send_keys(username)
    login_password = browser.find_element_by_id('Password')
    login_password.send_keys(password)
    submit_elem = browser.find_element_by_xpath("//button[contains(text(), 'Log in')]")
    submit_elem.click()

driver.get('www.example.com')
time.sleep(3) # Let the user actually see something!
login_entry('username', 'password', driver)
#search_box.send_keys('ChromeDriver')
#search_box.submit()
time.sleep(5)
test_output = open('chrome_selenium_test_source_output.html', 'w')
test_output.write(repr(driver.page_source))
test_output.close()

time.sleep(5) # Let the user actually see something!
driver.quit()
