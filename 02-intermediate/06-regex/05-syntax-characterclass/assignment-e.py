"""
* Assignment: RE Syntax CharacterClass
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. all two-letter conjunctives (two-letter words)
        b. all two-letter pairs embedded in the words
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. wszystkie dwu literowe spójniki (dwu-literowe słowa)
        b. wszystkie dwu literowe pary wbudowane w słowach
    2. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * Use `r-string`

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

    >>> result = re.findall(result_a, DATA)
    >>> pprint(result, compact=True, width=72)
    ['on', 'on', 'at', 'to', 'on', 'at', 'kg', 'of', 'to', 'to', 'as', 'in',
     'on', 'to']

    >>> result = re.findall(result_b, DATA)
    >>> pprint(result, compact=True, width=72)
    ['po', 'll', 'me', 'ri', 'ca', 'pa', 'ce', 'fl', 'ig', 'ha', 'ir', 'an',
     'de', 'um', 'an', 'oo', 'om', 'ma', 'nd', 'ei', 'rm', 'st', 'ro', 'un',
     'od', 'ul', 'il', 'uz', 'ld', 'ri', 'an', 'de', 'po', 'll', 'un', 'od',
     'ul', 'ag', 'ul', 'rm', 'st', 'ro', 'ec', 'am', 'ir', 'er', 'so', 'te',
     'nt', 'oo', 'ur', 'fa', 'ou', 'in', 'ut', 'at', 'ul', 'ld', 'ri', 'oi',
     'ne', 'in', 'ut', 'at', 'he', 'pe', 'ou', 'in', 'ut', 'xp', 'lo', 'ri',
     'it', 'he', 'am', 'ra', 'nq', 'ui', 'li', 'as', 'po', 'an', 'di', 'rm',
     'st', 'ro', 'ld', 'ri', 'ol', 'le', 'ct', 'ou', 'nd', 'un', 'at', 'er',
     'ia', 'ri', 'ac', 'ar', 'il', 'ic', 'ha', 'ol', 'li', 'le', 'om', 'ma',
     'od', 'ul', 'ol', 'um', 'bi', 'un', 'rb', 'er', 'oo', 'ur', 'fa', 'ou',
     'in', 'ut', 'ef', 'or', 'if', 'ti', 'ej', 'oi', 'ol', 'um', 'bi']
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

# Find all two-letter conjunctives in text (standalone two-letter words)
# Example: 'on', 'on', 'at', 'to', ...
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_a = r''

# Find all two-letter pairs embedded in the words
# Example: 'po', 'll', 'me', 'ri', 'ca', 'pa', 'ce', ...
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_b = r''

