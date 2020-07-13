import requests
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url= "https://journals.msrt.ir/"
req = requests.get(url)
soup = BeautifulSoup(req.text)
journals_link = soup.find("div", {"class":"category__item__panel__body"})
journals_link_list = []
for tag in journals_link.findAll("a"):
    i = 0
    journals_link_list.insert(i, tag["href"])
    journals_link_list[i] = urljoin(url, journals_link_list[i])
    i =+ 1


journals_link_json = json.dump(journals_link_list,open("Journals_link.json","w"))
print(journals_link_json )
