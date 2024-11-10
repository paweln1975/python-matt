#!/usr/bin/env python3

# Reference:
# https://python3.info/database/sql/sql-datatypes.html

#%% SQL Data Types
# Python None  -> SQLite3 NULL
# Python int   -> SQLite3 INTEGER
# Python float -> SQLite3 REAL
# Python str   -> SQLite3 TEXT
# Python bytes -> SQLite3 BLOB



#%% NULL Type
# The value is a undefined value



#%% INTEGER Type
# The value is a signed integer
# Stored in 1, 2, 3, 4, 6, or 8 bytes
# Depending on the magnitude of the value



#%% REAL Type
# The value is a floating point value
# Stored as an 8-byte IEEE floating point number



#%% TEXT Type
# The value is a text string
# Stored using the database encoding (ie. UTF-8)



#%% BLOB Type
# Binary Large Object
# The value is a blob of data
# Stored exactly as it was input



#%% NUMERIC Affinity
# May contain values using all five storage classes



#%% DATETIME Affinity