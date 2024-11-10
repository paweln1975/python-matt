"""
* Assignment: CSV DictWriter Schemaless
* Complexity: medium
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Using `csv.DictWriter()` write variable schema data to `FILE`
    2. `fieldnames` must be automatically generated from `DATA`
    3. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `,` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` line terminator
        e. Sort `fieldnames` using `sorted()`
    4. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz dane o zmiennej strukturze do `FILE`
    2. `fieldnames` musi być generowane automatycznie na podstawie `DATA`
    3. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
        e. Posortuj `fieldnames` używając `sorted()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "petal_length","petal_width","sepal_length","sepal_width","species"
    "","","","","virginica"
    "1.4","0.2","","3.5","setosa"
    "4.1","1.3","5.7","","versicolor"
    "","1.8","6.3","2.9","virginica"
    "4.5","","6.4","3.2","versicolor"
    "","","4.7","3.2","setosa"
    "4.7","1.4","","","versicolor"
    "","2.1","7.6","","virginica"
    "1.4","","","3.0","setosa"
    <BLANKLINE>
"""
import csv


DATA = [
    {"species": "virginica"},
    {"sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "species": "setosa"},
    {"sepal_length": 5.7, "petal_length": 4.1, "petal_width": 1.3, "species": "versicolor"},
    {"sepal_length": 6.3, "sepal_width": 2.9, "petal_width": 1.8, "species": "virginica"},
    {"sepal_length": 6.4, "sepal_width": 3.2, "petal_length": 4.5, "species": "versicolor"},
    {"sepal_length": 4.7, "sepal_width": 3.2, "species": "setosa"},
    {"petal_length": 4.7, "petal_width": 1.4, "species": "versicolor"},
    {"sepal_length": 7.6, "petal_width": 2.1, "species": "virginica"},
    {"sepal_width": 3.0, "petal_length": 1.4, "species": "setosa"}
]

FILE = r'_temporary.csv'


# Write DATA to FILE, generate header from DATA
# type: ContextManager
with open(FILE, mode='wt', encoding='utf-8') as file:
    ...


