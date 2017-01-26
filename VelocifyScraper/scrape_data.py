# Velocify Data Scraper
#
import webbrowser
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test_source.html'), "html.parser")

#header_labels = ["Local Time", "Step", "Data", "Query Type", "Query ID", "Contact ID", "Notification", "Program ID"]

stuff = soup.find_all('tbody')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#def get_event_desc():
    #for each row, grab and store the information (i.e., column values)

print(stuff)
