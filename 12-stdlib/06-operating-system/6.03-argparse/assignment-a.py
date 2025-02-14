"""
Name: Argument parsing
Difficulty: easy
Lines: 5
Minutes: 13

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

"""

# %% SetUp

result: float

def avg(*args):
    return sum(args) / len(args)

# English
# 1. Write a script that will parse command line arguments
# 2. It should accept only `int` and `float`
# 3. For arguments it should run `avg()` function from the listing below:
# 4. Run `python argparse_avg.py --numbers 5 10 100 32 -90 27.5`
# 5. Run doctests - all must pass

# Polish
# 1. Napisz parser parametrów linii poleceń
# 2. Ma przyjmować tylko `int` i `float`
# 3. Dla parametrów ma uruchomić funkcje `avg()` z listingu poniżej:
# 4. Uruchamianie `python argparse_avg.py --numbers 5 10 100 32 -90 27.5`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...