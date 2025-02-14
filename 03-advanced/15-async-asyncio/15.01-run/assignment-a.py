"""
Name: OOP Async GatherMany
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
Terminal: `python -m doctest -v assignment-a.py`

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

>>> assert iscoroutinefunction(main)
>>> assert iscoroutine(main())

>>> asyncio.run(main())
a: before
b: before
c: before
b: after
a: after
c: after
['a', 'b', 'c']

"""

# %% SetUp

import asyncio

from typing import Coroutine
main: Coroutine

async def a():
    print('a: before')
    await asyncio.sleep(1.0)
    print('a: after')
    return 'a'

async def b():
    print('b: before')
    await asyncio.sleep(0.5)
    print('b: after')
    return 'b'

async def c():
    print('c: before')
    await asyncio.sleep(1.5)
    print('c: after')
    return 'c'

# English
# 1. Define:
#    - coroutine function `main()`
# 2. After running coroutine should:
#    - execute coroutines a(), b() and c()
#    - gather their returned values
#    - return results
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj:
#    - coroutine function `main()`
# 2. Po uruchomieniu coroutine powinna:
#    - wykonać korutyny a(), b() i c()
#    - zebrać ich zwracane wartości
#    - zwrócić wyniki
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def main():
    ...