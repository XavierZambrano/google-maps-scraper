import os
import json
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
        process.crawl(TextSearchSpider, query='filler text to satisfy the query requirement')
        self.spider = list(process.crawlers)[0].spider

    def test_parse_id(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['id'], expected_result['id'])

    def test_parse_primaryType(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['primaryType'], expected_result['primaryType'])

    def test_parse_nationalPhoneNumber(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['nationalPhoneNumber'], expected_result['nationalPhoneNumber'])

    def test_parse_internationalPhoneNumber(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['internationalPhoneNumber'], expected_result['internationalPhoneNumber'])

    def test_parse_formattedAddress(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['formattedAddress'], expected_result['formattedAddress'])

    def test_parse_location(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)
        decimal_numbers = 7
        for key, value in expected_result['location'].items():
            value_truncated = float(f'{value:.{decimal_numbers}f}')
            expected_result['location'][key] = value_truncated

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['location'], expected_result['location'])

    def test_parse_rating(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['rating'], expected_result['rating'])

    def test_parse_googleMapsUri(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['googleMapsUri'], expected_result['googleMapsUri'])

    def test_parse_displayName(self):
        mock_response = self.get_mock_response(f'https://google.com/maps/search/restaurants+in+sydney/')
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)
        expected_result['displayName'].pop('languageCode')

        generator = self.spider.parse(mock_response)
        result = next(generator)

        self.assertEqual(result['displayName'], expected_result['displayName'])

    def get_mock_response(self, url):
        response = self.session.get(url)
        if response.ok is False:
            raise ValueError(f'Request to {url} failed with status code {response.status_code}')
        scrapy_response = HtmlResponse(url=url, body=response.content)

        return scrapy_response
