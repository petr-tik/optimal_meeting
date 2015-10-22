# -*- coding=utf-8 -*-


import search_space
import pandas as pd
import requests
import numpy as np


table = pd.read_table('data/postcodes_final.csv', sep = ',', encoding = 'utf-8', index_col = 0)

# only consider valid coordinate values
table = table.dropna()
print table
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
	print "This is departure coordinates for {}:".format(name), departure
	destination = [dest_lat, dest_long]
	print "The destination coordinates are:", destination
	# tfl authentication details 
	App_ID = 'c33e8e43'
	Key = '9c1e8ae73df1b9424c8b285eb5bc81f8'
	URL = 'https://api.tfl.gov.uk/Journey/JourneyResults/{},{}/to/{},{}?nationalSearch=False&&&timeIs=Departing&&&&&&&&&&&&&alternativeCycle=False&alternativeWalking=False&applyHtmlMarkup=False&useMultiModalCall=False&app_id={}&app_key={}'.format(departure[0], departure[1], destination[0], destination[1], App_ID, Key)
	r = requests.get(URL)
	if r.status_code == 200:
		print "We are good, let's go"
	
		content = r.json()
		trips_durations = [content['journeys'][i]['duration'] for i in xrange(len(content['journeys']))]
		print trips_durations
	
		# yield the shortest trip option 	
		shortest_trip = min(trips_durations)
		print "The shortest trip for {} from {} to {} is {} minutes long".format(name, departure, destination, shortest_trip)
		return departure, destination, shortest_trip		
	else:
		pass


dest_to_times = {}	
for long in myrange(parameters['longitude_lower_bound'], parameters['longitude_upper_bound'], parameters['longitude_increment']):
	for lat in myrange(parameters['latitude_lower_bound'], parameters['latitude_upper_bound'], parameters['latitude_increment']):
		for name in names_list: 
			res = calc_travel(name, lat, long)
			if not res:
			    continue
		    (departure, destination, shortest_trip) = res
		    dest_to_times.setdefault(destination, []).append(shortest_trip)

dest_stdevs = [(dest, np.stdev(times)) for (dest, times) in dest_to_times]

# now sort them
dest_stdevs.sort(key=lambda pair: pair[1])

best_dest = dest_stdevs[0][0]
