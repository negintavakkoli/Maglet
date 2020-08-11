# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
import json
import os
import pickle
class ArticlescraperSpider(CrawlSpider):
    name = 'maglet'
    allowed_domains = []
    start_urls = []
    with open("Journals_list_complete.json" ,"r") as f:
        j = json.load(f)

        for item in j:
            url_temp = item["url"]
            start_urls.append(url_temp)
            allowed_domains.append (urlparse(url_temp).netloc)



    rules = (
        #Rule(LinkExtractor(), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('article',)), callback='parse_item'),
        Rule(LinkExtractor() , follow=True),
        )

    def parse_item(self, response):
        filename = urlparse(response.request.url).netloc.replace("/", "_")

        try:
            with open(os.path.join(filename+".abstract"), 'rb') as f:
                list_abstract = pickle.load(f)
        except:
            list_abstract = []
        try:
            with open(os.path.join(filename+".title"), 'rb') as f:
                list_title = pickle.load(f)
        except:
            list_title = []
        #filename = urlparse(response.request.url).path.replace("/", "_")
        ####Yektaweb
        t1 = response.xpath('//tr/td[@class="abstractmed"]').getall()
        t2 = response.xpath('//span[@class="abstract_title"]').getall()
        if len(t1) > 0:
            abstract = ""
            max_len = 0
            for item in t1:
                soup = BeautifulSoup(item)
                t = soup.text
                if len(t) > max_len:
                    max_len = len(t)
                    abstract = t
            if len(t2)>0:
                title = ""
                max_len = 0
                for item in t2:
                    soup = BeautifulSoup(item)
                    t = soup.text
                    if len(t) > max_len:
                        max_len = len(t)
                        title = t
            list_abstract.append(abstract)
            list_title.append(title)
        else:
            ####Sinaweb
            tt = response.xpath('//div[@class="padding_abstract justify"]').getall()
            title = response.xpath('//span[@class="article_title bold"]//text()').get()
            abstract = ""
            max_len = 0
            for item in tt:
                soup = BeautifulSoup(item)
                t = soup.text
                if len(t) > max_len:
                    max_len = len(t)
                    abstract = t
            if len(t2) > 0:
                title = ""
                max_len = 0
                for item in t2:
                    soup = BeautifulSoup(item)
                    t = soup.text
                    if len(t) > max_len:
                        max_len = len(t)
                        title = t
            list_abstract.append(abstract)
            list_title.append(title)
        with open(os.path.join(filename+".abstract"), 'wb') as f:
            pickle.dump(list_abstract, f)
        with open(os.path.join(filename+".title"), 'wb') as f:
            pickle.dump(list_title, f)