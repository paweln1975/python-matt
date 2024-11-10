"""
* Assignment: Datetime Format US
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: str` with `DATA` in long US format
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z `DATA` w długim formacie amerykańskim
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> content = Path(__file__).read_text()

    >>> assert '%'+'-H' not in content, \
    '%H is used for 24-hour clock, use %I instead'
    >>> assert '%'+'_H' not in content, \
    '%H is used for 24-hour clock, use %I instead'
    >>> assert '%'+'#H' not in content, \
    '%H is used for 24-hour clock, use %I instead'
    >>> assert '%'+'I' in content, \
    'Use %I for 12-hour clock'
    >>> assert '%'+'p' in content, \
    'Use %p for AM/PM'

    >>> result
    'July 21, 1969 02:56:15 AM'
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)

# DATA in long US format: 'July 21, 1969 02:56:15 AM'
# type: str
result = ...

