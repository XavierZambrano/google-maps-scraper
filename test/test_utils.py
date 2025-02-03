import unittest
import json

from google_maps_scraper.spiders.text_search import get_place_data
from google_maps_scraper.utils import get_weekday_descriptions, get_periods



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
    maxDiff = None
    def test_get_weekday_descriptions(self):
        with open('test/expected/place_ChIJF5-RdGquEmsR5rN_H74uSqQ.json', 'r') as f:
            place_data = json.load(f)
        result = get_weekday_descriptions(place_data['regularOpeningHours']['periods'])
        expected_result = place_data['regularOpeningHours']['weekdayDescriptions']

        self.assertEqual(result, expected_result)

    def test_get_periods(self):
        mock_data = [
            ['domingo', 7, [2025, 2, 9], [['Cerrado']], 0, 2],
            ['lunes', 1, [2025, 2, 10], [['12–2:30\u202fp.m.', [[12], [14, 30]]], ['5:30–9:30\u202fp.m.', [[17, 30], [21, 30]]]], 0, 1],
            ['martes', 2, [2025, 2, 4], [['12–2:30\u202fp.m.', [[12], [14, 30]]], ['5:30–9:30\u202fp.m.', [[17, 30], [21, 30]]]], 0, 1],
            ['miércoles', 3, [2025, 2, 5], [['12–2:30\u202fp.m.', [[12], [14, 30]]], ['5:30–9:30\u202fp.m.', [[17, 30], [21, 30]]]], 0, 1],
            ['jueves', 4, [2025, 2, 6], [['12–2:30\u202fp.m.', [[12], [14, 30]]], ['5:30–9:30\u202fp.m.', [[17, 30], [21, 30]]]], 0, 1],
            ['viernes', 5, [2025, 2, 7], [['12–2:30\u202fp.m.', [[12], [14, 30]]], ['5:30–9:30\u202fp.m.', [[17, 30], [21, 30]]]], 0, 1],
            ['sábado', 6, [2025, 2, 8], [['5–9:30\u202fp.m.', [[17], [21, 30]]]], 0, 1],
        ]
        expected_result = [
            {
                'close': {'day': 1, 'hour': 14, 'minute': 30},
                'open': {'day': 1, 'hour': 12, 'minute': 0}},
            {
                'close': {'day': 1, 'hour': 21, 'minute': 30},
                'open': {'day': 1, 'hour': 17, 'minute': 30}},
            {
                'close': {'day': 2, 'hour': 14, 'minute': 30},
                'open': {'day': 2, 'hour': 12, 'minute': 0}},
            {
                'close': {'day': 2, 'hour': 21, 'minute': 30},
                'open': {'day': 2, 'hour': 17, 'minute': 30}},
            {
                'close': {'day': 3, 'hour': 14, 'minute': 30},
                'open': {'day': 3, 'hour': 12, 'minute': 0}},
            {
                'close': {'day': 3, 'hour': 21, 'minute': 30},
                'open': {'day': 3, 'hour': 17, 'minute': 30}},
            {
                'close': {'day': 4, 'hour': 14, 'minute': 30},
                'open': {'day': 4, 'hour': 12, 'minute': 0}},
            {
                'close': {'day': 4, 'hour': 21, 'minute': 30},
                'open': {'day': 4, 'hour': 17, 'minute': 30}},
            {
                'close': {'day': 5, 'hour': 14, 'minute': 30},
                'open': {'day': 5, 'hour': 12, 'minute': 0}},
            {
                'close': {'day': 5, 'hour': 21, 'minute': 30},
                'open': {'day': 5, 'hour': 17, 'minute': 30}
            },
            {
                'close': {'day': 6, 'hour': 21, 'minute': 30},
                'open': {'day': 6, 'hour': 17, 'minute': 0}}
        ]

        result = get_periods(mock_data)

        self.assertEqual(result, expected_result)
