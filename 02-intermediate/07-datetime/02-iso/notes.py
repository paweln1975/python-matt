#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/iso.html

#%% Datetime ISO Standard
# ISO 8601 is an International Standard [#wikiISO8601]_



#%% Dates
# Year-Month-Day
# Format: YYYY-mm-dd
# Example: 1969-07-21



#%% Time
# 24 hour clock
# Format: HH:MM:SS.ffffff or HH:MM:SS or HH:MM
# Example: 12:34, 12:34:56, 12:34:56.123456
# Optional seconds and microseconds
# 00:00 - midnight, at the beginning of a day
# 23:59:59.999999 - midnight, at the end of a day



#%% Date and Time
# Format: YYYY-mm-ddTHH:MM:SS.ffffff
# Example: 1969-07-21T02:56:15.123456
# "T" separates date and time)
# Optional seconds and microseconds



#%% Timezone
# Format: YYYY-mm-ddTHH:MM:SS.ffffffUTC
# Format: YYYY-mm-ddTHH:MM:SS.ffffffZ
# Example: 1969-07-21T02:56:15.123456+0200
# Optional seconds and microseconds
# "Z" (Zulu) means UTC



#%% Week
# Format: YYYY-Www
# The ISO 8601 definition for week 01 is the week with the first Thursday of the Gregorian year (i.e. of January) in it. [#wikisoweekdate]_
# 2009-W01 - First week of 2009
# 2009-W53 - Last week of 2009



#%% Weekday
# Format: YYYY-Www-dd
# Week starts on Monday
# ISO defines Monday as one
# Note year/month changes during the week
# 2009-W01-1 - Monday 29 December 2008
# 2009-W53-7 - Sunday 3 January 2010



#%% Duration
# Format: P...Y...M...DT...H...M...S
# Example: P8Y3M8DT20H49M15S
# P - period - placed at the start of the duration representation
# Y - number of years
# M - number of months
# W - number of weeks
# D - number of days
# T - precedes the time components of the representation
# H - number of hours
# M - number of minutes
# S - number of seconds



#%% To ISO Format
# datetime.isoformat()
# date.isoformat()
# time.isoformat()



#%% From ISO Format
# datetime.fromisoformat()
# date.fromisoformat()
# time.fromisoformat()