#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/comprehensions/about.html

#%% Comprehension About
# Loop leaks out values

result = []
for x in range(0, 5):
    result.append(x)

#%% Syntax

result = [x for x in range(0, 5)]
print(x)

#%% Good Practices
# Use shorter variable names
# x is common name
