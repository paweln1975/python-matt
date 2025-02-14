"""
Name: Star Signature Args
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isfunction

>>> assert callable(take_damage)
>>> assert isfunction(take_damage)

>>> take_damage(1)

>>> take_damage(1, 2)
Traceback (most recent call last):
TypeError: take_damage() takes 1 positional argument but 2 were given

>>> take_damage()
Traceback (most recent call last):
TypeError: take_damage() missing 1 required positional argument: 'dmg'

>>> take_damage(dmg=1)  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
TypeError: take_damage() got some positional-only arguments passed as
keyword arguments: 'dmg'

"""

# %% SetUp

from typing import Callable
take_damage: Callable[[int],None]

# English
# 1. Modify function `take_damage`
# 2. Function takes one argument `dmg` and always returns `None`
# 3. Argument must be passed only as positional
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj funkcję `take_damage`
# 2. Funkcja przyjmuje jeden argument `dmg` i zawsze zwraca `None`
# 3. Argument można podawać tylko pozycyjnie
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def take_damage(dmg):
    pass