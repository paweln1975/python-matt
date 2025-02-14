"""
Name: Test Doctest Temperature
Difficulty: easy
Lines: 5
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isfunction

"""

# %% SetUp

from typing import Callable
type T = tuple[int|float,...] | list[int|float] | set[int|float]
celsius_to_kelvin: Callable[[T], T]

def celsius_to_kelvin(degrees):
    if type(degrees) in (int, float):
        if degrees < -273.15:
            raise ValueError('Argument must be not less than -273.15')
        return 273.15 + degrees
    if type(degrees) in (list, tuple, set):
        if any(degree < -273.15 for degree in degrees):
            raise ValueError('Argument must be not less than -273.15')
        cls = type(degrees)
        return cls(x+273.15 for x in degrees)
    raise TypeError('Invalid argument type')

# English
# 1. Write doctests to `celsius_to_kelvin` function
# 2. Parameter `degrees` can be:
#    - int
#    - float
#    - list[int|float]
#    - tuple[int|float,...]
#    - set[int|float]
#    - In other case raise an exception: TypeError
#            with message: "Invalid argument type"
# 3. Run doctests - all must succeed

# Polish
# 1. Napisz doctesty do funkcji `celsius_to_kelvin`
# 2. Parametr `degrees` może być:
#    - int
#    - float
#    - list[int|float]
#    - tuple[int|float,...]
#    - set[int|float]
#    - W przeciwnym wypadku podnieś wyjątek: TypeError
#            z komunikatem: "Invalid argument type"
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
