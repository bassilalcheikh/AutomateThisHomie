# LenderX ETL
#
# Guaranteed Rate, Inc.
#
# Project Specification: extract the results from the LenderX tables and upload
# them into the database.
#
#
#import time
#import LenderXreadXLS
#import selenium_surfer

def login_info(welcome):
    print(welcome)
    username = raw_input("Please input username: ")
    password = raw_input("Please input password: ")
    return [username, password]

credentials = login_info("Hello, welcome to the ETL automator!")

#print(LenderXreadXLS.get_row_str(7))
