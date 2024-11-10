

"""
* Assignment: Serialization Dump Schemaless
* Complexity: hard
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Define function `dump()`:
        a. Argument: `data: list[tuple]`, `file: str`
        b. Returns: `None`
        c. Function writes `data` to `file` in CSV format
        d. Add quotes to values
    2. Sort header
    3. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: `"`
       c. Quoting: always
       d. Delimiter: `,`
       e. Lineseparator: `\n`
       f. Sort `fieldnames`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `dump()`:
        a. Argument: `data: list[tuple]`, `file: str`
        b. Zwraca: `None`
        c. Funkcja zapisuje `data` do `file` w formacie CSV
        d. Dodaj cudzysłowia do wartości
    2. Posortuj header
    3. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: `"`
       c. Quoting: zawsze
       d. Delimiter: `,`
       e. Lineseparator: `\n`
       f. Posortuj `fieldnames`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `sorted()`
    * `set()`
    * `set.update()`
    * `str.join()`
    * `dict.get(..., default)`

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
    "petal_length","petal_width","sepal_length","sepal_width","species"
    "","","5.1","3.5","setosa"
    "4.1","1.3","","","versicolor"
    "","1.8","6.3","","virginica"
    "","0.2","5.0","","setosa"
    "4.1","","","2.8","versicolor"
    "","1.8","","2.9","virginica"
    <BLANKLINE>

    >>> remove(FILE)
"""

FILE = '_temporary.csv'

DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'species': 'setosa'},
    {'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.0, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_width': 2.8, 'petal_length': 4.1, 'species': 'versicolor'},
    {'sepal_width': 2.9, 'petal_width': 1.8, 'species': 'virginica'},
]

# Define function `dump()`:
# - Argument: `data: list[tuple]`, `file: str`
# - Returns: `None`
# - Function writes `data` to `file` in CSV format
# - Add quotes to values
# Sort header
# type: Callable[[list[tuple]], str]
def dump(data, file):
    ...


