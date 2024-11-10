"""
* Assignment: Loop Unpack Months
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use `DATA: list[tuple]`
    2. Define `result: dict` with month number and name:
        a. Keys: month number
        b. Values: month name
    3. Use unpack syntax in a for loop
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: list[tuple]`
    2. Zdefiniuj `result: dict` z numerem miesiąca i nazwą:
        a. Klucz: numer miesiąca
        b. Wartość: nazwa miesiąca
    3. Użyj składni rozpakowania w pętli for
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(x in result.keys() for x in range(1, 13))
    >>> assert all(v in result.values() for k,v in DATA)

    >>> 13 not in result
    True
    >>> 0 not in result
    True

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

# Define `result: dict` with month number and name:
# - Keys: month number
# - Values: month name
# Use unpack syntax in a for loop
# type: dict[int,str]
result = {}

for number, month in DATA:
    result[number] = month

# trainer solution
result = dict(DATA)
