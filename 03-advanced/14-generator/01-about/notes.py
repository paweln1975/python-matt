#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/generator/about.html

#%% Generator About
# Processes one element at a time
# Does not remember previous element
# Does not know next element
# Can be used only once
# Save memory (does not require more memory for processing large data)
# Uses around 10% more CPU than regular processing
# Typical usage: streams, processing larger than memory files or data
# Cannot use len() as of generators don't have length
# Previous element is overridden by current on next()
# Functions (list, dict, tuple, frozenset, set, sum, all, any, etc) will evaluate generator instantly



#%% Plain Function
# Plain function returns plain object



#%% Generator Function
# Generator function returns generator object



#%% Yield vs Return
# After return function stops
# After yield function pauses



#%% Lazy Evaluation
# After yield function pauses
# Calling next() resumes function until next yield
# After last yield raises StopIteration



#%% Instant Evaluation
# Using list() will evaluate generator instantly
# Functions (list, tuple, set,  dict, sum, min, max, all, any, etc) will evaluate generator instantly