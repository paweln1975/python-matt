"""
Name: Test Doctest Distance
Difficulty: easy
Lines: 21
Minutes: 13

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0

Hints:
1 km = 1000 m

"""

# %% SetUp

from typing import Callable
km_to_meters: Callable[[int|float], float]

def km_to_meters(kilometers):
    if type(kilometers) not in {int, float}:
        raise TypeError('Invalid argument type')
    if kilometers < 0:
        raise ValueError('Argument must be not negative')
    return float(kilometers * 1000)

# English
# 1. Write doctests to a functions which convert distance given in kilometers to meters
# 2. Valid arguments:
#    - `int`
#    - `float`
# 3. Invalid argumentm, raise exception `TypeError`:
#    - `str`
#    - `list[int]`
#    - `list[float]`
#    - `bool`
#    - any other type
# 4. Returned distance must be float
# 5. Returned distance cannot be negative
# 6. Run doctests - all must succeed

# Polish
# 1. Napisz doctesty do funkcji, która przeliczy dystans podany w kilometrach na metry
# 2. Poprawne argumenty:
#    - `int`
#    - `float`
# 3. Niepoprawne argumenty, podnieś wyjątek `TypeError`:
#    - `str`
#    - `list[int]`
#    - `list[float]`
#    - `bool`
#    - any other type
# 4. Zwracany dystans musi być float
# 5. Zwracany dystans nie może być ujemny
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
