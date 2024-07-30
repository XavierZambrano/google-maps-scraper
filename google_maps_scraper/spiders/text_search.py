import scrapy


class TextSearchSpider(scrapy.Spider):
    name = "text_search"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]

    def __init__(self, query='', *args, **kwargs):
        super(TextSearchSpider, self).__init__(*args, **kwargs)

        if not query:
            raise ValueError('query is required')

        query = query.replace(' ', '+')
        self.start_urls = [f'https://google.com/search/{query}/']

    def parse(self, response):
        pass
