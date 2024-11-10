"""
* Assignment: Datetime Format LeadingZero
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: str` with `DATA` in short US format
    2. Make sure, that month, day and hour are without leading zero
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z `DATA` w krótkim formacie amerykańskim
    2. Upewnij się, że miesiąc, dzień i godzina jest bez wiodącego zera
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use `%-I` on *nix systems (macOS, BSD, Linux)
    * Use `%#I` on Windows

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
    >>> assert '%'+'-I' in content or '%'+'_I' in content, \
    'Use %I for 12-hour clock'
    >>> assert '%'+'p' in content, \
    'Use %p for AM/PM'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, must be a str'

    >>> result
    '7/21/69 2:56 AM'
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)

# DATA in short US format: '7/21/69 2:56 AM'
# type: str
result = ...

