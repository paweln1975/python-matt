"""
Name: Decorator Functools Args
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(mydecorator), \
'Create mydecorator() function'

>>> assert isfunction(mydecorator(True)), \
'mydecorator() should take one positional argument'

>>> assert isfunction(mydecorator(happy=True)), \
'mydecorator() should take one keyword argument'

>>> assert isfunction(mydecorator(happy=True)(lambda: ...)), \
'The result of mydecorator() should take function as an argument'

>>> @mydecorator(happy=False)
... def hello():
...     '''Hello Docstring'''
>>> hello.__name__
'hello'
>>> hello.__doc__
'Hello Docstring'

"""

# %% SetUp

from functools import wraps

from typing import Callable
mydecorator: Callable[[bool], Callable]

# English
# 1. Use `functools.wraps` in correct place
# 2. Run doctests - all must succeed

# Polish
# 1. Użyj `functools.wraps` w odpowiednim miejscu
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def mydecorator(happy=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator