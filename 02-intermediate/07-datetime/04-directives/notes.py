#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/directives.html

#%% Datetime Directives
# Similar in almost all programming language
# Some minor differences like in JavaScript minutes are i, not M
# Source: [#pydocdtformat]_



#%% Frequently Used
# %Y - Year with century as a decimal number
# %m - Month as a zero-padded decimal number
# %d - Day of the month as a zero-padded decimal number
# %H - Hour (24-hour clock) as a zero-padded decimal number
# %M - Minute as a zero-padded decimal number
# %S - Second as a zero-padded decimal number
# %f - Microsecond as a decimal number, zero-padded on the left
# %Z - Time zone name (empty string if the object is naive)
# %z - UTC offset in the form +HHMM or -HHMM (empty string if the object is naive)
# %A - Weekday as locale's full name
# %a - Weekday as locale's abbreviated name
# %B - Month as locale's full name
# %b - Month as locale's abbreviated name
# %I - Hour (12-hour clock) as a zero-padded decimal number
# %p - Locale's equivalent of either AM or PM



#%% Year
# %Y - Year with century as a decimal number
# %y - Year without century as a zero-padded decimal number
# %G - ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V)



#%% Month
# %m - Month as a zero-padded decimal number
# %B - Month as locale's full name
# %b - Month as locale's abbreviated name



#%% Day
# %d - Day of the month as a zero-padded decimal number
# %a - Weekday as locale's abbreviated name
# %A - Weekday as locale's full name
# %u - ISO 8601 weekday as a decimal number where 1 is Monday
# %w - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
# %j - Day of the year as a zero-padded decimal number



#%% Hour
# %H - Hour (24-hour clock) as a zero-padded decimal number
# %I - Hour (12-hour clock) as a zero-padded decimal number
# %p - Locale's equivalent of either AM or PM



#%% Minute
# %M - Minute as a zero-padded decimal number



#%% Seconds
# %S - Second as a zero-padded decimal number



#%% Micro Seconds
# %f - Microsecond as a decimal number, zero-padded on the left



#%% Timezone
# %Z - Time zone name (empty string if the object is naive)
# %z - UTC offset in the form +HHMM or -HHMM (empty string if the object is naive)
# %:z - UTC offset in the form ±HH:MM[:SS[.ffffff]] (empty string if the object is naive).



#%% Week
# %U - Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0
# %W - Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0
# %V - ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4



#%% Presets
# %c - Locale's appropriate date and time representation
# %x - Locale's appropriate date representation
# %X - Locale's appropriate time representation



#%% Other
# %% - A literal % character