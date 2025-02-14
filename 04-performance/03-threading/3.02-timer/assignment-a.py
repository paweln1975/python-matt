"""
Name: Concurrency Threading Timer
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> def check(result):
...     assert result == [1, 2, 3], f'Result is {result}'

>>> Timer(INTERVAL, ping).start()
>>> Timer(INTERVAL*MAX+1, check, [result]).start()

"""

# %% SetUp

from threading import Timer

from typing import Callable
ping: Callable[[int], None]

INTERVAL = 0.1
MAX = 3
result = []

# English
# 1. Define function `ping()`, with optional parameter
#    `n: int`, which defaults to 1
# 2. Function `ping()` should append value of `n` to `result`
# 3. Function should be called every `INTERVAL`
# 4. Function should be called maximum `MAX` times
# 5. Use `Timer` from `threading` module
# 6. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj funkcję `ping(n: int)` z opcjonalnym parametrem
#    `n: int`, który domyślnie jest 1
# 2. Funkcja `ping()` powinna dopisywać wartość `n` do `result`
# 3. Funkcja powinna być wywoływana co `INTERVAL`
# 4. Funkcja powinna być wywołana maksymalnie `MAX` razy
# 5. Użyj `Timer` z modułu `threading`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
