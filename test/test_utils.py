import unittest
import json

from google_maps_scraper.spiders.text_search import get_place_data
from google_maps_scraper.utils import get_weekday_descriptions


class TestGetPlaceData(unittest.TestCase):
    def test_get_place_data_name(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['name'], expected_result['name'])
    
    def test_get_place_data_types(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        expected_result = ['french_restaurant', 'modern_french_restaurant', 'restaurant']

        self.assertEqual(place_data['types'], expected_result)

    def test_get_place_data_id(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['id'], expected_result['id'])

    def test_get_place_data_primaryTypeDisplayName(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)
        expected_result['primaryTypeDisplayName'].pop('languageCode')

        self.assertEqual(place_data['primaryTypeDisplayName'], expected_result['primaryTypeDisplayName'])

    def test_get_place_data_nationalPhoneNumber(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['nationalPhoneNumber'], expected_result['nationalPhoneNumber'])

    def test_get_place_data_internationalPhoneNumber(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['internationalPhoneNumber'], expected_result['internationalPhoneNumber'])

    def test_get_place_data_formattedAddress(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['formattedAddress'], expected_result['formattedAddress'])
    
    def test_get_place_data_plusCode(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)
        expected_result['plusCode'].pop('compoundCode')
        self.assertEqual(place_data['plusCode'], expected_result['plusCode'])
    
    def test_get_websiteUri(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['websiteUri'], expected_result['websiteUri'])
    
    def test_get_regularOpeningHours_periods(self):
        with open('test/assets/place_data_ChIJdxxU1WeuEmsR11c4fswX-Io.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJdxxU1WeuEmsR11c4fswX-Io.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['regularOpeningHours']['periods'], expected_result['regularOpeningHours']['periods'])

    def test_get_regularOpeningHours_weekdayDescriptions(self):
        with open('test/assets/place_data_ChIJdxxU1WeuEmsR11c4fswX-Io.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJdxxU1WeuEmsR11c4fswX-Io.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['regularOpeningHours']['weekdayDescriptions'], expected_result['regularOpeningHours']['weekdayDescriptions'])

    def test_get_regularOpeningHours_weekdayDescriptions_closed_days(self):
        with open('test/assets/place_data_ChIJE0JkojOvEmsRvo_DkZ7zBBg.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/text_search_place_ChIJE0JkojOvEmsRvo_DkZ7zBBg.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['regularOpeningHours']['weekdayDescriptions'], expected_result['regularOpeningHours']['weekdayDescriptions'])

    def test_get_userRatingCount(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['userRatingCount'], expected_result['userRatingCount'])

    def test_get_place_data_location(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)
        decimal_numbers = 7
        for key, value in expected_result['location'].items():
            value_truncated = float(f'{value:.{decimal_numbers}f}')
            expected_result['location'][key] = value_truncated

        self.assertEqual(place_data['location'], expected_result['location'])

    def test_get_place_data_rating(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['rating'], expected_result['rating'])

    def test_get_place_data_googleMapsUri(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['googleMapsUri'], expected_result['googleMapsUri'])

    def test_get_place_data_displayName(self):
        with open('test/assets/place_data_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            expected_result = json.load(f)
        expected_result['displayName'].pop('languageCode')

        self.assertEqual(place_data['displayName'], expected_result['displayName'])


class TestGetPlaceDataColloquialArea(unittest.TestCase):
    def test_get_place_data_id(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['id'], expected_result['id'])

    def test_get_place_data_primaryTypeDisplayName(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))

        self.assertNotIn('primaryTypeDisplayName', place_data)

    def test_get_place_data_nationalPhoneNumber(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))

        self.assertNotIn('nationalPhoneNumber', place_data)

    def test_get_place_data_internationalPhoneNumber(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))

        self.assertNotIn('internationalPhoneNumber', place_data)

    def test_get_place_data_formattedAddress(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['formattedAddress'], expected_result['formattedAddress'])

    def test_get_place_data_location(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            expected_result = json.load(f)
        decimal_numbers = 7
        for key, value in expected_result['location'].items():
            value_truncated = float(f'{value:.{decimal_numbers}f}')
            expected_result['location'][key] = value_truncated

        self.assertEqual(place_data['location'], expected_result['location'])

    def test_get_place_data_rating(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))

        self.assertNotIn('rating', place_data)

    def test_get_place_data_googleMapsUri(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            expected_result = json.load(f)

        self.assertEqual(place_data['googleMapsUri'], expected_result['googleMapsUri'])

    def test_get_place_data_displayName(self):
        with open('test/assets/place_data_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            place_data = get_place_data(json.load(f))
        with open('test/expected/place_ChIJP3Sa8ziYEmsRUKgyFmh9AQM.json', 'r') as f:
            expected_result = json.load(f)
        expected_result['displayName'].pop('languageCode')

        self.assertEqual(place_data['displayName'], expected_result['displayName'])

class TestUtils(unittest.TestCase):
    def test_get_weekday_descriptions(self):
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = json.load(f)
        result = get_weekday_descriptions(place_data['regularOpeningHours']['periods'])
        expected_result = place_data['regularOpeningHours']['weekdayDescriptions']

        self.assertEqual(result, expected_result)
