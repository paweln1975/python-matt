"""
* Assignment: Pickle Load ListObjects
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: list[User]` with data from `FILE`
    2. Use `pickle` module
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[User]` z danymi z `FILE`
    2. Użyj modułu `pickle`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> result
    ('Mark', 'Watney', 1)

    >>> remove(FILE)
"""

import pickle

FILE = r'_temporary.pkl'

with open(FILE, mode='wb') as file:
    file.write(
        b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c'
        b'\x04Mark\x94\x8c\x06Watney\x94K\x01\x87\x94.'
    )


