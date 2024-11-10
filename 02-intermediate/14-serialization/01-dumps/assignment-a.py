

"""
* Assignment: Serialization Dumps ListTuple
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define function `dumps()`:
        a. Argument: `data: list[tuple]`
        b. Returns: `str`
        c. Function converts `data` to CSV format
        d. Do not add quotes to values
    2. Define `result: str` with
       result of `dumps()` function for `DATA`
    3. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: None
       c. Quoting: never
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `dumps()`:
        a. Argument: `data: list[tuple]`
        b. Zwraca: `str`
        c. Funkcja konwertuje `data` do formatu CSV
        d. Nie dodawaj cudzysłowiów do wartości
    2. Zdefiniuj `result: str` z
       wynikiem funkcji `dumps()` dla `DATA`
    3. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: None
       c. Quoting: nigdy
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `[x for x in data]`
    * `str.join()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    sepal_length,sepal_width,petal_length,petal_width,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    7.0,3.2,4.7,1.4,versicolor
    7.6,3.0,6.6,2.1,virginica
    4.9,3.0,1.4,0.2,setosa
    <BLANKLINE>
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
]

# Define function `dumps()`:
# - Argument: `data: list[tuple]`
# - Returns: `str`
# - Function converts `data` to CSV format
# - Do not add quotes to values
# type: Callable[[list[tuple]], str]
def dumps(data):
    ...

# Define `result: str` with
# result of `dumps()` function for `DATA`
# type: str
result = ...


