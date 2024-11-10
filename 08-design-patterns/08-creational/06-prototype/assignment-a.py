"""
* Assignment: DesignPatterns Creational PrototypeDate
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Create class `Date` with:
        a. `year: int`
        b. `month: int`
        c. `day: int`
        d. method `.clone()`
    2. Method `.clone()` returns another `Date` with the same values
    3. Do not use `vars(self)`
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Date` z:
        a. `year: int`
        b. `month: int`
        c. `day: int`
        d. metodą `.clone()`
    2. Metoda `.clone()` zwraca kolejny `Date` z tymi samymi wartościami
    3. Nie używaj `vars(self)`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> date = Date(1969, 7, 21)
    >>> result = date.clone()

    >>> result.year
    1969
    >>> result.month
    7
    >>> result.day
    21
"""
from dataclasses import dataclass


@dataclass
class Date:
    year: int
    month: int
    day: int


