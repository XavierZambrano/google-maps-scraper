import scrapy
import json
from dotenv import load_dotenv

from google_maps_scraper.utils import GOOGLE_SUPPORTED_LANGUAGES

load_dotenv()  # load HTTP_PROXY and HTTPS_PROXY from .env file


class TextSearchSpider(scrapy.Spider):
    name = "text_search"
    allowed_domains = ["google.com"]

    def __init__(self, query='', language='en', max_results=20, *args, **kwargs):
        super(TextSearchSpider, self).__init__(*args, **kwargs)

        self.max_results = int(max_results)

        if not query:
            raise ValueError('query is required')
        if language not in GOOGLE_SUPPORTED_LANGUAGES.values():
            raise ValueError(f'language {language} is not supported, please use one of: {json.dumps(GOOGLE_SUPPORTED_LANGUAGES, indent=2)}')
        if not (20 <= self.max_results <= 120 and self.max_results % 20 == 0):
            raise ValueError('max_results must be between 20 and 120 and multiple of 20')

        query = query.replace(' ', '+')
        self.start_urls = [f'https://www.google.com/maps/search/?api=1&query={query}&hl={language}']

    def parse(self, response):
        script = response.xpath('//script[contains(text(), "window.APP_INITIALIZATION_STATE")]/text()').get()
        initialization_state = script.split('window.APP_INITIALIZATION_STATE=')[1].split('];')[0] + ']'
        initialization_state_json = json.loads(initialization_state)
        data1 = initialization_state_json[3]
        data2 = data1[2]

        data3 = json.loads(data2[5:])

        # skip the first one, it's other data [1:]
        for index, place_data in enumerate(data3[0][1][1:]):
            data4 = place_data[14]

            cid = data3[16][3][0][4][index][0][1]

            _id = data4[78]
            types = data4[13]
            primaryTypeDisplayName = {
                'text': types[0],
            }
            nationalPhoneNumber = data4[178][0][1][0][0]
            internationalPhoneNumber = data4[178][0][0]
            formattedAddress = data4[39]
            location = {
                'latitude': data4[9][2],
                'longitude': data4[9][3],
            }
            rating = data4[4][7]
            googleMapsUri = 'https://maps.google.com/?cid=' + cid
            displayName = {
                'text': data4[11],
            }

            yield {
                'id': _id,
                'primaryTypeDisplayName': primaryTypeDisplayName,
                # 'types': types,
                'nationalPhoneNumber': nationalPhoneNumber,
                'internationalPhoneNumber': internationalPhoneNumber,
                'formattedAddress': formattedAddress,
                'location': location,
                'rating': rating,
                'googleMapsUri': googleMapsUri,
                'displayName': displayName,
            }


