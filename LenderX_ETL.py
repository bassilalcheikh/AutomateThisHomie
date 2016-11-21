# LenderX ETL
#
# Guaranteed Rate, Inc.
#
# Project Specification: extract the results from the LenderX tables and upload
# them into the database.
#
#
#import time
#import res, bs4
#res = requests.get('http://')
def login_info(welcome):
    print(welcome)
    username = raw_input("Please input username: ")
    password = raw_input("Please input password: ")
    return [username, password]

credentials = login_info("Hello, welcome to the ETL mumbo-jumbo!")

website_homepage = 'https://app.lenderx.com'
