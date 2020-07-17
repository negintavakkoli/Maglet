import scrapy


class MagletSpider(scrapy.Item):

    name = scrapy.Field()
    link = scrapy.Field()