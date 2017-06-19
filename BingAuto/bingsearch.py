from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def login_entry(username, password, browser): # logs into website
    login_email = browser.find_element_by_id('UserName')
    login_email.send_keys(username)
    login_password = browser.find_element_by_id('Password')
    login_password.send_keys(password)
    submit_elem = browser.find_element_by_xpath("//button[contains(text(), 'Log in')]")
    submit_elem.click()

def main_function(agent_id):
    driver = webdriver.Chrome()
    driver.get('https://www.bing.com/')
    #login
    login_entry(credentials_page.website_username, credentials_page.website_password, driver)
    time.sleep(3) # WAIT: NECESSARY
    # first test to see if "not found"
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[2]/div[2]/table/tbody')))
    table_html = get_element('/html/body/div/div/div[2]/div[2]/table/tbody', driver)
    driver.quit()
