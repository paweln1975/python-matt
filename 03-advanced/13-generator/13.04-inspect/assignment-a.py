"""
Name: Generator Function Iris
Difficulty: easy
Lines: 8
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from sys import getsizeof
>>> from inspect import isfunction, isgeneratorfunction

>>> assert isfunction(function)
>>> assert isgeneratorfunction(generator)

>>> list(function(DATA, 'setosa'))
[[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]
>>> list(generator(DATA, 'setosa'))
[[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]

>>> getsizeof(function(DATA, 'setosa'))
88
>>> getsizeof(function(DATA*10, 'setosa'))
248
>>> getsizeof(function(DATA*100, 'setosa'))
1656
>>> getsizeof(generator(DATA, 'setosa'))
216
>>> getsizeof(generator(DATA*10, 'setosa'))
216
>>> getsizeof(generator(DATA*100, 'setosa'))
216

"""

# %% SetUp

from typing import Callable, Generator
function: Callable[[list[float|str], str], list[float]]
generator: Callable[[list[float|str], str], Generator[list[float], None, None]]

DATA = [
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# English
# 1. Write filter for `DATA` which returns `features: list[float]` for given `species: str`
# 2. Implement solution using function
# 3. Implement solution using generator and `yield` keyword
# 4. Compare results of both using `sys.getsizeof()`
# 5. What will happen if input data will be bigger?
# 6. Note, that in different Python versions you'll get slightly
#    different values for getsizeof generator and function:
#    - 216 for generator in Python 3.13
#    - 216 for generator in Python 3.12
#    - 224 for generator in Python 3.11
#    - 104 for generator in Python 3.10
#    - 112 for generator in Python 3.9
#    - 112 for generator in Python 3.8
#    - 120 for generator in Python 3.7
# 7. Run doctests - all must succeed

# Polish
# 1. Napisz filtr dla `DATA` zwracający `features: list[float]` dla danego gatunku `species: str`
# 2. Zaimplementuj rozwiązanie wykorzystując funkcję
# 3. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
# 4. Porównaj wyniki obu używając `sys.getsizeof()`
# 5. Co się stanie, gdy ilość danych będzie większa?
# 6. Zwróć uwagę, że w zależności od wersji Python wartości getsizeof
#    dla funkcji i generatora mogą się nieznaczenie różnić:
#    - 216 dla generator w Python 3.13
#    - 216 dla generator w Python 3.12
#    - 224 dla generator w Python 3.11
#    - 104 dla generator w Python 3.10
#    - 112 dla generator w Python 3.9
#    - 112 dla generator w Python 3.8
#    - 120 dla generator w Python 3.7
# 7. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def function(data: list, species: str):
    ...

def generator(data: list, species: str):
    ...