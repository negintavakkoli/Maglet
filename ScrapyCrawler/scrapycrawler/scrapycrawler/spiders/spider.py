import scrapy
from scrapy.selector import Selector


class MagletSpider(scrapy.Spider):
    name = "maglet"
    allowed_domains = ["https://journals.msrt.ir/"]
    start_urls = ["https://journals.msrt.ir/"]

    def parse(self, response):
        filename = response.url.split( "/" )[-2]
        with open( filename, 'wb' ) as f:
            f.write( response.body )


