#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/files/mode-read.html

#%% File Read
# Works with both relative and absolute path
# Fails when directory with file cannot be accessed
# Fails when file cannot be accessed
# Uses context manager
# mode parameter to open() function is optional (defaults to mode='rt')



#%% Read From File
# Always remember to close file



#%% Read Using Context Manager
# Context managers use with ... as ...: syntax
# It closes file automatically upon block exit (dedent)
# Using context manager is best practice
# More information in Protocol Context Manager



#%% Read File at Once
# Note, that whole file must fit into memory



#%% Read File as List of Lines

with open('/file.txt', mode='rt') as file:
    for line in file:
        print(file)

#%% Reading File as Generator
# Use generator to iterate over other lines
# In those examples, file is a generator



#%% StringIO

from tempfile import NamedTemporaryFile

