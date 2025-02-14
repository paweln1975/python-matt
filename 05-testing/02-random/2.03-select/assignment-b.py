"""
Name: Random Select Inner
Difficulty: medium
Lines: 1
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result
62

Hints:
`random.randint()`
`randint(a,b)` includes both end points a and b

"""

# %% SetUp

result: int

DATA = [[6, 6, 0, 4, 8, 7, 6, 4, 7, 5, 9, 3, 8, 2, 4, 2],
        [1, 9, 4, 8, 9, 2, 4, 1, 1, 5, 7, 8, 1, 5, 6, 5],
        [9, 3, 8, 7, 7, 8, 4, 0, 8, 0, 1, 6, 0, 9, 7, 5],
        [3, 5, 1, 3, 9, 3, 3, 2, 8, 7, 1, 1, 5, 8, 7, 1],
        [4, 8, 4, 1, 8, 5, 8, 3, 9, 8, 9, 4, 7, 1, 9, 6],
        [5, 9, 3, 4, 2, 3, 2, 0, 9, 4, 7, 1, 1, 2, 2, 0],
        [1, 8, 6, 8, 4, 8, 3, 3, 9, 6, 9, 4, 7, 7, 5, 1],
        [5, 9, 1, 7, 9, 5, 3, 3, 0, 4, 1, 3, 5, 2, 5, 6],
        [0, 1, 2, 3, 0, 9, 8, 9, 1, 0, 1, 3, 9, 9, 1, 6],
        [1, 5, 1, 0, 9, 0, 3, 2, 1, 7, 3, 0, 0, 8, 6, 9],
        [1, 4, 1, 3, 1, 4, 5, 6, 2, 0, 8, 7, 0, 9, 1, 6],
        [3, 4, 5, 7, 9, 2, 3, 0, 2, 2, 5, 8, 4, 1, 9, 7],
        [2, 0, 7, 6, 9, 8, 4, 5, 6, 4, 2, 8, 0, 7, 1, 5],
        [0, 8, 4, 2, 3, 7, 5, 9, 4, 5, 9, 9, 2, 4, 6, 6],
        [1, 0, 9, 3, 5, 2, 3, 3, 7, 6, 9, 6, 0, 6, 9, 6],
        [0, 2, 7, 1, 4, 2, 7, 8, 7, 8, 9, 0, 0, 7, 5, 4]]

# English
# 1. Use only `random` module
# 2. Set `random.seed(0)`
# 3. Define `matrix: list[list[int]]` with generated
#    16x16 random digits (0-9 inclusive)
# 4. Define `result: int` with sum of inner 4x4 elements
# 5. Inner matrix is exactly in the middle of outer
# 6. Run doctests - all must succeed

# Polish
# 1. Używaj tylko modułu `random`
# 2. Ustaw `random.seed(0)`
# 3. Zdefiniuj `matrix: list[list[int]]` z wygenerowanymi
#    16x16 losowymi cyframi (0-9 włącznie)
# 4. Zdefiniuj `result: int` z sumą środkowych 4x4 elementów
# 5. Środkowa macierz jest dokładnie w środku większej
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...