#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/exception/traceback.html

#%% Exception Traceback
# Traceback will help you track down the bug



#%% Fine Grained Error Locations
# Since Python 3.11
# :pep:657 -- Include Fine Grained Error Locations in Tracebacks



#%% Traceback Analysis
# Stacktrace is 8 levels deep, it's not Java's 200 ;)
# Start analysing traceback from bottom-up



#%% Change Verbosity Level
# Change level with sys.tracebacklimit
# Default traceback limit is 8
# From time to time you can have problems somewhere in the middle, but it's rare
# Last lines are the most important, in most cases error is there