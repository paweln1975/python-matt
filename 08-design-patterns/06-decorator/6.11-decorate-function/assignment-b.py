"""
Name: Decorator Syntax Disable
Difficulty: easy
Lines: 1
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(disable), \
'Create disable() function'

>>> assert isfunction(disable(lambda: ...)), \
'disable() should take function as an argument'

>>> @disable
... def echo(text):
...     print(text)

>>> echo('hello')
Traceback (most recent call last):
PermissionError: Function is disabled

"""

# %% SetUp

from typing import Callable
disable: Callable[[Callable], Callable]

# English
# 1. Modify decorator `disable`
# 2. Decorator raises `PermissionError` and does not execute function
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj dekorator `disable`
# 2. Dekorator podnosi `PermissionError` i nie wywołuje funkcji
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def disable(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper