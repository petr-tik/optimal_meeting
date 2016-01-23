#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


# define search space

# load the dataframe and extract longitude and latitude


class SearchSpace():
    """ define the search space class, which will call data from the table, 
        collect all longitudes and latitudes
        make a recangular search space
        increment
    """
    def __init__(self, table, longitudes, latitudes):
	    self.coordinates = pd.read_table('data/postcodes_final.csv', 
                                            delimiter = ',', encoding = 'utf-8')
        self.needed_columns = ['longitude', 'latitude']
	    # create a dictionary where different values will be stored
        self.longitudes = self.coordinates['longitude'].tolist()
        self.latitudes = self.coordinates['latitude'].tolist()	    
	

    def parameters(self, increment):
        pass


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

