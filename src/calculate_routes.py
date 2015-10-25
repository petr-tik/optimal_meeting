# -*- coding=utf-8 -*-


import search_space
import pandas as pd
import requests
import numpy as np


table = pd.read_table('data/postcodes_final.csv', sep = ',', encoding = 'utf-8', index_col = 0)

# only consider valid coordinate values
table = table.dropna()
# call the method define from module search_space and create a dictionary of values
parameters = search_space.define_search_space()
# make a list of name strings 
names_list = table.index.values.tolist()

store_results = pd.DataFrame()

# define myrange function to pass float like longitude and latitude
def myrange(a, b, c):
	x = a
	while x < b:
	  yield x
	  x += c
	  
# take name, look up the respective coordinates, pass them into tfl api

def calc_travel(name, dest_lat, dest_long):
	# .loc allows you to select data based on row and column labels, .tolist() turns the selection into a list
	departure = table.loc[name, ['latitude', 'longitude']].tolist()
	destination = [dest_lat, dest_long]
	# tfl authentication details 
	App_ID = 'c33e8e43'
	Key = '9c1e8ae73df1b9424c8b285eb5bc81f8'
	# URL composition
	URL = 'https://api.tfl.gov.uk/Journey/JourneyResults/{},{}/to/{},{}?nationalSearch=False&&&timeIs=Departing&&&&&&&&&&&&&alternativeCycle=False&alternativeWalking=False&applyHtmlMarkup=False&useMultiModalCall=False&app_id={}&app_key={}'.format(departure[0], departure[1], destination[0], destination[1], App_ID, Key)

	r = requests.get(URL)
	if r.status_code == 200:
	
		content = r.json()
		# make a dictionary with numerical keys and value that 
		journeys = content['journeys']
		journeys_dict = {key : content['journeys'][key] for key in xrange(len(journeys))}

		# find which one 
		min_key = min(journeys_dict, key=journeys_dict.get)
		
		# use the min_key to take the quickest journey
		shortest_trip = journeys[min_key]

		# the duration of the shortest trip 
		min_duration = shortest_trip['duration']		
		# a list of transport modes used
		description = [shortest_trip['legs'][x]['mode']['id'] for x in xrange(len(shortest_trip['legs']))]
		
		# return a dictionary describing each plotted journey by destination, name and the shortest trip
		return {'name' : name, 'destination' : destination, 'trip' : {'duration' : min_duration, 'description' : description}}	
			
	else:
		print "Something fishy is going on"
		pass


for long in myrange(parameters['longitude']['lower_bound'], parameters['longitude']['upper_bound'], parameters['longitude']['increment']):
	for lat in myrange(parameters['latitude']['lower_bound'], parameters['latitude']['upper_bound'], parameters['latitude']['increment']):
		for name in names_list: 
			res = calc_travel(name, lat, long)
			
