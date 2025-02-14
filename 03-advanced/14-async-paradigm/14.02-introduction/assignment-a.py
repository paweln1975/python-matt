"""
Name: OOP Async Coroutine
Difficulty: easy
Lines: 2
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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> import sys; sys.tracebacklimit = 0
>>> from inspect import iscoroutine, iscoroutinefunction
>>> import asyncio

>>> assert iscoroutinefunction(a)
>>> assert iscoroutine(a())

>>> asyncio.run(a())
'a'

"""

# %% SetUp

import asyncio

from typing import Coroutine
a: Coroutine

# English
# 1. Define coroutine function `a()`
# 2. After running coroutine should return 'a'
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj coroutine function `a()`
# 2. Po uruchomieniu coroutine powinna zwracać 'a'
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def a():
    ...