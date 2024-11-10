#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/standards.html

#%% Datetime Standards
# Date and time formats varies from country to country [#wikiDateTimeFormats]_



#%% Date



#%% 12 and 24 Hour Clock
# What AM stands for?
# What PM stands for?



#%% Noon and Midnight
# Confusion at noon and midnight [#wikiNoonMidnight]_
# Which time is a midnight?
# Which time is a noon?



#%% Exactly Midnight
# 00:00:00.000000 - day start, exactly midnight
# 23:59:59.999999 - day end, excluding last microsecond
# 24:00:00.000000 - day end, including last microsecond



#%% After Midnight
# Times after Midnight [#wikiTimesAfter2400]_



#%% Leap Second
# International Earth Rotation and Reference Systems Service (IERS)
# UTC leap second [#wikiLeapSecond]_
# Leap second discontinuation post 2035 [#natureLeapSecond]_
# Issues created by insertion (or removal) of leap seconds
# Calculation of time differences and sequence of events
# Missing leap seconds announcement
# Implementation differences
# Textual representation of the leap second
# Binary representation of the leap second
# Other reported software problems associated with the leap second
# June 30th or December 31st
# Introduced in 1972
# Last leap second (to date) was in 2016



#%% Zero Padded
# Zero padded minutes, seconds and microseconds but not hours
# Variable length microseconds



#%% Roman Numerals
# In latin V is read as U
# In latin I is read as J
# In latin IV is read as JU
# JU stands for Jupyter - roman god
# Louis XIV did not like IV and changed to IIII [#watchmaster]_
# There is a symetry in groups of four I, II, III, IIII, V, VI, VII, VIII, IX, X, XI, XII



#%% Calendars
# Julian Calendar [#wikiJulianCalendar]_
# Gregorian Calendar [#wikiGregorianCalendar]_
# Introduced by Pope Gregory XIII in October 1582
# Saudi Arabia was the last country to adopt Gregorian calendar in 2016
# There are only four countries which have not adopted the Gregorian calendar: Ethiopia (Ethiopian calendar), Nepal (Vikram Samvat and Nepal Sambat), Iran and Afghanistan (Solar Hijri calendar)
# List of adoption dates of the Gregorian calendar by country [#wikiGregorianCalendarAdoption]_



#%% Astronomy
# Synodic day - the period for a celestial object to rotate once in relation to the star it is orbiting [#wikiSynodicDay]_
# Solar time - calculation of the passage of time based on the position of the Sun in the sky [#wikiSolarTime]_
# Epoch (astronomy) [#wikiEpochAstronomy]_
# Sidereal Time [#wikiSiderealTime]_
# JD - Julian Day [#wikiJulianDay]_



#%% Databases
# SQLite dates and time are stored as TEXT, INTEGER or REAL values.
# TEXT as ISO-8601 strings ('YYYY-MM-DDTHH:MM:SS.SSS').
# INTEGER as timestamp, the number of seconds since 1970-01-01 00:00:00 UTC.
# REAL as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the Gregorian calendar.



#%% Space Industry
# UTC - Coordinated Universal Time [#wikiCoordinatedUniversalTime]_
# GMT - Greenwich Mean Time [#wikiGreenwichMeanTime]_
# MET - Mission Elapsed Time
# Relativistic effects
# Time dilatation due to speed approaching speed of light



#%% Planet Mars
# MSD - Mars Sol Date [#wikiMarsSolDate]_
# MTC - Coordinated Mars Time [#wikiCoordinatedMarsTime]_
# Timekeeping on Mars [#wikiTimekeepingOnMars]_
# Mars Clock [#wikiMarsClock]_
# Martian sidereal day is 24 h 37 m 22.663 s (88,642.663 seconds)
# Martian solar day is 24 h 39 m 35.244 s (88,775.244 seconds)



#%% Military Time
# Military time [#wikiMilitaryTime]_
# Military time zones [#wikiMilitaryTimezones]_
# 24 hour clock



#%% Decimal Time
# Unix time gives date and time as the number of seconds since January 1, 1970
# Microsoft's FILETIME as multiples of 100ns since January 1, 1601 [#wikiMetricTime]_
# VAX/VMS uses the number of 100ns since November 17, 1858 [#wikiMetricTime]_
# RISC OS the number of centiseconds since January 1, 1900 [#wikiMetricTime]_



#%% Other
# Swatch Internet Time - Beats @300 [#wikiSwatchInternetTime]_
# sidereal day on Earth is approximately 86164.0905 seconds (23 h 56 min 4.0905 s or 23.9344696 h)