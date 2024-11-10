"""
* Assignment: Type Int Time
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define variables for breaks in work:
        a. workbreak: 5 minutes
        b. workday: 8 workbreak
        c. workweek: 5 workday
        d. workmonth: 4 workweek
    2. All variables must be in seconds
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne dla przerw w pracy:
        a. workbreak: 5 minut
        b. workday: 8 workbreak
        c. workweek: 5 workday
        d. workmonth: 4 workweek
    2. Wszystkie zmienne muszą być wyrażone w sekundach
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Multiply

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert workbreak is not Ellipsis, \
    'Assign your result to variable `workbreak`'
    >>> assert workday is not Ellipsis, \
    'Assign your result to variable `workday`'
    >>> assert workweek is not Ellipsis, \
    'Assign your result to variable `workweek`'
    >>> assert workmonth is not Ellipsis, \
    'Assign your result to variable `workmonth`'

    >>> assert type(workbreak) is int, \
    'Variable `workbreak` has invalid type, should be int'
    >>> assert type(workday) is int, \
    'Variable `workday` has invalid type, should be int'
    >>> assert type(workweek) is int, \
    'Variable `workweek` has invalid type, should be int'
    >>> assert type(workmonth) is int, \
    'Variable `workmonth` has invalid type, should be int'

    >>> pprint(workbreak)
    300
    >>> pprint(workday)
    2400
    >>> pprint(workweek)
    12000
    >>> pprint(workmonth)
    48000
"""


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY

# workbreak: 5 minutes
# type: int
workbreak = 5*MINUTE

# workday: 8 workbreak
# type: int
workday = 8*workbreak

# workweek: 5 workday
# type: int
workweek = 5*workday

# workmonth: 4 workweek
# type: int
workmonth = 4*workweek

