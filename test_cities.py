import unittest
from city_country_function import city_country
class test_city_country(unittest.TestCase):
    def test_city_country(self):
        city_country1 = city_country('santiago', 'chile')
        self.assertEqual(city_country1, 'Santiago Chile')
    def test_city_country_population(self):
        city_country_population1 = city_country('santiago', 'chile', '5 000 000')
        self.assertEqual(city_country_population1, 'Santiago Chile- Population 5 000 000')
unittest.main()
