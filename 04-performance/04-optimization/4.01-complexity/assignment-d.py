"""
Name: Unpack Parameters Define
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> mean(1)
1.0
>>> mean(1, 2)
1.5
>>> mean(1, 2, 3)
2.0
>>> mean(1, 2, 3, 4)
2.5
>>> mean()
Traceback (most recent call last):
ValueError: At least one argument is required

Hints:
`raise ValueError('error message')`
`sum(...) / len(...)`

"""

# %% SetUp

from typing import Callable
mean: Callable[[tuple[int|float]], float]

# English
# 1. Create function `mean()`, which calculates arithmetic mean
# 2. Function can have arbitrary number of positional arguments
# 3. Non-functional requirements:
#    - Do not import any libraries and modules
#    - Use builtin functions `sum()` and `len()`
# 4. Run doctests - all must succeed

# Polish
# 1. Napisz funkcję `mean()`, wyliczającą średnią arytmetyczną
# 2. Funkcja przyjmuje dowolną ilość pozycyjnych argumentów
# 3. Wymagania niefunkcjonalne:
#    - Nie importuj żadnych bibliotek i modułów
#    - Użyj wbudowanych funckji `sum()` i `len()`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
