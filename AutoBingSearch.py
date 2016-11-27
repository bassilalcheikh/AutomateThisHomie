# Automate the Daily Bing Search 
#
# 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

browser.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1480117030&rver=6.7.6631.0&wp=MBI&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttp%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1&lc=1033&id=264960")

usr = input("enter username")
pwd = input("enter password")

def login_entry(username, password):
    login_email = browser.find_element_by_id('i0116')
    login_email.send_keys(username)
    submit_elem_1 = browser.find_element_by_id('idSIButton9').click()
    time.sleep(3)
    login_password = browser.find_element_by_id('i0118')
    login_password.send_keys(password)
    submit_elem_2 = browser.find_element_by_id('idSIButton9')
    submit_elem_2.click()

login_entry(usr, pwd)

def brute_search(count):
    starting_number = int(time.strftime("%j"))
    search_input = browser.find_element_by_id('sb_form')
    search_enter = browser.find_element_by_id('sb_form_go')
    time.sleep(2)
    search_input.send_keys(str(starting_number-1))
    search_enter.click()
    browser.find_element_by_xpath("//*[contains(text(), 'Images')]").click()
    for i in range(starting_number, starting_number+count+1):
        time.sleep(3)
        # ERROR HERE:
        #browser.find_element_by_xpath("//*[contains(title(), 'Search for:')]").click()
        #print(i)
  

time.sleep(3)
brute_search(30)

