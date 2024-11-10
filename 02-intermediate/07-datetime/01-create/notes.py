#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/create.html

#%% Datetime Create
# datetime.date() - Date
# datetime.time() - Time
# datetime.datetime() - Date and time



#%% Custom Date and Time
# date(year, month, day) - create date
# time(hour, minute, second, microsecond) - create time
# datetime(year, month, day, hour, minute, second, microsecond) - create datetime



#%% Date Attributes
# date.year - year
# date.month - month
# date.day - day



#%% Time Attributes
# time.hour - hour
# time.minute - minute
# time.second - second
# time.microsecond - microsecond



#%% Datetime Attributes
# datetime.year - year
# datetime.month - month
# datetime.day - day
# datetime.hour - hour
# datetime.minute - minute
# datetime.second - second
# datetime.microsecond - microsecond



#%% Current Date and Time
# datetime.now() - current date and time
# date.today() - current date
# There is no time.now()



#%% Combine
# datetime.combine(d, t) - create datetime from date and time



#%% Split
# datetime.date() - get date from datetime
# datetime.time() - get time from datetime



#%% Empty Time
# def time(hour=0, minute=0, second=0, microsecond=0) - create time
# def datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0) - create datetime
# time() - midnight