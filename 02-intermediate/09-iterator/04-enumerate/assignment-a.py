"""
* Assignment: Iterator Enumerate Start
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Convert `MONTH` into dict:
        a. key: int - month number
        b. value: str - month name
    2. Use enumerate()
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `MONTH` w słownik:
        a. klucz: int - numer miesiąca
        b. wartość: str - nazwa miesiąca
    2. Użyj enumerate()
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict()`
    * `enumerate()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result)
    >>> assert -1 not in result
    >>> assert 0 in result
    >>> assert 12 not in result
    >>> assert 13 not in result
    >>> assert result[0] == 'January'

    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())

    >>> pprint(result, width=30, sort_dicts=False)
    {0: 'January',
     1: 'February',
     2: 'March',
     3: 'April',
     4: 'May',
     5: 'June',
     6: 'July',
     7: 'August',
     8: 'September',
     9: 'October',
     10: 'November',
     11: 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

# number and month name
# type: dict[int,str]
result = ...

