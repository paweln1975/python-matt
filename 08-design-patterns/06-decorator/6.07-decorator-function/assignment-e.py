"""
Name: Decorator Function Numeric
Difficulty: easy
Lines: 4
Minutes: 5

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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(numeric), \
'Create numeric() function'

>>> assert isfunction(numeric(lambda: ...)), \
'numeric() should take function as an argument'

>>> @numeric
... def add(a, b):
...     return a + b

>>> add(1, 1)
2
>>> add(1.5, 2.5)
4.0
>>> add(-1, 1.5)
0.5

>>> add('one', 1)
Traceback (most recent call last):
TypeError: Argument "a" must be int or float
>>> add(1, 'two')
Traceback (most recent call last):
TypeError: Argument "b" must be int or float

>>> add(True, 0)
Traceback (most recent call last):
TypeError: Argument "a" must be int or float
>>> add(0, True)
Traceback (most recent call last):
TypeError: Argument "b" must be int or float

"""

# %% SetUp

from typing import Callable
numeric: Callable[[Callable], Callable]

# English
# 1. Modify decorator `numeric`
# 2. Decorator must check arguments `a` and `b` types
# 3. If type `a` or `b` are not `int` or `float`
#    raise exception `TypeError`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj dekorator `numeric`
# 2. Dekorator ma sprawdzać typy argumentów `a` oraz `b`
# 3. Jeżeli typ `a` lub `b` nie jest `int` lub `float`
#    to podnieś wyjątek `TypeError`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def numeric(func):
    def wrapper(a, b):
        return func(a, b)
    return wrapper