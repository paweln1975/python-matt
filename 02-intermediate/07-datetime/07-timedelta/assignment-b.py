"""
* Assignment: Datetime Timedelta Age
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: date` age of a person born on `DATE`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: date` z wiekiem osoby urodzonej w `DATE`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is int, \
    'Variable `result` has invalid type, must be a int'

    >>> result
    24
"""

from datetime import date


DAY = 1
YEAR = 365.25 * DAY
DATE = date(2000, 1, 1)


# age of a person born on `DATE`
# type: int
result = ...

