# -*- coding=utf-8 -*-

import pandas as pd


# define search space

# load the dataframe and extract longitude and latitude


def define_search_space():

	coordinates = pd.read_table('../data/postcodes_final.csv', delimiter = ',', encoding = 'utf-8')
	needed_columns = ['longitude', 'latitude']
	# create a dictionary where different values will be stored
	space_parameters = []
	
	# iterate over 2 relevant columns
	for column_name in needed_columns:
		column_name = dict()
		print "Creating a dictionary called {}".format(column_name), column_name
		# for each: long and latitude, make a list with all the values
		# store different values under different keys
		column_name['all_values'] = coordinates[column_name].tolist()		
		column_name['lower_bound'] = min(space_parameters['{}_all_values'.format(column_name)]) + 0.25*(max(space_parameters['{}_all_values'.format(column_name)]) - min(space_parameters['{}_all_values'.format(column_name)]))
		column_name['upper_bound'] = min(space_parameters['{}_all_values'.format(column_name)]) + 0.75*(max(space_parameters['{}_all_values'.format(column_name)]) - min(space_parameters['{}_all_values'.format(column_name)]))
		column_name['increment'] = (max(space_parameters['{}_all_values'.format(column_name)]) - min(space_parameters['{}_all_values'.format(column_name)]))/2
		space_parameters.append(column_name) 
	
	return space_parameters
# the search space is the rectangle between lower quartile latitude/longitude and upper quarter latitude/longitude

list = define_search_space()
print list
