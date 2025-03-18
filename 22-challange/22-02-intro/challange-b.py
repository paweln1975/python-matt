"""
>>> is_leap(2000)
True

>>> is_leap(1999)
False

>>> is_leap(1700)
False

>>> is_leap(1300)
False

>>> is_leap(1900)
False

>>> is_leap(2100)
False

>>> is_leap(2200)
False

>>> is_leap(2300)
False

>>> is_leap(2500)
False

>>> is_leap(2600)
False
"""
import calendar


def is_leap(year, build_in = True):
    # Write your logic here
    if build_in:
        return calendar.isleap(year)
    else:
        return is_leap2(year)

def is_leap2(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
