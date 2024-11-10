#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/structural/flyweight.html

#%% Flyweight
# EN: Flyweight
# PL: Pyłek
# Type: object



#%% Pattern
# In applications with large number of objects
# Objects take significant amount of memory
# Reduce memory consumed by objects



#%% Problem
# Imagine mapping application, such as: Open Street Maps, Google Maps, Yelp, Trip Advisor etc.
# There are thousands points of interests such as Cafe, Shops, Restaurants, School etc.
# Icons can take a lot of memory, times number of points on the map
# It might crash with out of memory error (especially on mobile devices)



#%% Solution
# Separate the data you want to share from other data
# Pattern will create a dict with point type and its icon
# It will reuse icon for each type
# So it will prevent from storing duplicated data in memory