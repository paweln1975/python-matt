"""
* Assignment: Datetime Timedelta Age
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. How old was Neil Armstrong when he made a first step on the Moon?
    2. Result round to full years
    3. Mind, that there are two different objects: `date` and `datetime`
    4. Run doctests - all must succeed

Polish:
    1. Ile lat miał Neil Armstrong kiedy zrobił pierwszy krok na Księżycu?
    2. Rezultat zaokrąglij do pełnych lat
    3. Zwróć uwagę, że tam są dwa różne obiekty: `date` i `datetime`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is int, \
    'Variable `result` has invalid type, must be a int'

    >>> result
    38
"""

from datetime import date, datetime


DAY = 1
YEAR = 365.25 * DAY

BIRTHDATE = date(1930, 8, 5)
FIRST_STEP = datetime(1969, 7, 21, 2, 56, 15)

# Armstrong's age when he made a first step on the Moon
# type: int
result = ...


