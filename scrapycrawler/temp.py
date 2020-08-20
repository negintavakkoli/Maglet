import json
from urllib.parse import urlparse

with open( "../Journals_list_complete_newURLs.json" , "rb" ) as f:
    jsonlist = json.load(f)
new_list = []
for item in jsonlist:
    url_temp = item["url"]
    if url_temp != "-":
        new_list.append(item)
with open( "../Journals_list_complete_final.json" , "w" ) as f:
    json.dump(new_list,f)

#
# r = open("Journals_direct_urls.json", "w")
#
# urls = []
# i = 0
# for item in f:
#     url_temp = item["url"]
#     title =  item["title"]
#     t = urlparse(url_temp).path
#     # print(len(t))
#     if len(t) > 1:
#         urls.append(url_temp)
#         r.write(title+"\t"+url_temp+"\n")
# r.close()


# f = open("Journals_direct_urls.txt", "r")
# dic = {}
# for line in f:
#     try:
#         q = line.strip().split("\t")
#         dic[q[1]] = q[2]
#     except:
#         print(line)
# f.close()
# for item in jsonlist:
#     url_temp = item["url"]
#     try:
#         new_url = dic[url_temp]
#         item["url"] = new_url
#         print(new_url)
#     except:
#         pass
# with open( "../Journals_list_complete_newURLs.json" , "w" ) as f:
#     json.dump(jsonlist,f)