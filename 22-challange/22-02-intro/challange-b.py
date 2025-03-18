import calendar
import doctest


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

import pytest
from challenge.b import is_leap2  # Replace 'your_module' with the actual module name

@pytest.mark.parametrize("year, expected", [
    (2000, True),
    (1999, False),
    (1700, False),
    (1300, False),
    (1900, False),
    (2100, False),
    (2200, False),
    (2300, False),
    (2500, False),
    (2600, False),
    (2020, True),
    (2024, True),
    (1600, True),
    (2400, True),
])
def test_is_leap2(year, expected):
    assert is_leap2(year) == expected

def test_is_leap2_edge_cases():
    assert is_leap2(0) == True
    assert is_leap2(-4) == True
    assert is_leap2(-100) == False
    assert is_leap2(-400) == True

def test_is_leap2_type_error():
    with pytest.raises(TypeError):
        is_leap2("2000")
    with pytest.raises(TypeError):
        is_leap2(2000.0)




