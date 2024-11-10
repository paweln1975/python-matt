"""
* Assignment: Comprehension About Upper
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[float]` with
       capitalized letters from `DATA`
    2. Non-functional requirements:
        a. Use `DATA` variable
        b. Use list comprehension
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list` z
       literami z `DATA` zapisanymi wielkimi literami
    2. Non-functional requirements:
        a. Użyj zmiennej `DATA`
        b. Use list comprehension
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * str.upper()
    * [... for ... in ...]

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'
    >>> assert all(type(x) is str for x in result), \
    'Result should be a list of str'

    >>> result
    ['A', 'B', 'C', 'D']
"""

DATA = ['a', 'b', 'c', 'd']

# Capitalized letters from `DATA`
# type: list[float]
result = [l.upper() for l in DATA]

