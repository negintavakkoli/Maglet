# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
#from maglet.item import MagletSpider
#from scrapy.http import HtmlResponse


#class MagletSpider

class acSpider(scrapy.Spider):
    name = "ac"

    allowed_domains = [
        "journals.research.ac.ir"
    ]

    start_urls = [
        "https://journals.research.ac.ir/"
    ]

    def parse(self , response):
        # Extracting the content using css selectors
        #titles = response.xpath ( '//div[@class="TblRowMain"]').extract()
        titles = response.xpath ('//span/text()').get()
        #votes = response.css ( '.score.unvoted::text' ).extract ()
        #times = response.css ( 'time::attr(title)' ).extract ()
        #comments = response.css ( '.comments::text' ).extract ()
        scraped_info = {'title': titles}
        print(scraped_info)
        yield scraped_info
        # Give the extracted content row wise
        """for item in zip ( titles ):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0] ,
                #'vote': item[1] ,
                #'created_at': item[2] ,
                #'comments': item[3] ,
            }

            # yield or give the scraped info to scrapy
            print(scraped_info)
            yield scraped_info"""











  #  rules = (
   #     Rule ( LinkExtractor () , callback = 'parsemsrt' , follow = True ) ,)

    """def parsemsrt(self , response ):

        for div in response.xpath ( "//div[@class='TblRowMain']/text()" ).extract():
            print(div)
            yield {"title": div}



        for href in response.xpath ( '//a/@href' ).getall ():
            print(href)
            yield scrapy.Request ( response.urljoin ( href ) , self.parse )

     #  body = response.css("body").extract_first()
      ## print(item)
       # yield item"""

