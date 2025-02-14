"""
Name: Star Signature Kwargs
Difficulty: easy
Lines: 1
Minutes: 2

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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isfunction

>>> assert callable(set_position)
>>> assert isfunction(set_position)

>>> set_position(x=1, y=2)

>>> set_position()  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
TypeError: set_position() missing 2 required keyword-only arguments: 'x' and 'y'

>>> set_position(1)
Traceback (most recent call last):
TypeError: set_position() takes 0 positional arguments but 1 was given

>>> set_position(1, 2)
Traceback (most recent call last):
TypeError: set_position() takes 0 positional arguments but 2 were given

>>> set_position(1, y=1)  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
TypeError: set_position() takes 0 positional arguments but 1 positional
argument (and 1 keyword-only argument) were given

>>> set_position(x=1, 2)
Traceback (most recent call last):
SyntaxError: positional argument follows keyword argument

"""

# %% SetUp

from typing import Callable
set_position: Callable[[int,int],None]

# English
# 1. Create function `set_position`
# 2. Function takes two arguments `x`, `y` and always returns `None`
# 3. Arguments must be passed only as keywords
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz funkcję `set_position`
# 2. Funkcja przyjmuje dwa argumenty `x`, `y` i zawsze zwraca `None`
# 3. Argumenty można podawać tylko nazwanie (keyword)
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def set_position(x, y):
    pass