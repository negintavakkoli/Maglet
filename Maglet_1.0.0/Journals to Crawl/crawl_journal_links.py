import json
from urllib import parse as PR
import requests as RQ
from bs4 import BeautifulSoup
import os
import xml.etree.ElementTree as ET






with open('Journals_list_complete.json', 'r') as journals_list:
    healthcare_dic = json.load ( journals_list )


website_name = {}

for item in healthcare_dic:
    website_name[item["url"]] = item["ID"]

for website , id in website_name.items():
    if(website=="-"):
        continue
    try:
        dir = os.path.join("Journals_XML", str(id))
        os.mkdir(dir)
    except FileExistsError:
        pass
    except:
        print("Error")
    allowed_domain = website
    NETLOC_mother = PR.urlparse(website).netloc
    seed = [website]
    visited = {}
    xml_count = 0
    index_counter = 1
    while len(seed) > 0 :
        link_to_see = seed.pop(0)
        try:
            temp = visited[link_to_see]
            continue
        except:
            visited[link_to_see] = 1
        try:
            r = RQ.get(link_to_see,timeout=3)
        except Exception as e:
            continue
        if "xml" in r.headers["Content-Type"]:
            with open(os.path.join(dir ,str(index_counter)+".xml"), "w") as f:
                f.write(r.text)
            xml_count+=1
            index_counter+=1
        else:
            soup = BeautifulSoup(r.content)
            for a in soup.find_all('a', href=True):
                link = a["href"]
                link = PR.urljoin(allowed_domain,link)
                link = link.lower()
                if(PR.urlparse(link).netloc == NETLOC_mother):
                    seed.append(link)
        seed = list(set(seed))
        print(link_to_see,len(seed),len(visited),xml_count)