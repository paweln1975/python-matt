#!/usr/bin/env python3
# https://python3.info/pandas/date/timedelta.html


# %% Date Shifts
# %%



# %% Between Time
# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.between_time.html
# %%



# %% Timedelta
# - Represents a duration, the difference between two dates or times
# - Difference expressed in: days, hours, minutes, seconds
# - Similar to datetime.timedelta from the standard library
# - Can be both positive and negative
# - https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html#timedelta-data
# %%



# %% DateOffset
# - A relative time duration that respects calendar arithmetic
# - If a date is Sat then adding a Bday will return the next Monday (next Business day) instead of a Saturday
# - Test if a date is in the DateOffset().onOffset(date)
# %%



