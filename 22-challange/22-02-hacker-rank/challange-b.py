import calendar
import pytest


def is_leap(year, build_in = True):
    """
    Determines whether a given year is a leap year.

    This function checks if the provided year is a leap year using either the built-in
    calendar module or a custom implementation.

    Parameters:
        year (int): The year to check for leap year status.
        build_in (bool, optional): Flag to determine which method to use for checking.
            If True (default), uses the calendar.isleap() function.
            If False, uses a custom implementation (is_leap2 function).

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Notes:
        - The function relies on the calendar module when build_in is True.
        - When build_in is False, it calls an external function is_leap2, which is not
        defined in this snippet and should be implemented separately.
        - The function includes example usage and test cases in its docstring.

    Examples:
        >>> is_leap(2000)
        True
        >>> is_leap(1999)
        False
        >>> is_leap(1900)
        False
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
    if build_in:
        return calendar.isleap(year)
    else:
        return is_leap2(year)

def is_leap2(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

