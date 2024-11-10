"""
* Assignment: Type Float Round
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Euler's number is 2.71828
    2. Round number using `round()` funtion
    3. Run doctests - all must succeed

Polish:
    1. Liczba Eulra to 2.71828
    2. Zaokrąglij liczbę wykorzystując funkcję `round()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert a is not Ellipsis, \
    'Assign your result to variable `a`'
    >>> assert b is not Ellipsis, \
    'Assign your result to variable `b`'
    >>> assert c is not Ellipsis, \
    'Assign your result to variable `c`'
    >>> assert d is not Ellipsis, \
    'Assign your result to variable `d`'
    >>> assert e is not Ellipsis, \
    'Assign your result to variable `e`'

    >>> assert type(a) is float, \
    'Variable `a` has invalid type, should be float'
    >>> assert type(b) is float, \
    'Variable `b` has invalid type, should be float'
    >>> assert type(c) is float, \
    'Variable `c` has invalid type, should be float'
    >>> assert type(d) is float, \
    'Variable `d` has invalid type, should be float'
    >>> assert type(e) is int, \
    'Variable `e` has invalid type, should be int'

    >>> pprint(a)
    2.718

    >>> pprint(b)
    2.72

    >>> pprint(c)
    2.7

    >>> pprint(d)
    3.0

    >>> pprint(e)
    3

"""

EULER = 2.71828

# Round Euler's number to 3 decimal places
# Use `round()`
# type: float
a = round(EULER, 3)

# Round Euler's number to 2 decimal places
# Use `round()`
# type: float
b = round(EULER, 2)

# Round Euler's number to 1 decimal places
# Use `round()`
# type: float
c = round(EULER, 1)

# Round Euler's number to 0 decimal places
# Use `round()`
# type: float
d = round(EULER, 0)

# Round Euler's number to nearest integer
# Use `round()`
# type: int
e = round(EULER)

