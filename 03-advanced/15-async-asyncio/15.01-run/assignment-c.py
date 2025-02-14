"""
Name: OOP Async Fetch
Difficulty: easy
Lines: 7
Minutes: 8

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

>>> assert iscoroutinefunction(fetch)
>>> assert iscoroutine(fetch(''))

>>> assert iscoroutinefunction(check)
>>> assert iscoroutine(check(''))

>>> assert iscoroutinefunction(main)
>>> assert iscoroutine(main())

>>> asyncio.run(main())  # doctest: +NORMALIZE_WHITESPACE
[{'url': 'https://python3.info', 'license': True},
 {'url': 'https://python3.info/index.html', 'license': True},
 {'url': 'https://python3.info/about.html', 'license': False},
 {'url': 'https://python3.info/LICENSE.html', 'license': True}]

"""

# %% SetUp

import asyncio
from httpx import AsyncClient

from typing import Coroutine
check: Coroutine
main: Coroutine

DATA = [
    'https://python3.info',
    'https://python3.info/index.html',
    'https://python3.info/about.html',
    'https://python3.info/LICENSE.html',
]

async def fetch(url):
    return await AsyncClient().get(url)

# English
# 1. Define:
#    - coroutine function `check()`
#    - coroutine function `main()`
# 2. Coroutine `check()` should use coroutine `fetch()` to download html
# 3. Coroutine `check()` should check if string 'Matt Harasymczuk' is in html
# 4. Coroutine `main()` should schedule `check()` for each URL in DATA
# 5. Coroutine `main()` should return gathered results as list[dict], for example:
#    [{'url': 'https://python3.info', 'license': True},
#     {'url': 'https://python3.info/index.html', 'license': True},
#     {'url': 'https://python3.info/about.html', 'license': False},
#     {'url': 'https://python3.info/LICENSE.html', 'license': True}]
# 6. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj:
#    - coroutine function `check()`
#    - coroutine function `main()`
# 2. Korutyna `check` powinna użyć korutyny `fetch()` aby ściągnąć html
# 3. Korutyna `check()` powinna sprawdzać czy string 'Matt Harasymczuk' jest w htmlu
# 4. Korutyna `main()` powinna zaschedulować `check()` dla każdego URL w DATA
# 5. Korutyna `main()` powinna zwrócić zebrane wyniki jako list[dict], na przykład:
#    [{'url': 'https://python3.info', 'license': True},
#     {'url': 'https://python3.info/index.html', 'license': True},
#     {'url': 'https://python3.info/about.html', 'license': False},
#     {'url': 'https://python3.info/LICENSE.html', 'license': True}]
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
async def check(url):
    ...

async def main():
    ...