#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/functional/paradigm-memoization.html

#%% Functional Memoization



#%% Problem
# Calling the same function with the same parameter
# Requires computation every time the function is called



#%% Solution
# Memoization - remembering function results for given parameter
# Store information in external dict
# key: function parameter
# value: function call result for given parameter
# Dicts are very fast



#%% LRU cache
# Least Recently Used
# from functools import lru_cache
# @lru_cache(maxsize=None)



#%% Performance
# Date: 2024-08-22
# Python: 3.12.5
# IPython: 8.26.0
# Computer: MacBook M3 Max, 16 cores (12 performance and 4 efficiency) / 3nm, 128 GB RAM LPDDR5
# System: macOS 14.5