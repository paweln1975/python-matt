"""
* Assignment: RE Syntax PositionalGroup
* Complexity: medium
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: str` with regular expression to find:
        a. year
        b. month
        c. day
    2. Use named groups (year, month, day)
    3. For simplicity, all ordinals (st, th, nd, rd) were removed
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. rok
        b. miesiąc
        c. dzień
    2. Użyj grup nazwanych (year, month, day)
    3. Dla uproszczenia, usunięto liczebniki porządkowe (st, th, nd, rd)
    4. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Authors: Wikipedia contributors
        Title: Apollo 11
        Publisher: Wikipedia
        Year: 2019
        Retrieved: 2019-12-14
        URL: https://en.wikipedia.org/wiki/Apollo_11

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> matches = re.finditer(result, DATA)

    >>> match = next(matches)
    >>> match.group('month')
    'July'
    >>> match.group('day')
    '20'
    >>> match.group('year')
    '1969'

    >>> match = next(matches)
    >>> match.group('month')
    'July'
    >>> match.group('day')
    '21'
    >>> match.group('year')
    '1969'
"""

import re

DATA = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named
Tranquility Base upon landing. Armstrong and Aldrin collected 47.5 pounds
(21.5 kg) of lunar material to bring back to Earth as pilot Michael Collins
(CMP) flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""

# Find all: year, month, day
# Use named groups (year, month, day)
# Note: For simplicity, all ordinals (st, th, nd, rd) were removed
# Example: 'July 21, 1969', 'July 21, 1969'
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result = r''

