#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/functional/paradigm-pure-function.html

#%% Functional Pure Functions
# Pure functions have no side effects (i.e. memory, state, I/O)
# Calling the pure function again with the same arguments returns the same result (this can enable caching optimizations such as memoization)
# If the result of a pure expression is not used, it can be removed without affecting other expressions
# If there is no data dependency between two pure expressions, their order can be reversed, or they can be performed in parallel and they cannot interfere with one another (the evaluation of any pure expression is thread-safe) [#WikipediaFunc]_



#%% Pure Function



#%% Impure Function



#%% Impure to Pure Function



#%% Side Effects
# I/O - Input Output
# Looks like a pure function
# File content can change by other process