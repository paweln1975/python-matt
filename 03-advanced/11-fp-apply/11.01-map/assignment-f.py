"""
Name: Functional Map JSON
Difficulty: medium
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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert type(result) is map
>>> result = list(result)
>>> assert len(result) == 9

>>> classes = (Setosa, Virginica, Versicolor)
>>> assert all(type(row) in classes for row in result)

>>> result[0]
Virginica(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9)

>>> result[1]
Setosa(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2)

Hints:
`dict.pop()`
`globals()[clsname]`
`cls(*dict)`
`json.loads()`

"""

# %% SetUp

import json
from dataclasses import dataclass

result: map

FILE = r'_temporary.json'

DATA = (
    '[{"sepal_length":5.8,"sepal_width":2.7,"petal_length":5.1,"petal_widt'
    'h":1.9,"species":"virginica"},{"sepal_length":5.1,"sepal_width":3.5,"'
    'petal_length":1.4,"petal_width":0.2,"species":"setosa"},{"sepal_lengt'
    'h":5.7,"sepal_width":2.8,"petal_length":4.1,"petal_width":1.3,"specie'
    's":"versicolor"},{"sepal_length":6.3,"sepal_width":2.9,"petal_length"'
    ':5.6,"petal_width":1.8,"species":"virginica"},{"sepal_length":6.4,"se'
    'pal_width":3.2,"petal_length":4.5,"petal_width":1.5,"species":"versic'
    'olor"},{"sepal_length":4.7,"sepal_width":3.2,"petal_length":1.3,"peta'
    'l_width":0.2,"species":"setosa"},{"sepal_length":7.0,"sepal_width":3.'
    '2,"petal_length":4.7,"petal_width":1.4,"species":"versicolor"},{"sepa'
    'l_length":7.6,"sepal_width":3.0,"petal_length":6.6,"petal_width":2.1,'
    '"species":"virginica"},{"sepal_length":4.9,"sepal_width":3.0,"petal_l'
    'ength":1.4,"petal_width":0.2,"species":"setosa"}]'
)

@dataclass
class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class Setosa(Iris):
    pass

class Virginica(Iris):
    pass

class Versicolor(Iris):
    pass

# English
# 1. Convert from JSON format to Python using decoder function
# 2. Create instances of `Setosa`, `Virginica`, `Versicolor`
#    classes based on value in field "species"
# 3. Generate instances in `result: map`
# 4. Run doctests - all must succeed

# Polish
# 1. Przekonwertuj dane z JSON do Python używając dekodera funkcyjnego
# 2. Twórz obiekty klas `Setosa`, `Virginica`, `Versicolor`
#    w zależności od wartości pola "species"
# 3. Generuj instancje w `result: map`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result

def decoder(data):
    match data:
        case {"species":"virginica", **values}:
            object = Virginica(**values)
        case {"species": "setosa", **values}:
            object = Setosa(**values)
        case {"species": "versicolor", **values}:
            object = Versicolor(**values)
    return object

result = map(decoder, json.loads(DATA))