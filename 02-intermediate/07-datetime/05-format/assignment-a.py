"""
* Assignment: Datetime Format ISO-8601
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: str` with `DATA` in ISO-8601 format
    2. Do not use `datetime.isoformat()` method
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z `DATA` w formacie ISO-8601
    2. Nie używaj metody `datetime.isoformat()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, must be a str'

    >>> result
    '1969-07-21 02:56:15'
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)

# DATA in ISO-8601 format: '1969-07-21 02:56:15'
# type: str
result = ...

