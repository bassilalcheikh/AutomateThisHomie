# Main Script for Bing Search Automator
#
import import_logins
import bingsearch
#import time
#t_0 = time.time()

usernames = import_logins.usernames
passwords = import_logins.passwords

for id_number in agent_id_numbers:
    if web_element_scraper.main_function(str(id_number)):
        time.sleep(3) # WAIT: NECESSARY
        web_element_cleaner.main_function('results_cache.html','detagged_markup.html')
        time.sleep(3) # WAIT: NECESSARY
        print("Preparing to upload data for Agent "+str(id_number))
        db_upload.main_function(str(id_number))

#m, s = divmod(time.time()-t_0, 60)
#print "ETL process completed. Time taken: %02d:%02d" % (m, s)
