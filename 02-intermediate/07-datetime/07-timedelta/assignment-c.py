"""
* Assignment: Datetime Timedelta Age
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. How old was Yuri Gagarin when he was launched to space?
    2. Result round to full years
    3. Run doctests - all must succeed

Polish:
    1. Ile miał lat Juri Gagarin kiedy wystartował w kosmos?
    2. Rezultat zaokrąglij do pełnych lat
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is int, \
    'Variable `result` has invalid type, must be a int'

    >>> result
    27
"""

from datetime import date, datetime


DAY = 1
YEAR = 365.25 * DAY

BIRTHDATE = date(1934, 3, 9)
LAUNCH_DATE = date(1961, 4, 12)

# Gagarin's age when he was launched to space
# type: int
result = ...


