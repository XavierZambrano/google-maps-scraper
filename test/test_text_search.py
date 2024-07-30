import os
from betamax import Betamax
from betamax.fixtures.unittest import BetamaxTestCase
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse

from google_maps_scraper.spiders.text_search import TextSearchSpider


with Betamax.configure() as config:
    cassette_library_dir = 'test/fixtures/cassettes'
    os.makedirs(cassette_library_dir, exist_ok=True)

    config.cassette_library_dir = cassette_library_dir
    config.preserve_exact_body_bytes = True


class TestTextSearchSpider(BetamaxTestCase):
    def setUp(self):
        super().setUp()

        process = CrawlerProcess(install_root_handler=False)
        process.crawl(TextSearchSpider)
        self.spider = list(process.crawlers)[0].spider

    def test_parse_name(self):
        # TODO
        # restaurants in sydney
        # mock_response =
        expected_result = 'Restaurant Hubert'

        result = {}

        self.assertEqual(result['name'], expected_result)

    def get_mock_response(self, url):
        response = self.session.get(url)
        if response.ok is False:
            raise ValueError(f'Request to {url} failed with status code {response.status_code}')
        scrapy_response = HtmlResponse(url=url, body=response.content)

        return scrapy_response
