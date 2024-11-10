"""
* Assignment: Comprehension About Round
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: list[float]` with
       rounded values in `DATA` to 2 decimal places
    2. Non-functional requirements:
        a. Use `DATA` variable
        b. Use list comprehension
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list` z
       zaaokrąglonymi wartościami w `DATA` do 2 miejsc po przecinku
    2. Non-functional requirements:
        a. Użyj zmiennej `DATA`
        b. Use list comprehension
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * round()
    * [... for ... in ...]

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'
    >>> assert all(type(x) is float for x in result), \
    'Result should be a list of float'

    >>> result
    [1.11, 2.22, 3.33, 4.44]
"""

DATA = [1.1111, 2.2222, 3.3333, 4.4444]

# Rounded values in `DATA` to 2 decimal places
# type: list[float]
result = [round(x, 2) for x in DATA]

