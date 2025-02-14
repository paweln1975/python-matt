"""
Name: OOP AttributeSlots Repr
Difficulty: medium
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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = [Iris(*row) for row in DATA[1:]]
>>> result  # doctest: +NORMALIZE_WHITESPACE
[Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
 Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
 Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
 Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
 Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
 Iris(4.7, 3.2, 1.3, 0.2, 'setosa')]

>>> iris = result[0]
>>> iris
Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

>>> iris.__slots__
('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

>>> [getattr(iris, x) for x in iris.__slots__]
[5.8, 2.7, 5.1, 1.9, 'virginica']

>>> {x: getattr(iris, x)
...  for x in iris.__slots__}  # doctest: +NORMALIZE_WHITESPACE
{'sepal_length': 5.8,
 'sepal_width': 2.7,
 'petal_length': 5.1,
 'petal_width': 1.9,
 'species': 'virginica'}

>>> iris.__dict__
Traceback (most recent call last):
AttributeError: 'Iris' object has no attribute '__dict__'. Did you mean: '__dir__'?

>>> values = tuple(getattr(iris, x) for x in iris.__slots__)
>>> print(f'Iris{values}')
Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

Hints:
`self.__class__.__name__`
`tuple()`
`dict.values()`

"""

# %% SetUp

from typing import Callable
__repr__: Callable[[object], str]

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# English
# 1. Define method `__repr__` which prints class name and all values
#    positionally, ie. `Iris(5.8, 2.7, 5.1, 1.9, 'virginica')`
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj metodę `__repr__` wypisującą nazwę klasy i wszystkie
#    wartości atrybutów pozycyjnie, np. `Iris(5.8, 2.7, 5.1, 1.9, 'virginica')`
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Iris:
    __slots__ = ('sepal_length', 'sepal_width', 'petal_length',
                 'petal_width', 'species')

    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def _dump(self) -> dict:
        return {x:getattr(self,x) for x in self.__slots__}

    def __repr__(self):
        ...