"""
Name: OOP MethodClassmethod FromTimestamp
Difficulty: easy
Lines: 4
Minutes: 3

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
Terminal: `python -m doctest -v assignment-g.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Timezone)
>>> assert isclass(CET)
>>> assert isclass(CEST)

>>> cet = CET.from_timestamp(1234567890)
>>> assert type(cet.tzname) is str
>>> assert type(cet.dt) is datetime
>>> assert cet.tzname == 'Central European Time'
>>> assert cet.dt == datetime(2009, 2, 13, 23, 31, 30, tzinfo=timezone.utc)

>>> cest = CEST.from_timestamp(1234567890)
>>> assert type(cest.tzname) is str
>>> assert type(cest.dt) is datetime
>>> assert cest.tzname == 'Central European Summer Time'
>>> assert cest.dt == datetime(2009, 2, 13, 23, 31, 30, tzinfo=timezone.utc)

Hints:
`datetime.fromtimestamp(tz=timezone.utc)`

"""

# %% SetUp

from datetime import datetime, timezone

from typing import Callable
from zoneinfo import ZoneInfo

Timezone: type
from_timestamp: Callable[[type, int], object]

# English
# 1. Modify class `Timezone`
# 2. Define method `from_timestamp()`:
#    - parameter `timestamp: int`, example: 1234567890
#    - returns instance of a class on which was called
# 3. Use `tz=timezone.utc` as a parameter to `datetime.fromtimestamp()`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Timezone`
# 2. Zdefiniuj classmethod `from_timestamp()`:
#    - parametr `timestamp: int`, przykład: 1234567890
#    - zwraca instancję klasy na której została wykonana
# 3. Użyj `tz=timezone.utc` jako parametr do `datetime.fromtimestamp()`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Timezone:
    tzname: str
    dt: datetime

    def __init__(self, dt):
        self.dt = dt

    @classmethod
    def from_timestamp(cls, timestamp: int):
        return cls(datetime.fromtimestamp(timestamp, timezone.utc))


class CET(Timezone):
    tzname = 'Central European Time'

class CEST(Timezone):
    tzname = 'Central European Summer Time'