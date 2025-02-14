"""
Name: Decorator Functools Cls
Difficulty: easy
Lines: 2
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction, isclass

>>> assert isfunction(mydecorator), \
'Create mydecorator() function'

>>> assert mydecorator(object), \
'mydecorator() should take class as an argument'

>>> assert isclass(mydecorator(object)), \
'The result of mydecorator() should be a class'

>>> @mydecorator
... class Hello:
...     '''Hello Docstring'''
>>> hello = Hello()
>>> hello.__name__
'Hello'
>>> hello.__doc__
'Hello Docstring'

"""

# %% SetUp

from typing import Callable
mydecorator: Callable[[type], type]

# English
# 1. Modify code to restore docstring and name from decorated class
# 2. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj kod aby przywrócić docstring oraz nazwę z dekorowanej klasy
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def mydecorator(cls):
    class Wrapper(cls):
        pass
    return Wrapper