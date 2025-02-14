"""
Name: OOP Async Concurrent
Difficulty: easy
Lines: 3
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> from inspect import iscoroutine, iscoroutinefunction
>>> import asyncio

>>> assert iscoroutinefunction(a)
>>> assert iscoroutinefunction(b)
>>> assert iscoroutinefunction(c)
>>> assert iscoroutine(a())
>>> assert iscoroutine(b())
>>> assert iscoroutine(c())

>>> async def main():
...     return await asyncio.gather(a(), b(), c())
>>>
>>> result = asyncio.run(main())
a: before
a: after
b: before
b: after
c: before
c: after

Hints:
`time.sleep()`

"""

# %% SetUp

import asyncio
import time

from typing import Coroutine
a: Coroutine
b: Coroutine
c: Coroutine

# English
# 1. Define coroutine function `a()`
#    which after running should
#       - print: 'a: before'
#       - sleep: 1.0 second
#       - print: 'a: after'
# 2. Define coroutine function `b()`
#    which after running should
#       - print: 'b: before'
#       - sleep: 0.5 second
#       - print: 'b: after'
# 3. Define coroutine function `c()`
#    which after running should
#       - print: 'c: before'
#       - sleep: 1.5 second
#       - print: 'c: after'
# 4. Use function `time.sleep()`
# 5. Do not use `await` keyword in front of `sleep`
# 6. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj coroutine function `a()`
#    która po uruchomieniu powinna
#       - wypisać: 'a: before'
#       - czekać: 1.0 sekundy
#       - wypisać: 'a: after'
# 2. Zdefiniuj coroutine function `b()`
#    która po uruchomieniu powinna
#       - wypisać: 'b: before'
#       - czekać: 0.5 sekundy
#       - wypisać: 'b: after'
# 3. Zdefiniuj coroutine function `c()`
#    która po uruchomieniu powinna
#       - wypisać: 'c: before'
#       - czekać: 1.5 sekundy
#       - wypisać: 'c: after'
# 4. Użyj funkcji `time.sleep()`
# 5. Użyj słowa kluczowego `await` przed `sleep`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
async def a():
    print('a: before')
    ...
    print('a: after')

async def b():
    print('b: before')
    ...
    print('b: after')

async def c():
    print('c: before')
    ...
    print('c: after')