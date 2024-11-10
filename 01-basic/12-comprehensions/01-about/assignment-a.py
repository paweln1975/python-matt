"""
* Assignment: Comprehension About Range
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[int]` with
       numbers from 0 to 5 (without 5)
    2. Non-functional requirements:
        a. Use list comprehension
        b. Use `range()` function
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[int]` z
       liczbami od 0 do 5 (bez 5)
    2. Non-functional requirements:
        a. Użyj list comprehension
        b. Użyj funkcji `range()`
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * [... for ... in ...]
    * range()
    * range parameter `start` is inclusive
    * range parameter `stop` is exclusive

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'
    >>> assert all(type(x) is int for x in result), \
    'Result should be a list of int'

    >>> result
    [0, 1, 2, 3, 4]
"""

# Numbers from 0 to 5 (without 5)
# type: list[int]
result = [x for x in range(0, 5)]

