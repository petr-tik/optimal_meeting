import unittest
from src.search_space import Search_space
"""
search space will be defined by (min, max)&(longitude, latitude)


the right test function will make sure all longitude and latitude values available are within the range 
"""


class Search_space(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()

		pass


	def tearDown(self):
		del self.config

	def test_search_space(self, coordinates, longitudes, latitudes):
		self.coordinates = # get all coordinates as list of tuples (longitude and latitude) for all users
		self.latitudes = # pull out all relevant 
		self.longitudes = # 






