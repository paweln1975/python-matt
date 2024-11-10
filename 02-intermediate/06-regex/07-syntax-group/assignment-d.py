"""
* Assignment: RE Syntax Group
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Find all duration values
    2. SKIP durations without hours (only with minutes)
    3. Use:
       a. `result_a`: using positional group
       b. `result_b`: using named group
    4. Run doctests - all must succeed

Polish:
    1. Znajdź wszystkie okresy czasowe
    2. POMIŃ okresy bez godzin (tylko z minutami)
    3. Define:
        a. `result_a`: używając grupy pozycyjnej
        b. `result_b`: używając grupy nazwanej
    3. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> result_a = re.findall(result_a, DATA)
    >>> pprint(result_a, compact=True, width=20)
    [('6', '39'),
     ('2', '31'),
     ('21', '36')]

    >>> result_b = re.finditer(result_b, DATA)
    >>> result_b = [x.groupdict() for x in result_b]
    >>> pprint(result_b, compact=True, width=50)
    [{'hours': '6', 'minutes': '39'},
     {'hours': '2', 'minutes': '31'},
     {'hours': '21', 'minutes': '36'}]

"""

import re

DATA = """Apollo 11 was the American spaceflight that first landed
humans on the Moon. Commander (CDR) Neil Armstrong and lunar module
pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on
July 20th, 1969 at 20:17 UTC, and Armstrong became the first person
to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later,
on July 21st, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later.
They spent 2 hours 31 minutes exploring the site they had named
Tranquility Base upon landing. Armstrong and Aldrin collected 47.5 pounds
(21.5 kg) of lunar material to bring back to Earth as pilot Michael Collins
(CMP) flew the Command Module (CM) Columbia in lunar orbit, and were on the
Moon's surface for 21 hours 36 minutes before lifting off to rejoin
Columbia."""

# Find all duration values, use positional groups
# SKIP durations without hours (only with minutes)
# Example: [('6', '39'), ('2', '31'), ('21', '36')]
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_a = r''

# Find all duration values, use named groups
# SKIP durations without hours (only with minutes)
# Example: [{'hours': '6', 'minutes': '39'}, {'hours': '2', 'minutes': '31'}]
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_b = r''

