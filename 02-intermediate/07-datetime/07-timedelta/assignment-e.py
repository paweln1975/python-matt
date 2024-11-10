"""
* Assignment: Datetime Timedelta Duration
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Calculate how many years passed between Gagarin's launch
       and Armstrong's first step on the Moon
    2. Assume:
        a. year = 365.25 days
        b. month = 30.4375 days
    3. Result round to two decimal places
    4. Run doctests - all must succeed

Polish:
    1. Podany jest czas, który upłynął między startem Gagarina
       a pierwszym krokiem Armstronga na Księżycu
    2. Uwzględnij założenie:
        a. rok = 365.25 dni
        b. miesiąc = 30.4375 dni
    3. Rezultat zaokrąglij do dwóch miejsc po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is float, \
    'Variable `result` has invalid type, must be a float'

    >>> result
    8.27
"""

from datetime import datetime


DAY = 1
YEAR = 365.25 * DAY

GAGARIN = datetime(1961, 4, 12, 6, 7)
ARMSTRONG = datetime(1969, 7, 21, 2, 56, 15)

# Number of years rounded to 2 decimal place
# type: float
result = ...

