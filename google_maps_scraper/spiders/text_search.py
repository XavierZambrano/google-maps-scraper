import scrapy
import json
from dotenv import load_dotenv
from scrapy import Request
from openlocationcode.openlocationcode import encode as OLCencode
from urllib.parse import unquote

from google_maps_scraper.items import Place
from google_maps_scraper.utils import GOOGLE_SUPPORTED_LANGUAGES, get_weekday_descriptions, get_periods

load_dotenv()  # load HTTP_PROXY and HTTPS_PROXY from .env file


class TextSearchSpider(scrapy.Spider):
    name = "text_search"
    allowed_domains = ["google.com"]

    def __init__(self, queries, language='en', limit=20, *args, **kwargs):
        super(TextSearchSpider, self).__init__(*args, **kwargs)
        
        self.page_size = 20
        self.language = language
        self.limit = int(limit)

        if isinstance(queries, list):
            self.queries = queries
        elif isinstance(queries, str):
            self.queries = queries.split(',')
        else:
            raise ValueError('queries must be a str delimited by commas or a list')
        
        if not self.queries:
            raise ValueError('queries is required')
        if self.language not in GOOGLE_SUPPORTED_LANGUAGES.values():
            raise ValueError(f'language {self.language} is not supported, please use one of: {json.dumps(GOOGLE_SUPPORTED_LANGUAGES, indent=2)}')
        if not (20 <= self.limit <= 120 and self.limit % 20 == 0):
            raise ValueError('limit must be between 20 and 120 and multiple of 20')

    def start_requests(self):
        for query in self.queries:
            query = query.replace(' ', '+')
            url = f'https://www.google.com/maps/search/?api=1&query={query}&hl={self.language}'
            yield Request(url, dont_filter=True, meta={'offset': 0, 'query': query})

    def parse(self, response):
        if response.meta['offset'] == 0:
            # first page
            script = response.xpath('//script[contains(text(), "window.APP_INITIALIZATION_STATE")]/text()').get()
            initialization_state = script.split('window.APP_INITIALIZATION_STATE=')[1].split('];')[0] + ']'
            initialization_state_json = json.loads(initialization_state)
            data1 = initialization_state_json[3]
            data2 = data1[2]

            data3 = json.loads(data2[5:])
        else:
            json_str1 = response.text[18:-6]
            json_str = json_str1.replace('\\n', '').replace('\\"', '\"')
            e_index = json_str.rfind('"e":')
            # Is necessary the unicode_escape, the response has strings like '\\uxxxx'
            json_str = json_str[:e_index - 2].encode().decode('unicode_escape')
            data3 = json.loads(json_str)

        # skip the first one, it's other data [1:]
        for index, raw_data in enumerate(data3[0][1][1:]):
            item = get_place_data(raw_data[14])
            yield item

        offset = response.meta['offset']
        query = response.meta['query']
        page = offset // self.page_size
        next_offset = offset + self.page_size
        if next_offset < self.limit:
            altitude = data3[1][0][0]
            longitude = data3[1][0][1]
            latitude = data3[1][0][2]
            next_page_url = (f'https://www.google.com/search?tbm=map&authuser=0'
                             f'&hl={self.language}'
                             f'&q={query}'
                             f'&tch=1'
                             f'&ech={page}'
                             f'&pb={get_protobuf(altitude, longitude, latitude, next_offset)}')
            yield Request(next_page_url, dont_filter=True, meta={'offset': next_offset, 'query': query})


def get_place_data(data4):
    colloquial_area = False
    decimal_numbers_coordinates = 7

    place = Place()
    cid = int(data4[10].split('0x')[-1], 16)


    place['id'] = data4[78]
    place['name'] = f'places/{place["id"]}'

    types = data4[13]
    if data4[76]:
        place['types'] = [fd[0] for fd in data4[76]]

    if types:
        place['primaryTypeDisplayName'] = {
            'text': types[0],
        }
    else:
        colloquial_area = True
    if data4[178]:
        place['nationalPhoneNumber'] = data4[178][0][1][0][0]
        place['internationalPhoneNumber'] = data4[178][0][0]
    if colloquial_area:
        place['formattedAddress'] = data4[18]
    else:
        place['formattedAddress'] = data4[39]
    latitude = float(f'{data4[9][2]:.{decimal_numbers_coordinates}f}')
    longitude = float(f'{data4[9][3]:.{decimal_numbers_coordinates}f}')
    globalCode = OLCencode(latitude, longitude)
    place['plusCode'] = {
        'globalCode': globalCode,
    }
    place['location'] = {
        'latitude': latitude,
        'longitude': longitude,
    }
    if data4[4]:
        place['rating'] = data4[4][7]
        place['userRatingCount'] = data4[4][8]

    place['googleMapsUri'] = 'https://maps.google.com/?cid=' + str(cid)
    if data4[7]:
        place['websiteUri'] = unquote(data4[7][0].split('/url?q=')[1]).split('&opi')[0]
        place['regularOpeningHours'] = {}
        if data4[203]:
            periods = get_periods(data4[203][0])
            place['regularOpeningHours']['periods'] = periods
            place['regularOpeningHours']['weekdayDescriptions'] = get_weekday_descriptions(periods)
    place['displayName'] = {
        'text': data4[11],
    }

    return place


def get_protobuf(altitude, longitude, latitude, offset):
    return (
        f"!4m8!1m3!1d"
        f"{altitude}"
        f"!2d"
        f"{longitude}"
        f"!3d"
        f"{latitude}"
        f"!3m2!1i1024!2i768!4f13.1!7i20!8i"
        f"{offset}"
        f"!10b1!12m25!1m1!18b1!2m3!5m1!6e2!20e3!6m16!4b1!23b1!26i1!27i1!41i2!45b1!49b1!63m0!67b1!73m0!74i150000!75b1!89b1!105b1!109b1!110m0!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m65!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m50!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m3!1s!2z!7e81!24m55!1m15!13m7!2b1!3b1!4b1!6i1!8b1!9b1!20b0!18m6!3b1!4b1!5b1!6b1!13b0!14b0!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m4!1e3!1e6!1e14!1e15!24b1!25b1!26b1!29b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!89b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i768!1m6!1m2!1i974!2i0!2m2!1i1024!2i768!1m6!1m2!1i0!2i0!2m2!1i1024!2i20!1m6!1m2!1i0!2i748!2m2!1i1024!2i768!34m16!2b1!3b1!4b1!6b1!8m4!1b1!3b1!4b1!6b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!46m1!1e9!47m0!49m1!3b1!50m53!1m49!2m7!1u3!4s!5e1!9s!10m2!3m1!1e1!2m7!1u2!4s!5e1!9s!10m2!2m1!1e1!2m7!1u16!4s!5e1!9s!10m2!16m1!1e1!2m7!1u16!4s!5e1!9s!10m2!16m1!1e2!3m11!1u16!2m4!1m2!16m1!1e1!2s!2m4!1m2!16m1!1e2!2s!3m1!1u2!3m1!1u3!4BIAE!2e2!3m1!3b1!59B!65m0!69i540"
    )