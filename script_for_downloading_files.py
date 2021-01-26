import re
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# get the web content urls
r = requests.get('https://aliah.ac.in/').text

# converting into Beautifulsoup Object
soup = bs(r, 'lxml')

# printing only HTML
# print(soup.body.select('a[href^="https"]'))
pdf_file_list = soup.body.select('a[href$=".pdf"]')
str_list = str(pdf_file_list)
fresh_link = re.sub(
    '(href=|<|>|Downloads|target="_blank"|]|Download|class="btn btn-info btn-xs"|\+|/a, a|")', "", str_list)
data = fresh_link.split('/a, a')
filter_data = filter(None, data)
link_list = []
for i in filter_data:
    link_list.append(i.strip('[a/'))
print(link_list)
