"""
* Assignment: Comprehension About Create
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: dict` with:
       a. `key: int` integer from 1 to 5 (exclusive)
       b. `value: str` value for key squared (raised to the power of 2)
       c. example: `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`
    2. Non-functional requirements:
        a. Use list comprehension
        b. Use `range()` function
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict` z:
       a. `klucz: int` liczba całkowita od 0 do 5 (rozłącznie)
       b. `wartość: str` wartość dla klucza podniesiona do kwadratu
       c. przykład: `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`
    2. Non-functional requirements:
        a. Użyj list comprehension
        b. Użyj funkcji `range()`
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * [... for ... in ...]
    * range(start,stop)
    * start is inclusive
    * stop is exclusive

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Result should be a dict'
    >>> assert all(type(x) is int for x in result), \
    'Result should be a list of int'

    >>> result
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
"""

# `key: int` integer from 1 to 5 (exclusive)
# `value: str` value for key squared (raised to the power of 2)
# example: `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`
# type: dict[int,int]
result = {x:x**2 for x in range(5)}
