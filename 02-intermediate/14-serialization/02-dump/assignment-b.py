

"""
* Assignment: Serialization Dump ListObject
* Complexity: medium
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Define function `dump()`:
        a. Argument: `data: list[tuple]`, `file: str`
        b. Returns: `None`
        c. Function writes `data` to `file` in CSV format
        d. Add quotes to values
    2. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: `"`
       c. Quoting: always
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `dump()`:
        a. Argument: `data: list[tuple]`, `file: str`
        b. Zwraca: `None`
        c. Funkcja zapisuje `data` do `file` w formacie CSV
        d. Dodaj cudzysłowia do wartości
    2. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: `"`
       c. Quoting: zawsze
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `vars()`
    * `tuple()`
    * `dict.keys()`
    * `dict.values()`
    * `list.append()`
    * `list.extend()`
    * `str.join()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> dump(DATA, file=FILE)
    >>> result = open(FILE).read()

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert result != '', \
    'File content is empty'

    >>> print(result)
    "sepal_length","sepal_width","petal_length","petal_width","species"
    "5.1","3.5","1.4","0.2","setosa"
    "5.8","2.7","5.1","1.9","virginica"
    "5.1","3.5","1.4","0.2","setosa"
    "5.7","2.8","4.1","1.3","versicolor"
    "6.3","2.9","5.6","1.8","virginica"
    "6.4","3.2","4.5","1.5","versicolor"
    <BLANKLINE>

    >>> remove(FILE)
"""

class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species


FILE = '_temporary.csv'

DATA = [
    Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    Iris(5.8, 2.7, 5.1, 1.9, 'virginica'),
    Iris(5.1, 3.5, 1.4, 0.2, 'setosa'),
    Iris(5.7, 2.8, 4.1, 1.3, 'versicolor'),
    Iris(6.3, 2.9, 5.6, 1.8, 'virginica'),
    Iris(6.4, 3.2, 4.5, 1.5, 'versicolor'),
]

# Define function `dump()`:
# - Argument: `data: list[tuple]`, `file: str`
# - Returns: `None`
# - Function writes `data` to `file` in CSV format
# - Add quotes to values
# type: Callable[[list[tuple]], None]
def dump(data, file):
    ...


