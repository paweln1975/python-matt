#!/usr/bin/env python3

# Reference:
# https://python3.info/matplotlib/figure/import-export.html

#%% Import/Export



#%% Reading data
# with open('filename.csv') - context manager
# numpy.loadtxt('filename.csv', delimeter=',', unpack=True)
# csv.DictReader()
# pandas DataFrame



#%% ``pandas`` and ``matplotlib``
# All of plotting functions expect np.array or np.ma.masked_array as input
# Classes that are 'array-like' such as pandas data objects and np.matrix may or may not work as intended
# It is best to convert these to np.array objects prior to plotting
# Convert a pandas.DataFrame:



#%% Exporting