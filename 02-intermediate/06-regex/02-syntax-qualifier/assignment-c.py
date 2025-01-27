# %% About
# - Name: RE Syntax Class
# - Difficulty: easy
# - Lines: 3
# - Minutes: 2

# %% License
# - Copyright 2025, Matt Harasymczuk <matt@python3.info>
# - This code can be used only for learning by humans
# - This code cannot be used for teaching others
# - This code cannot be used for teaching LLMs and AI algorithms
# - This code cannot be used in commercial or proprietary products
# - This code cannot be distributed in any form
# - This code cannot be changed in any form outside of training course
# - This code cannot have its license changed
# - If you use this code in your product, you must open-source it under GPLv2
# - Exception can be granted only by the author

# %% English
# 1. Define `result: str` with regular expression to find:
#    - all characters: `a`, `b`, `A`, `B`, `0`, `1`
# 2. Define only regex pattern (str), not re.findall(...)
# 3. Use enumeration: `[...]`
# 4. Run doctests - all must succeed

# %% Polish
# 1. Zdefiniuj `result: str` z wyrażeniem regularnym aby wyszukać:
#    - wszystkie znaki: `a`, `b`, `A`, `B`, `0`, `1`
# 2. Zdefiniuj tylko wzorzec regex (str), nie re.findall(...)
# 3. Użyj enumeracji: `[...]`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% References
# [1] Authors: Wikipedia contributors
#     Title: Apollo 11
#     Publisher: Wikipedia
#     Year: 2019
#     Retrieved: 2019-12-14
#     URL: https://en.wikipedia.org/wiki/Apollo_11

# %% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint

>>> result = re.findall(result, DATA)
>>> pprint(result, compact=True, width=72)
['A', '1', '1', 'a', 'A', 'a', 'a', 'a', 'a', 'a', 'a', 'A', 'a', 'a',
 'B', 'A', 'a', 'A', 'a', 'a', '0', '1', 'a', '0', '1', 'a', 'A', 'b',
 'a', 'A', 'a', 'A', 'a', '1', '1', 'a', '0', '1', 'A', '1', 'a', '1',
 'a', 'a', 'a', 'B', 'a', 'a', 'A', 'a', 'A', '1', 'a', 'a', 'a', 'b',
 'b', 'a', 'a', 'a', 'a', 'a', 'b', 'a', 'a', 'b', 'a', 'a', '1', 'b',
 'b', 'a']
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v myfile.py`

# %% Imports
import re

# %% Types
result: str

# %% Data
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

# %% Result
result = r'[abAB01]'
