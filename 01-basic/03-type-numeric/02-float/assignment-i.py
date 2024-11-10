"""
* Assignment: Type Float Velocity
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Speed limit is 75 MPH
    2. Convert to miles per hour (mph) in imperial system (US)
    3. Convert to kilometers per hour (kph) in metric system (SI)
    4. Speed limit print in KPH (km/h)
    5. Run doctests - all must succeed

Polish:
    1. Ograniczenie prędkości wynosi 75 MPH
    2. Przelicz je na mile na godzinę (mph) w systemie imperialnym (US)
    3. Przelicz je na kilometry na godzinę (kph) w systie metrycznym (układ SI)
    4. Ograniczenie prędkości wypisz w KPH (km/h)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert speed_limit_mph is not Ellipsis, \
    'Assign your result to variable `speed_limit_mph`'
    >>> assert speed_limit_kph is not Ellipsis, \
    'Assign your result to variable `speed_limit_kph`'
    >>> assert type(speed_limit_mph) is float, \
    'Variable `speed_limit_mph` has invalid type, should be float'
    >>> assert type(speed_limit_kph) is float, \
    'Variable `speed_limit_kph` has invalid type, should be float'

    >>> result = round(speed_limit_mph, 1)
    >>> pprint(result)
    75.0

    >>> result = round(speed_limit_kph, 1)
    >>> pprint(result)
    120.7

"""

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

m = 1
km = 1000 * m
mi = 1609.344 * m
kph = km / HOUR
mph = mi / HOUR

SPEED_LIMIT = 75 * mph


# SPEED_LIMIT in miles per hour
# type: float
speed_limit_mph = SPEED_LIMIT / mph

# SPEED_LIMIT in kilometers per hour
# type: float
speed_limit_kph = SPEED_LIMIT / kph


