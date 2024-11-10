#!/usr/bin/env python3

# Reference:
# https://python3.info/pandas/dataframe/mapping.html

#%% DataFrame Mapping
# Series.map() - Map values of Series according to an input mapping or function
# Series.apply() - Invoke function on values of Series
# DataFrame.apply() - Apply a function along an axis of the DataFrame
# DataFrame.applymap() - Apply a function to a Dataframe elementwise
# DataFrame.pipe() - Apply chainable functions that expect Series or DataFrames
# DataFrame.where(cond, sub) - Replace values where the condition is False
# DataFrame.mask(cond, sub) - Replace values where the condition is True
# Series.str.split(regex, expand=True) - Split strings around given separator/delimiter
# Series.str.extract(regex, expand=True) - Extract capture groups in the regex pat as columns in a DataFrame
# Series.str.extractall() - Extract capture groups in the regex pat as columns in DataFrame
# Series.str.findall(regex) - Find all occurrences of pattern or regular expression in the Series/Index
# Series.str.fullmatch(regex) - Determine if each string entirely matches a regular expression
# Series.dt.strftime(...) - formatted strings specified by date_format, which supports the same string format as the python standard library
# Series.dt.date - Returns numpy array of python datetime.date objects
# Series.dt.time - Returns numpy array of datetime.time objects
# Series.dt.timez - Returns numpy array of datetime.time objects with timezone information



#%% Map
# Works only on Series
# Argument: dict, Series, or Callable
# Works element-wise on a Series
# Operate on one element at time
# When passed a dictionary/Series will map elements based on the keys in that dictionary/Series, missing values will be recorded as NaN in the output
# Is optimised for elementwise mappings and transformation
# Operations that involve dictionaries or Series will enable pandas to use faster code paths for better performance [#stackoverflowMapApplyApplyMap]_



#%% Apply
# Works on both Series and DataFrame
# Argument: Callable
# On Series: operate on one element at time
# On DataFrame: elementwise but also row / column basis
# Suited to more complex operations and aggregation
# The behaviour and return value depends on the function
# Returns a scalar for aggregating operations, Series otherwise. Similarly for DataFrame.apply
# Has fastpaths when called with certain NumPy functions such as mean, sum, etc. [#stackoverflowMapApplyApplyMap]_



#%% Applymap
# Works only on DataFrame
# Argument: Callable
# Works element-wise on a DataFrame
# Operate on one element at time
# In more recent versions has been optimised for some operations
# You will find applymap slightly faster than apply in some cases.
# Test both and use whatever works better [#stackoverflowMapApplyApplyMap]_



#%% Summary



#%% Differentiation