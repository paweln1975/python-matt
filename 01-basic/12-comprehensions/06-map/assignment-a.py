"""
* Assignment: Comprehension About Float
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[float]` with
       converted to float values from `DATA`
    2. Non-functional requirements:
        a. Use `DATA` variable
        b. Use list comprehension
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list` z
       przekształconymi na float wartościami z `DATA`
    2. Non-functional requirements:
        a. Użyj zmiennej `DATA`
        b. Use list comprehension
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * float()
    * [... for ... in ...]

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'
    >>> assert all(type(x) is float for x in result), \
    'Result should be a list of float'

    >>> result
    [0.0, 1.0, 2.0, 3.0, 4.0]
"""

DATA = [0, 1, 2, 3, 4]

# Converted to float values from `DATA`
# type: list[float]
result = [float(x) for x in DATA]

