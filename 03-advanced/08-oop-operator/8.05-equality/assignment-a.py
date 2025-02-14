"""
Name: Operator Comparison Equals
Difficulty: easy
Lines: 3
Minutes: 3

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> class Car:
...     def __init__(self, year, name):
...         self.year = year
...         self.name = name

>>> Mission(2035, 'Ares 3') == Car(2035, 'Ares 3')
False
>>> Mission(2035, 'Ares 3') == Mission(2035, 'Ares 3')
True
>>> Mission(2035, 'Ares 3') == Mission(1973, 'Apollo 18')
False
>>> Mission(2035, 'Ares 3') == Mission(2035, 'Apollo 18')
False
>>> Mission(2035, 'Ares 3') == Mission(1973, 'Ares 3')
False

"""

# %% SetUp

from typing import Callable
Mission: type
__eq__: Callable[[object, object], bool]

# English
# 1. Override operator for code to work correctly
# 2. Do not use `dataclasses`
# 3. Run doctests - all must succeed

# Polish
# 1. Nadpisz operator aby poniższy kod zadziałał poprawnie
# 2. Nie używaj `dataclasses`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name