"""
Name: DesignPatterns Creational FactoryMethod
Difficulty: easy
Lines: 6
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

>>> from pprint import pprint

>>> result = map(iris, DATA[1:])
>>> pprint(list(result), width=120)
[Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9),
 Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2),
 Versicolor(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3),
 Virginica(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8),
 Versicolor(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5),
 Setosa(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2)]

Hints:
`globals()[classname]`

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
iris: Callable[[tuple[float,float,float,float,str]], object]

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

@dataclass
class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Setosa(Iris):
    pass

class Versicolor(Iris):
    pass

class Virginica(Iris):
    pass

# English
# 1. Create polymorphism factory `iris` producing instances of `Iris`
# 2. Separate `values` from `species` in each row
# 3. Create instances of:
#    - class `Setosa` if `species` is "setosa"
#    - class `Versicolor` if `species` is "versicolor"
#    - class `Virginica` if `species` is "virginica"
# 4. Initialize instances with `values`
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz fabrykę abstrakcyjną `iris` tworzącą instancje klasy `Iris`
# 2. Odseparuj `values` od `species` w każdym wierszu
# 3. Stwórz instancje:
#    - klasy `Setosa` jeżeli `species` to "setosa"
#    - klasy `Versicolor` jeżeli `species` to "versicolor"
#    - klasy `Virginica` jeżeli `species` to "virginica"
# 4. Instancje inicjalizuj danymi z `values`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    ...