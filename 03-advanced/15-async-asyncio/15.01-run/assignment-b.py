"""
Name: OOP Async GatherParams
Difficulty: easy
Lines: 9
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> from inspect import iscoroutine, iscoroutinefunction
>>> import asyncio

>>> assert iscoroutinefunction(worker)
>>> assert iscoroutine(worker(None,0))

>>> assert iscoroutinefunction(main)
>>> assert iscoroutine(main())

>>> asyncio.run(main())
['a', 'b', 'c']

"""

# %% SetUp

import asyncio

from typing import Coroutine
worker: Coroutine
main: Coroutine

# English
# 1. Define:
#    - coroutine function `worker()`
#    - coroutine function `main()`
# 2. Coroutine `main()` should schedule `worker()` 3 times with parameters:
#    - First: name=a, sleep=1.0
#    - Second: name=b, sleep=0.5
#    - Third: name=c, sleep=1.5
# 3. Coroutine `main()` should return gathered results
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj:
#    - coroutine function `worker()`
#    - coroutine function `main()`
# 2. Korutyna `main()` powinna zaschedulować `worker()` 3 razy z parametrami:
#    - Pierwsze: name=a, sleep=1.0
#    - Drugie: name=b, sleep=0.5
#    - Trzecie: name=c, sleep=1.5
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
async def worker(name, sleep):
    ...

async def main():
    ...