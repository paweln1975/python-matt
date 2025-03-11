"""
Name: OOP ClassFactory Iris
Difficulty: medium
Lines: 8
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

>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[Virginica(5.8, 2.7, 5.1, 1.9),
 Setosa(5.1, 3.5, 1.4, 0.2),
 Versicolor(5.7, 2.8, 4.1, 1.3),
 Virginica(6.3, 2.9, 5.6, 1.8),
 Versicolor(6.4, 3.2, 4.5, 1.5),
 Setosa(4.7, 3.2, 1.3, 0.2)]

Hints:
`globals()[classname]`

"""

# %% SetUp

result: list['Iris']

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

header, *rows = DATA

class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def __repr__(self):
        name = self.__class__.__name__
        args = tuple(self.__dict__.values())
        return f'{name}{args}'

# English
# 1. Define `result: list[Iris]`
# 2. Iterate over `DATA` rows (skip header - first row)
# 3. Separate `values` from `species` in each row
# 4. Append to `result`:
#    - if `species` is "setosa" append an instance of a class `Setosa`
#    - if `species` is "versicolor" append an instance of a class `Versicolor`
#    - if `species` is "virginica" append an instance of a class `Virginica`
# 5. Initialize instances with `values` using `*args` notation
# 6. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[Iris]`
# 2. Iteruj po wierszach w `DATA` (pomiń nagłówek - pierwszy wiersz)
# 3. Odseparuj `values` od `species` w każdym wierszu
# 4. Dodaj do `result`:
#    - jeżeli `species` jest "setosa" to dodaj instancję klasy `Setosa`
#    - jeżeli `species` jest "versicolor" to dodaj instancję klasy `Versicolor`
#    - jeżeli `species` jest "virginica" to dodaj instancję klasy `Virginica`
# 5. Instancje inicjalizuj danymi z `values` używając notacji `*args`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def factory(row):
    *values, species = row
    classname = species.capitalize()
    cls = type(classname, (Iris,), {})
    return cls(*values)

result = list(map(factory, DATA[1:]))