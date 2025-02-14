"""
Name: Decorator Method Alive
Difficulty: easy
Lines: 4
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

>>> assert isfunction(if_alive), \
'Create if_alive() function'

>>> assert isfunction(if_alive(lambda: ...)), \
'if_alive() should take method as an argument'

>>> class Hero:
...    def __init__(self, name):
...        self.name = name
...        self.current_health = 100
...
...    @if_alive
...    def make_damage(self):
...        return 10

>>> hero = Hero('Mark Watney')
>>> hero.make_damage()
10
>>> hero.current_health = -10
>>> hero.make_damage()
Traceback (most recent call last):
RuntimeError: Hero is dead and cannot make damage

"""

# %% SetUp

from typing import Callable
if_alive: Callable[[Callable], Callable]

# English
# 1. Create `if_alive` method decorator
# 2. Decorator will allow running `make_damage` method
#    only if `current_health` is greater than 0
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz dekorator metody `if_alive`
# 2. Dekorator pozwoli na wykonanie metody `make_damage`,
#    tylko gdy `current_health` jest większe niż 0
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def if_alive(method):
    def wrapper(hero, *args, **kwargs):
        return method(hero, *args, **kwargs)
    return wrapper