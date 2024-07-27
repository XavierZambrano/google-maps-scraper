import scrapy


class TextSearchSpider(scrapy.Spider):
    name = "text_search"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]

    def parse(self, response):
        pass
