#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
import pandas as pd
import matplotlib.pyplot as plt


# create a dataFrame from csv table
table = pd.read_table('data/postcodes.csv', delimiter = ',', encoding = 'utf-8')

# convert pandas Dataframe into a dictionary, where the row index is key
# and value is another dict
table_as_dict = table.to_dict(orient = 'index')

df = pd.DataFrame.from_dict(table_as_dict)

class Traveller(object):
    """ A traveller whose route has to be taken into account

    Properties include:
        start_postcode - usually office
        finish_postcode - usually home
        mode - transport mode - bike, tube, car, walk, bus
        start_coor - starting coordinates
        finish_coor - finish coordinates        

        """

    def __init__(self, name):
    
        self.start_postcode = start_postcode
        self.finish_postcode = finish_postcode
        self.mode = mode
        self.start_coor = []
        self.finish_coor = []

    def GeoConverter(self, postcode):
    """
    converts postcode into latitude and longitude

    returns a list of longitude and latitude values

    """

        api_call = requests.get('https://api.postcode.io/postcodes/{}'.format(postcode))
        if api_call['status'] != 200:
            print "Error {}".format(api_call)
        elif api_call['status'] == 200:         
            result = api_call.json()['result']
            self.coor = [result['longitude'], result['latitude']]
            return self.coor

    



"""

# calling a Series from a pandas dataFrame you can turn it into a list by .tolist()
for postcode in table['postcode'].tolist():
	# make a request with each postcode
	coordinates = requests.get('https://api.postcodes.io/postcodes/{}'.format(postcode)).json()
	idx = table[table['postcode'] == postcode].index

	# handle errors
	if coordinates['status'] == 404:
		pass
		#table.set_value(idx,'longitude',0)
		#table.set_value(idx, 'latitude',0)
	# without errors
	elif coordinates['status'] != 200:
		print "Error code"	
	else:
		# index of a dataframe returns an integer value given a particular condition
        for loc_field in ['longitude', 'latitude']:		
            table.set_value(idx, loc_field, coordinates['result'][loc_field])
		    
	
# goes through the column with postcodes passes a request to postcodes.io 
# and extracts the coordinates for each postcode
# it writes to a new csv file with coordinates


table.to_csv('data/postcodes_final.csv', separator=',',header = True, 
                        index = False, mode = 'wb', encoding = 'utf-8')
"""
