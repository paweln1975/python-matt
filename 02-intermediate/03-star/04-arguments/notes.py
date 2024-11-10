#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/star/arguments.html

#%% Star Arguments
# Unpack and Arbitrary Number of Parameters and Arguments



#%% Recap
# Argument - value passed to the function
# Argument can be: positional or keyword
# Positional arguments - resolved by position, order is important, must be at the left side
# Keyword arguments - resolved by name, order is not important, must be on the right side
# After first keyword argument, all following arguments must also be keyword



#%% Positional Arguments
# echo(*data) - unpacks from tuple, list or set
# * is used for positional arguments
# There is no convention, so you can use any name, for example *data



#%% Keyword Arguments
# echo(**data) - unpacks from dict
# ** is used for keyword arguments
# There is no convention, so you can use any name, for example **data



#%% Positional and Keyword Arguments
# echo(*data1, **data2) - unpacks from tuple, list, set and dict
# * is used for positional arguments
# ** is used for keyword arguments
# There is no convention, so you can use any name, for example *data1
# There is no convention, so you can use any name, for example **data2



#%% Merge Kwargs
# echo(**data1, **data2)



#%% Merge Dicts
# dict(**data1, **data2)
# {**data1, **data2}
# data1 | data2 - since Python 3.9



#%% Create One Object



#%% Create Many Objects



#%% Merge



#%% Recap