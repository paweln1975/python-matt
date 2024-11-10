"""
* Assignment: Datetime Timezone ZoneInfo
* Complexity: easy
* Lines of code: 2 lines
* Time: 13 min

English:
    0. If you're on Windows then install module `tzdata` (`pip install tzdata`)
    1. Create `zoneinfo.ZoneInfo` object of:
        a. North Pole
        b. South Pole (Henryk Arctowski Polish Antarctic Station)
    2. Use:
       a. `List of tz database time zones` [1]
       b. `Time in Antarctica` [3]
    3. Run doctests - all must succeed

Polish:
    0. Jeżeli masz Windows to zainstaluj moduł `tzdata` (`pip install tzdata`)
    1. Stwórz obiekt `zoneinfo.ZoneInfo` z:
        a. North Pole
        b. South Pole (Henryk Arctowski Polish Antarctic Station)
    2. Użyj:
       a. `List of tz database time zones` [1]
       b. `Time in Antarctica` [3]
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia. List of tz database time zones.
        Retrieved: 2022-12-01
        Year: 2022
        URL: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    [2] IANA. Time Zone Database.
        Retrieved: 2022-12-01
        Year: 2022
        URL: https://data.iana.org/time-zones/releases/
    [3] Time in Antarctica.
        Retrieved: 2022-12-01
        Year: 2022
        URL: https://en.wikipedia.org/wiki/Time_in_Antarctica

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from datetime import datetime

    >>> assert north_pole is not Ellipsis, \
    'Assign value to variable `north_pole` instead of Ellipsis (...)'
    >>> assert south_pole is not Ellipsis, \
    'Assign value to variable `south_pole` instead of Ellipsis (...)'

    >>> assert isinstance(north_pole, ZoneInfo), \
    'Variable `north_pole` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(south_pole, ZoneInfo), \
    'Variable `south_pole` has invalid type, must be a ZoneInfo'

    >>> def utcoffset(tz: ZoneInfo):
    ...     dt = datetime(2023, 1, 1)
    ...     return tz.utcoffset(dt).total_seconds()
    >>>
    >>> assert utcoffset(north_pole) == 3600, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(south_pole) == 3600, \
    'Invalid time zone, check IANA Time Zone Database'
"""

from zoneinfo import ZoneInfo


# Timezone in North Pole
# type: ZoneInfo
north_pole = ...

# Timezone in South Pole
# type: ZoneInfo
south_pole = ...

