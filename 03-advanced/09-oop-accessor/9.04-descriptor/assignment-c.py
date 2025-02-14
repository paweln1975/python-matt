"""
Name: Accessor Descriptor Inheritance
Difficulty: medium
Lines: 23
Minutes: 13

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> place1 = GeographicCoordinate(50.0, 120.0, 8000.0)
>>> place1
GeographicCoordinate(latitude=50.0, longitude=120.0, elevation=8000.0)

>>> place2 = GeographicCoordinate(22.0, 33.0, 44.0)
>>> place2
GeographicCoordinate(latitude=22.0, longitude=33.0, elevation=44.0)

>>> place1.latitude = 1.0
>>> place1.longitude = 2.0
>>> place1
GeographicCoordinate(latitude=1.0, longitude=2.0, elevation=8000.0)

>>> place2
GeographicCoordinate(latitude=22.0, longitude=33.0, elevation=44.0)

>>> GeographicCoordinate(90.0, 0.0, 0.0)
GeographicCoordinate(latitude=90.0, longitude=0.0, elevation=0.0)
>>> GeographicCoordinate(-90.0, 0.0, 0.0)
GeographicCoordinate(latitude=-90.0, longitude=0.0, elevation=0.0)
>>> GeographicCoordinate(0.0, +180.0, 0.0)
GeographicCoordinate(latitude=0.0, longitude=180.0, elevation=0.0)
>>> GeographicCoordinate(0.0, -180.0, 0.0)
GeographicCoordinate(latitude=0.0, longitude=-180.0, elevation=0.0)
>>> GeographicCoordinate(0.0, 0.0, +8848.0)
GeographicCoordinate(latitude=0.0, longitude=0.0, elevation=8848.0)
>>> GeographicCoordinate(0.0, 0.0, -10994.0)
GeographicCoordinate(latitude=0.0, longitude=0.0, elevation=-10994.0)

>>> GeographicCoordinate(-91.0, 0.0, 0.0)
Traceback (most recent call last):
ValueError: Out of bounds, must be between -90.0 and 90.0

>>> GeographicCoordinate(+91.0, 0.0, 0.0)
Traceback (most recent call last):
ValueError: Out of bounds, must be between -90.0 and 90.0

>>> GeographicCoordinate(0.0, -181.0, 0.0)
Traceback (most recent call last):
ValueError: Out of bounds, must be between -180.0 and 180.0

>>> GeographicCoordinate(0.0, +181.0, 0.0)
Traceback (most recent call last):
ValueError: Out of bounds, must be between -180.0 and 180.0

>>> GeographicCoordinate(0.0, 0.0, -10995.0)
Traceback (most recent call last):
ValueError: Out of bounds, must be between -10994.0 and 8848.0

>>> GeographicCoordinate(0.0, 0.0, +8849.0)
Traceback (most recent call last):
ValueError: Out of bounds, must be between -10994.0 and 8848.0

"""

# %% SetUp

from dataclasses import dataclass

Validator: type

# English
# 1. Define class `GeographicCoordinate`
# 2. Use descriptors to check value boundaries
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `GeographicCoordinate`
# 2. Użyj deskryptory do sprawdzania wartości brzegowych
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Validator:
    pass

class Latitude(Validator):
    min = -90.0
    max = 90.0

class Longitude(Validator):
    min = -180.0
    max = 180.0

class Elevation(Validator):
    min = -10994.0
    max = 8848.0

@dataclass
class GeographicCoordinate:
    latitude: float = Latitude()
    longitude: float = Longitude()
    elevation: float = Elevation()