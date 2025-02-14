"""
Name: Decorator Function Memoization
Difficulty: easy
Lines: 3
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from timeit import timeit
>>> from inspect import isfunction
>>> import logging
>>> sys.setrecursionlimit(5000)

>>> assert type(_cache) is dict, \
'Cache storage should be a dict'

>>> assert len(_cache) == 0, \
'Cache storage should be empty'

>>> assert isfunction(cache), \
'Create cache() function'

>>> assert isfunction(cache(lambda: ...)), \
'cache() should take function as an argument'

>>> @cache
... def fn1(n):
...     if n == 0:
...         return 1
...     else:
...         return n * fn1(n - 1)

>>> def fn2(n):
...     if n == 0:
...         return 1
...     else:
...         return n * fn2(n - 1)

>>> def run():
...     cached = timeit(
...         stmt='fn1(500); fn1(400); fn1(450); fn1(350)',
...         globals=globals(),
...         number=1000)
...     uncached = timeit(
...         stmt='fn2(500); fn2(400); fn2(450); fn2(350)',
...         globals=globals(),
...         number=1000)
...     ratio = uncached / cached
...     logging.warning(f'Uncached: {uncached:.4f} seconds')
...     logging.warning(f'Cached:   {cached:.4f} seconds')
...     logging.warning(f'Faster:   {ratio:.1f} times')
>>>
>>> _ = run()

"""

# %% SetUp

from typing import Callable
cache: Callable[[Callable], Callable]

_cache = {}

# English
# 1. Create decorator `@cache`
# 2. Decorator must check before running function, if for given argument
#    the computation was already done:
#    - if yes, return from `_cache`
#    - if not, calculate new result, update cache and return value
# 3. Check doctest output to see how much faster is cached version
# 4. Run doctests - all must succeed (beside three prints)

# Polish
# 1. Stwórz dekorator `@cache`
# 2. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego
#    argumentu wynik został już wcześniej obliczony:
#    - jeżeli tak, zwróć dane z `_cache`
#    - jeżeli nie, oblicz, zaktualizuj `_cache` i zwróć wartość
# 3. Sprawdź output doctestów, aby zobaczyć jak szybka jest wersja z cache
# 4. Uruchom doctesty - wszystkie muszą się powieść (poza trzema printami)

# %% Result
def cache(func):
    def wrapper(n):
        return func(n)
    return wrapper