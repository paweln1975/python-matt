"""
* Assignment: Comprehension List Str
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[float]` with
       converted to str values from `DATA`
    2. Non-functional requirements:
        a. Use `DATA` variable
        b. Use list comprehension
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list` z
       przekształconymi na str wartościami z `DATA`
    2. Non-functional requirements:
        a. Użyj zmiennej `DATA`
        b. Use list comprehension
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * str()
    * [... for ... in ...]

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'
    >>> assert all(type(x) is str for x in result), \
    'Result should be a list of str'

    >>> result
    ['Mark', 'Watney', '40']
"""

DATA = ['Mark', 'Watney', 40]

# Converted to str values from `DATA`
# type: list[float]
result = [str(x) for x in DATA]

