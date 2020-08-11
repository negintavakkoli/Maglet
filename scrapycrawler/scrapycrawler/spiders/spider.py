# # -*- coding: utf-8 -*-
# import scrapy
# import json
#
#
#
#
#
# class JournalSpider(scrapy.Spider):
#     name = "JournalSpider"
#     #start_urls = ['http://amf.ui.ac.ir/?_action=xml&article=23635']
#     # with open("../../../Maglet_1.0.0/Journals_to_Crawl/Journals_list_complete.json",'r') as journals_list:
#     #     healthcare_dic = json.load(journals_list)
#     # start_url = []
#     # for item in healthcare_dic:
#     #     start_url.append(item["url"])
#     # make json file/ directory
#     # print(start_url)
#
#
#     def start_requests(self):
#         urls = ['https://jipa.ut.ac.ir/?_action=xml&issue=9990']
#         for index, url in enumerate(urls):
#             yield scrapy.Request(url,meta = {"index":index})
#
#
#
#
#     def parse(self , response):
#         # print("***********************")
#         # print ( response.headers['Content-Type'] )
#         content = response.headers['Content-Type']
#         print(content)
#         if "xml" in content.lower():
#             with open(str(response.meta["index"]), "w") as files:
#                 files.write(response.text)
#
