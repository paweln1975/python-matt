#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/iterator/zip.html

#%% Iterator  Zip
# Combine two sequences
# Generator (lazy evaluated)
# zip(*iterables, strict=False)
# required *iterables - 1 or many sequences or iterator object
# Iterate over several iterables in parallel, producing tuples with an item from each one.



#%% Problem



#%% Solution



#%% Inspect
# from inspect import isgeneratorfunction
# from inspect import isgenerator



#%% Lazy Evaluation



#%% As List



#%% As Dict



#%% Zip Shortest
# zip() adjusts to the shortest



#%% Strict
# zip(*iterables, strict=False)
# Since Python 3.10: :pep:618 -- Add Optional Length-Checking To zip [#pep618]_
# Source [#pydoczip]_



#%% Zip Longest
# from itertools import zip_longest
# zip_longest(*iterables, [fillvalue=None])



#%% Three-way Merge



#%% In For Loop