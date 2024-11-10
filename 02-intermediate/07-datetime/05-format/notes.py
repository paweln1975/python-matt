#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/format.html

#%% Datetime Format
# format(dt, '%Y-%m-%d')
# f'Today is {dt:%Y-%m-%d}'
# dt.strftime('%Y-%m-%d')



#%% Formats
# format(dt, '%Y-%m-%d')



#%% Leading Zero
# %#H - remove leading zero (Windows)
# %-H - remove leading zero (macOS, Linux, \*nix)
# %_H - replace leading zero with space (macOS, Linux, \*nix)
# Works only with formatting
# raises ValueError while parsing [#pydocdtformat]_



#%% String Format Time
# datetime.strftime()



#%% Format String