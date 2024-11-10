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
    2. Use enumerate() starting with 1
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `MONTH` w słownik:
        a. klucz: int - numer miesiąca
        b. wartość: str - nazwa miesiąca
    2. Użyj enumerate() zaczynając od 1
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict()`
    * `enumerate()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> 0 not in result
    True
    >>> 13 not in result
    True
    >>> result[1] == 'January'
    True

    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {1: 'January',
     2: 'February',
     3: 'March',
     4: 'April',
     5: 'May',
     6: 'June',
     7: 'July',
     8: 'August',
     9: 'September',
     10: 'October',
     11: 'November',
     12: 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

# number and month name
# type: dict[int,str]
result = ...

