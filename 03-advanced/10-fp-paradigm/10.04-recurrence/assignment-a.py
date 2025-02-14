"""
Name: Functional Recurrence Fibonacci
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> fib(1)
1
>>> fib(2)
2
>>> fib(5)
8
>>> fib(9)
55
>>> fib(10)
89
>>> [fib(x) for x in range(10)]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

"""

# %% SetUp

from typing import Callable
fib: Callable[[int], int]

# English
# 1. Fibonacci series is created by adding two previous numbers, i.e.:
#    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 2. Define function `fib(n)` using recursion to generate
#    items of the Fibonacci series
# 3. For `n` less or equal to 1, return 1
# 4. Else return sum `fib(n-1)` and `fib(n-2)`
# 5. Run doctests - all must succeed

# Polish
# 1. Ciąg Fibonacciego powstaje przez dodawanie dwóch poprzednich liczb, np:
#    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 2. Zdefiniuj funkcję `fib(n)` używającą rekurencji do generowania
#    wyrazów ciągu Fibonacciego
# 3. Dla `n` mniejszej lub równej 1, zwróć 1
# 4. W przeciwnym wypadku zwróć sumę `fib(n-1)` i `fib(n-2)`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def fib():
    ...