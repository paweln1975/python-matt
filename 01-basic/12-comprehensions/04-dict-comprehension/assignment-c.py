"""
* Assignment: Comprehension Dict Months
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Convert `DATA` into `result: dict`:
        a. Keys: month number
        b. Values: month name
    2. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` w `result: dict`:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

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

    >>> pprint(result)
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

DATA = [
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
]

# number and month name
# type: dict[str,str]
result = {idx: month for idx, month in DATA}


