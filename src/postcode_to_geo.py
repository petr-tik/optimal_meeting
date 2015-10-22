# -*- coding=utf-8 -*-

import requests
import pandas as pd
import matplotlib.pyplot as plt


# create a dataFrame from csv table
table = pd.read_table('../data/postcodes.csv', delimiter = ',', encoding = 'utf-8')


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
		table.set_value(idx, 'longitude', coordinates['result']['longitude'])
		table.set_value(idx, 'latitude', coordinates['result']['latitude'])
	
	
# goes through the column with postcodes passes a request to postcodes.io 
# and extracts the coordinates for each postcode
# it writes to a new csv file with coordinates


table.to_csv('../data/postcodes_final.csv', separator=',',header = True, index = False, mode = 'wb', encoding = 'utf-8')

