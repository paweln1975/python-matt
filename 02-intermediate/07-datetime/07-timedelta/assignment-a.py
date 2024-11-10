"""
* Assignment: Datetime Timedelta Timeshift
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: date` with DATE + 4 days
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: date` z DATE + 4 dni
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is date, \
    'Variable `result` has invalid type, must be a date'

    >>> result
    datetime.date(2000, 1, 5)
"""

from datetime import date, timedelta


DATE = date(2000, 1, 1)


# Add 4 days to DATE
# type: date
result = ...

