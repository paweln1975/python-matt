"""
Name: OOP MethodClassmethod FromDatetime
Difficulty: easy
Lines: 10
Minutes: 5

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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(DateTime)
>>> assert isclass(UTC)
>>> assert isclass(CET)
>>> assert isclass(CEST)

>>> data = datetime(1969, 7, 21, 2, 56, 15)
>>> utc = UTC.from_datetime(data)
>>> assert type(utc.year) is int
>>> assert type(utc.month) is int
>>> assert type(utc.day) is int
>>> assert type(utc.hour) is int
>>> assert type(utc.minute) is int
>>> assert type(utc.second) is int
>>> assert type(utc.tzinfo) is ZoneInfo
>>> assert utc.year == 1969
>>> assert utc.month == 7
>>> assert utc.day == 21
>>> assert utc.hour == 2
>>> assert utc.minute == 56
>>> assert utc.second == 15
>>> assert utc.tzinfo == ZoneInfo('Etc/UTC')

>>> data = datetime(1969, 7, 21, 2, 56, 15)
>>> cet = CET.from_datetime(data)
>>> assert type(cet.year) is int
>>> assert type(cet.month) is int
>>> assert type(cet.day) is int
>>> assert type(cet.hour) is int
>>> assert type(cet.minute) is int
>>> assert type(cet.second) is int
>>> assert type(cet.tzinfo) is ZoneInfo
>>> assert cet.year == 1969
>>> assert cet.month == 7
>>> assert cet.day == 21
>>> assert cet.hour == 2
>>> assert cet.minute == 56
>>> assert cet.second == 15
>>> assert cet.tzinfo == ZoneInfo('Etc/GMT-1')

>>> data = datetime(1969, 7, 21, 2, 56, 15)
>>> cest = CEST.from_datetime(data)
>>> assert type(cest.year) is int
>>> assert type(cest.month) is int
>>> assert type(cest.day) is int
>>> assert type(cest.hour) is int
>>> assert type(cest.minute) is int
>>> assert type(cest.second) is int
>>> assert type(cest.tzinfo) is ZoneInfo
>>> assert cest.year == 1969
>>> assert cest.month == 7
>>> assert cest.day == 21
>>> assert cest.hour == 2
>>> assert cest.minute == 56
>>> assert cest.second == 15
>>> assert cest.tzinfo == ZoneInfo('Etc/GMT-2')

Hints:
`zoneinfo.ZoneInfo()`
`datetime.datetime()`

"""

# %% SetUp

from datetime import datetime
from zoneinfo import ZoneInfo

from typing import Callable
DateTime: type
from_datetime: Callable[[type, datetime], object]

# English
# 1. Modify class `DateTime`
# 2. Define classmethod `from_datetime()`:
#    - parameter `dt: datetime`, example: datetime(1969, 7, 21, 2, 56, 15)
#    - returns instance of a class on which was called
# 3. Use `tzinfo = ZoneInfo(cls.tzname)`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `DateTime`
# 2. Zdefiniuj classmethod `from_datetime()`:
#    - parametr `dt: datetime`, przykład: datetime(1969, 7, 21, 2, 56, 15)
#    - zwraca instancję klasy na której została wykonana
# 3. Użyj `tzinfo = ZoneInfo(cls.tzname)`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class DateTime:
    tzname: str

    def __init__(self, year, month, day, hour, minute, second, tzinfo):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.tzinfo = tzinfo

    @classmethod
    def from_datetime(cls, dt: datetime):
        ...

class UTC(DateTime):
    tzname = 'Etc/UTC'

class CET(DateTime):
    tzname = 'Etc/GMT-1'

class CEST(DateTime):
    tzname = 'Etc/GMT-2'