#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/timezones.html

#%% Datetime Timezone
# Always keep dates and times only in UTC (**important!**)
# Datetimes should be converted to local time only when displaying to user
# Computerphile Time & Time Zones [#ytComputerphileTimeZones]_
# Abolition of Time Zones [#wikiAbolitionOfTimeZones]_
# Since Python 3.9: :pep:615 -- Support for the IANA Time Zone Database in the Standard Library
# pip install tzdata



#%% Daylight Saving Time
# Daylight Saving Time date is different for each country and even US state
# Australia is 9h 30m shifted
# India is 3h 30m shifted
# Nepal is 3h 45m shifted
# In southern hemisphere the Daylight Saving Time is opposite direction
# They subtract hour in March and add in October
# Samoa is on the international date line
# Samoa changed from UTC-1200 to UTC+1200 for easier trades with Australia
# During World War II England was GMT+0200
# Libya in 2013 discontinued DST with couple of days notice
# Israel is on a different timezone than Palestine (multiple timezones in one location, based on nationality)
# Change from Julian to Gregorian calendar caused to skip few weeks
# In 18th century World change from Julian to Gregorian calendar
# In 20th century Russia change from Julian to Gregorian calendar (different days which was skipped than for worldwide change)
# In britain until 16th century the year started on 25th of March
# Mind leap seconds (add, subtract)
# UTC includes leap seconds
# Astronomical time does not include leap seconds
# Google invented smear second (on the day of leap second) they add a small fraction of a second to each second that day until midnight
# Not all cities has DST https://www.timeanddate.com/time/us/arizona-no-dst.html



#%% Timezone Naive Datetimes



#%% Timezone Aware Datetimes



#%% UTCNow
# datetime.utcnow() produces timezone naive datetimes!



#%% IANA Time Zone Database
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
# https://www.iana.org/time-zones
# https://pypi.org/project/tzdata/
# https://en.wikipedia.org/wiki/Time_in_Antarctica
# pip install tzdata



#%% ZoneInfo
# Since Python 3.9: :pep:615 -- Support for the IANA Time Zone Database in the Standard Library
# https://docs.python.org/3/library/zoneinfo.html