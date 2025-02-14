
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = Distance(meters=1337)
>>> format(result, 'km')
'1.3 km'
>>> format(result, 'cm')
'133700.0 cm'
>>> format(result, 'm')
'1337.0 m'
"""
# endregion

# region Show Types
from typing import Callable
__format__: Callable[[object, str], str]
# endregion

METER = 1
CENTIMETER = METER * 0.01
KILOMETER = METER * 1000

# English
# 1. Overload `format()`
# 2. Has to convert length units: km, cm, m
# 3. Round result to one decimal place
# 4. Run doctests - all must succeed

# Polish
# 1. Przeciąż `format()`
# 2. Ma konwertować jednostki długości: km, cm, m
# 3. Wynik zaokrąglij do jednego miejsca po przecinku
# 4. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - 1 km = 1000 m
# - 1 m = 100 cm
# endregion

# %% Your code
class Distance:
    meters: int | float

    def __init__(self, meters):
        self.meters = meters

    def __format__(self, format_spec):
        match format_spec:
            case 'km':
                return '%0.1f km' % (self.meters / KILOMETER)
            case 'cm':
                return '%0.1f cm' % (self.meters / CENTIMETER)
            case 'm':
                return '%0.1f m' % self.meters
