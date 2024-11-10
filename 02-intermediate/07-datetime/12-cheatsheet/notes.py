#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/cheatsheet.html

#%% Datetime Cheatsheet



#%% Python
# from datetime import datetime, date, time, timedelta, timezone
# datetime(year, month, day, hour, minute, second, microsecond, tzinfo) - Create a datetime object
# date(year, month, day) - Create a date object
# time(hour, minute, second, microsecond) - Create a time object
# date.today() - Get the current date
# datetime.now() - Get the current date and time
# datetime.now(timezone.utc) - Get the current date and time in UTC
# datetime.datetime.strptime('1969-07-21 02:56:15', '%Y-%m-%d %H:%M:%S') - Parse a string into a datetime object
# dt.isoformat() - Get the current date and time in ISO 8601 format
# dt.strftime(dt, '%Y-%m-%d %H:%M:%S') - Format a datetime object as a string



#%% Directives
# %Y - Year with century as a decimal number, example: '1969'
# %m - Month as a zero-padded decimal number, example: '07'
# %d - Day of the month as a zero-padded decimal number, example: '21'
# %H - Hour (24-hour clock) as a zero-padded decimal number, example: '02'
# %M - Minute as a zero-padded decimal number, example: '56'
# %S - Second as a zero-padded decimal number, example: '15'
# %f - Microsecond as a decimal number, zero-padded on the left, example: '000000'
# %Z - Time zone name (empty string if the object is naive), example: 'UTC'
# %z - UTC offset in the form +HHMM or -HHMM (empty string if the object is naive), example: '+0000'
# %A - Weekday as locale's full name, example: 'Monday'
# %a - Weekday as locale's abbreviated name, example: 'Mon'
# %B - Month as locale's full name, example: 'July'
# %b - Month as locale's abbreviated name, example: 'Jul'
# %I - Hour (12-hour clock) as a zero-padded decimal number, example: '02'
# %p - Locale's equivalent of either AM or PM, example: 'AM'
# %y - Year without century as a zero-padded decimal number
# %G - ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V)
# %m - Month as a zero-padded decimal number
# %B - Month as locale's full name
# %b - Month as locale's abbreviated name
# %d - Day of the month as a zero-padded decimal number
# %a - Weekday as locale's abbreviated name
# %A - Weekday as locale's full name
# %u - ISO 8601 weekday as a decimal number where 1 is Monday
# %w - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
# %j - Day of the year as a zero-padded decimal number
# %H - Hour (24-hour clock) as a zero-padded decimal number
# %I - Hour (12-hour clock) as a zero-padded decimal number
# %p - Locale's equivalent of either AM or PM
# %Z - Time zone name (empty string if the object is naive)
# %z - UTC offset in the form +HHMM or -HHMM (empty string if the object is naive)
# %:z - UTC offset in the form ±HH:MM[:SS[.ffffff]] (empty string if the object is naive).
# %U - Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0
# %W - Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0
# %V - ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4
# %c - Locale's appropriate date and time representation
# %x - Locale's appropriate date representation
# %X - Locale's appropriate time representation
# %% - A literal % character



#%% Timezones
# timezone.utc - UTC timezone
# from zoneinfo import ZoneInfo
# ZoneInfo('Africa/Cairo') - Timezone object for Cairo, Egypt
# ZoneInfo('Asia/Tokyo') - Timezone object for Tokyo, Japan
# ZoneInfo('Australia/Sydney') - Timezone object for Sydney, Australia
# ZoneInfo('Europe/Warsaw') - Timezone object for Warsaw, Poland
# ZoneInfo('Europe/Paris') - Timezone object for Paris, France
# ZoneInfo('Europe/London') - Timezone object for London, England
# ZoneInfo('America/New_York') - Timezone object for New York, USA
# ZoneInfo('America/Los_Angeles') - Timezone object for Los Angeles, USA
# More timezones: https://python3.info/intermediate/datetime/tzdata.html