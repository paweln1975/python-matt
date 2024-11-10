"""
* Assignment: RE Syntax CharacterClass
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define `result: str` with regular expression to find:
        a. all first three lowercase letters from each word
        b. all last three lowercase letters from each word
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
        a. wszystkie pierwsze trzy małe litery z każdego słowa
        b. wszystkie ostatnie trzy małe litery z każdego słowa
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
    ['spa', 'tha', 'fir', 'lan', 'hum', 'lun', 'mod', 'pil', 'lan', 'bec',
     'fir', 'per', 'ste', 'ont', 'sur', 'hou', 'min', 'lat', 'joi', 'min',
     'lat', 'spe', 'hou', 'min', 'exp', 'sit', 'the', 'nam', 'upo', 'lan',
     'col', 'pou', 'lun', 'mat', 'bri', 'bac', 'pil', 'fle', 'lun', 'orb',
     'wer', 'sur', 'hou', 'min', 'bef', 'lif', 'rej']

    >>> result = re.findall(result_b, DATA)
    >>> pprint(result, compact=True, width=72)
    ['llo', 'can', 'ght', 'hat', 'rst', 'ded', 'ans', 'oon', 'der', 'eil',
     'ong', 'nar', 'ule', 'lot', 'uzz', 'rin', 'ded', 'llo', 'nar', 'ule',
     'gle', 'uly', 'ong', 'ame', 'rst', 'son', 'tep', 'nto', 'oon', 'ace',
     'urs', 'tes', 'ter', 'uly', 'rin', 'ned', 'tes', 'ter', 'hey', 'ent',
     'urs', 'tes', 'ing', 'ite', 'hey', 'med', 'ity', 'ase', 'pon', 'ing',
     'ong', 'rin', 'ted', 'nds', 'nar', 'ial', 'ing', 'ack', 'rth', 'lot',
     'ael', 'ins', 'lew', 'and', 'ule', 'bia', 'nar', 'bit', 'ere', 'oon',
     'ace', 'urs', 'tes', 'ore', 'ing', 'oin', 'bia']
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

# Find all first three lowercase letters from each word
# Example: 'spa', 'tha', 'fir', 'lan', 'hum', 'lun', ...
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_a = r''

# Find all last three lowercase letters from each word
# Example: 'llo', 'can', 'ght', 'hat', 'rst', 'ded', ...
# Note: define only regex pattern (str), not re.findall(...)
# type: str
result_b = r''

