"""
* Assignment: Type Float Altitude
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Plane altitude is 10 km
    2. Convert to feet (ft) in imperial system (US)
    3. Convert to meters (m) in metric system (SI)
    4. Run doctests - all must succeed

Polish:
    1. Wysokość lotu samolotem wynosi 10 km
    2. Przelicz je na stopy (ft) w systemie imperialnym (US)
    3. Przelicz je na metry (m) w systie metrycznym (układ SI)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert altitude_m is not Ellipsis, \
    'Assign your result to variable `altitude_m`'
    >>> assert altitude_ft is not Ellipsis, \
    'Assign your result to variable `altitude_ft`'
    >>> assert type(altitude_m) is float, \
    'Variable `altitude_m` has invalid type, should be float'
    >>> assert type(altitude_ft) is float, \
    'Variable `altitude_ft` has invalid type, should be float'

    >>> result = round(altitude_m, 1)
    >>> pprint(result)
    10000.0

    >>> result = round(altitude_ft, 1)
    >>> pprint(result)
    32808.4
"""

m = 1
km = 1000 * m
ft = 0.3048 * m

ALTITUDE = 10*km


# ALTITUDE in meters
# type: float
altitude_m = ALTITUDE / m

# ALTITUDE in feet
# type: float
altitude_ft = ALTITUDE / ft

