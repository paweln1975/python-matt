"""
* Assignment: Datetime Timezone ZoneInfo
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    0. If you're on Windows then install module `tzdata` (`pip install tzdata`)
    1. Create `zoneinfo.ZoneInfo` object of:
        a. Cape Canaveral, FL, USA
        b. Houston, TX, USA
        c. Bajkonur Cosmodrome, Kazachstan
    2. Use `List of tz database time zones` [1]
    3. Run doctests - all must succeed

Polish:
    0. Jeżeli masz Windows to zainstaluj moduł `tzdata` (`pip install tzdata`)
    1. Stwórz obiekt `zoneinfo.ZoneInfo` z:
        a. Cape Canaveral, FL, USA
        b. Houston, TX, USA
        c. Bajkonur Cosmodrome, Kazachstan
    2. Użyj `List of tz database time zones` [1]
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

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from datetime import datetime

    >>> assert cape_canaveral is not Ellipsis, \
    'Assign value to variable `cape_canaveral` instead of Ellipsis (...)'
    >>> assert houston is not Ellipsis, \
    'Assign value to variable `houston` instead of Ellipsis (...)'
    >>> assert bajkonur is not Ellipsis, \
    'Assign value to variable `bajkonur` instead of Ellipsis (...)'

    >>> assert isinstance(cape_canaveral, ZoneInfo), \
    'Variable `cape_canaveral` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(houston, ZoneInfo), \
    'Variable `houston` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(bajkonur, ZoneInfo), \
    'Variable `bajkonur` has invalid type, must be a ZoneInfo'

    >>> def utcoffset(tz: ZoneInfo):
    ...     dt = datetime(2023, 1, 1)
    ...     return tz.utcoffset(dt).total_seconds()
    >>>
    >>> assert utcoffset(cape_canaveral) == -18000.0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(houston) == -21600.0, \
    'Invalid time zone, check IANA Time Zone Database'
    >>> assert utcoffset(bajkonur) == 21600, \
    'Invalid time zone, check IANA Time Zone Database'
"""

from zoneinfo import ZoneInfo


# Timezone in Cape Canaveral, FL, USA
# type: ZoneInfo
cape_canaveral = ...

# Timezone in Houston, TX, USA= ...
# type: ZoneInfo
houston = ...

# Timezone in Bajkonur Cosmodrome, Kazachstan
# type: ZoneInfo
bajkonur = ...

