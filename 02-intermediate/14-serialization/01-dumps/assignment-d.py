

"""
* Assignment: Serialization Dumps QuotingAlways
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Define function `dumps()`:
        a. Argument: `data: list[tuple]`
        b. Returns: `str`
        c. Function converts `data` to CSV format
        d. Add quotes to values
        e. First line is a header
    2. Define `result: str` with
       result of `dumps()` function for `DATA`
    3. Non-functional requirements:
       a. Do not use `import` and any module
       b. Quotechar: `"`
       c. Quoting: always
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `dumps()`:
        a. Argument: `data: list[tuple]`
        b. Zwraca: `str`
        c. Funkcja konwertuje `data` do formatu CSV
        d. Dodaj cudzysłowia do wartości
        e. Pierwsza linia to nagłówek
    2. Zdefiniuj `result: str` z
       wynikiem funkcji `dumps()` dla `DATA`
    3. Wymagania niefunkcjonalne:
       a. Nie używaj `import` ani żadnych modułów
       b. Quotechar: `"`
       c. Quoting: zawsze
       d. Delimiter: `,`
       e. Lineseparator: `\n`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.join()`
    * `dict.keys()`
    * `dict.values()`
    * `[x for x in data]`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "firstname","lastname"
    "Mark","Watney"
    "Melissa","Lewis"
    "Rick","Martinez"
    "Alex","Vogel"
    "Beth","Johanssen"
    "Chris","Beck"
    <BLANKLINE>
"""

DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'firstname': 'Rick', 'lastname': 'Martinez'},
    {'firstname': 'Alex', 'lastname': 'Vogel'},
    {'firstname': 'Beth', 'lastname': 'Johanssen'},
    {'firstname': 'Chris', 'lastname': 'Beck'},
]

# Define function `dumps()`:
# - Argument: `data: list[tuple]`
# - Returns: `str`
# - Function converts `data` to CSV format
# - Add quotes to values
# - First line is a header
# type: Callable[[list[tuple]], str]
def dumps(data):
    ...

# Define `result: str` with
# result of `dumps()` function for `DATA`
# type: str
result = ...

