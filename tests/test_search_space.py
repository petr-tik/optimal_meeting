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

	def __init__(self, coordinates, longitudes, latitudes):
		self.coordinates = # get all coordinates as list of tuples (longitude and latitude) for all users
		self.latitudes = # pull out all relevant 
		self.longitudes = # 

	def test_every_point_within_boundaries(self):
		# make sure all values are between min and max latitudes and longitudes respectively 
		for latit in self.latitudes:
			self.assertGreaterEqual(latit, min(latitudes))
			self.asserLessEqual(latit, max(latitudes))


		for longit in self.longitudes:
			self.assertGreaterEqual(longit, min(longitudes))
			self.assertLessEqual(longit, max(longitudes))

	def test_good_increment(self):
		# make sure the increment produced by the calculator is meaningful


	def test_lengths_match(self):
		# make sure the number of registered people matches the number of latitudes and longitudes
		self.assertEqual(len(members), len(self.longitudes))
		self.assertEqual(len(members), len(self.latitudes))




if __name__ == '__main__':
	unittest.main()


