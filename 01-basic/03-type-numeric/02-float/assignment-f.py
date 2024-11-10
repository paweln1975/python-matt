"""
* Assignment: Type Float Volume
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Bottle volume is 500 mililiter
    2. Convert to fluid unces (floz) in imperial system (US)
    3. Convert to liters (liter) in metric system (SI)
    4. Run doctests - all must succeed

Polish:
    1. Objętość butelki wynosi 500 mililitrów
    2. Przelicz je na uncje płynu (floz) w systemie imperialnym (US)
    3. Przelicz je na litry (liter) w systie metrycznym (układ SI)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert volume_floz is not Ellipsis, \
    'Assign your result to variable `volume_floz`'
    >>> assert volume_l is not Ellipsis, \
    'Assign your result to variable `volume_l`'
    >>> assert type(volume_floz) is float, \
    'Variable `volume_floz` has invalid type, should be float'
    >>> assert type(volume_l) is float, \
    'Variable `volume_l` has invalid type, should be float'

    >>> result = round(volume_floz, 1)
    >>> pprint(result)
    16.9

    >>> result = round(volume_l, 1)
    >>> pprint(result)
    0.5
"""

liter = 1
milliliter = 0.001 * liter
floz = 0.02957344 * liter

VOLUME = 500 * milliliter

# VOLUME in fluid ounces
# type: float
volume_floz = VOLUME / floz

# VOLUME in liters
# type: float
volume_l = VOLUME / liter

