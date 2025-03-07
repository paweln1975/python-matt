"""
Name: OOP MethodClassmethod FromCsv
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Iris)
>>> assert isclass(Setosa)
>>> assert isclass(Versicolor)
>>> assert isclass(Virginica)

>>> data = '5.8,2.7,5.1,1.9,virginica'
>>> virginica = Virginica.from_csv(data)
>>> assert type(virginica.sepal_length) is float
>>> assert type(virginica.sepal_width) is float
>>> assert type(virginica.petal_length) is float
>>> assert type(virginica.petal_width) is float
>>> assert type(virginica.species) is str
>>> assert virginica.sepal_length == 5.8
>>> assert virginica.sepal_width == 2.7
>>> assert virginica.petal_length == 5.1
>>> assert virginica.petal_width == 1.9
>>> assert virginica.species == 'virginica'

>>> data = '5.1,3.5,1.4,0.2,setosa'
>>> setosa = Setosa.from_csv(data)
>>> assert type(setosa.sepal_length) is float
>>> assert type(setosa.sepal_width) is float
>>> assert type(setosa.petal_length) is float
>>> assert type(setosa.petal_width) is float
>>> assert type(setosa.species) is str
>>> assert setosa.sepal_length == 5.1
>>> assert setosa.sepal_width == 3.5
>>> assert setosa.petal_length == 1.4
>>> assert setosa.petal_width == 0.2
>>> assert setosa.species == 'setosa'

>>> data = '5.7,2.8,4.1,1.3,versicolor'
>>> versicolor = Versicolor.from_csv(data)
>>> assert type(versicolor.sepal_length) is float
>>> assert type(versicolor.sepal_width) is float
>>> assert type(versicolor.petal_length) is float
>>> assert type(versicolor.petal_width) is float
>>> assert type(versicolor.species) is str
>>> assert versicolor.sepal_length == 5.7
>>> assert versicolor.sepal_width == 2.8
>>> assert versicolor.petal_length == 4.1
>>> assert versicolor.petal_width == 1.3
>>> assert versicolor.species == 'versicolor'

Hints:
`str.split()`

"""

# %% SetUp

from typing import Callable
Iris: type
from_csv: Callable[[type, str], object]

# English
# 1. Modify class `Iris`
# 2. Define classmethod `from_csv()`:
#    - parameter `line: str`, example: '5.8,2.7,5.1,1.9,virginica'
#    - returns instance of a class on which was called
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Iris`
# 2. Zdefiniuj classmethod `from_csv()`:
#    - parametr `line: str`, przykład: '5.8,2.7,5.1,1.9,virginica'
#    - zwraca instancję klasy na której została wykonana
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    @classmethod
    def from_csv(cls, line: str):
        *values, species = line.split(',')
        values = map(float, values)
        return cls(*values, species)

class Setosa(Iris):
    pass

class Virginica(Iris):
    pass

class Versicolor(Iris):
    pass