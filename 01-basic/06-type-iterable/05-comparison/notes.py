#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-iterable/comparison.html

#%% Iterable Comparison
# tuple - fast and memory efficient
# list - extensible and flexible
# set - unique elements, fast lookup



#%% Tuple
# Immutable - cannot add, modify or remove items
# Stores elements of any type
# Keeps order of inserting elements
# Possible to getitem and slice
# Elements can duplicate
# One contingent block of data in memory



#%% List
# Mutable - can add, remove, and modify items
# Stores elements of any type
# Keeps order of inserting elements
# Possible to getitem and slice
# Elements can duplicate
# Implemented in memory as list of references to objects
# Objects are scattered in memory



#%% Set
# Mutable - can add, remove, and modify items
# Stores only **hashable** elements (int, float, bool, None, str, tuple)
# Does not keep order of inserting elements
# It is not possible to getitem and slice
# Elements cannot duplicate
# Set is unordered data structure and do not record element position or insertion



#%% Memory Footprint



#%% Memory



#%% Performance
# O(n) - lookup (contains) in list and tuple
# O(1) - lookup (contains) in set
# [#pywikiTimeComplexity]_