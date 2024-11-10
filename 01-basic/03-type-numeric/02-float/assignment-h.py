"""
* Assignment: Type Float Round
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Euler's number is 2.71828
    2. Round number using f-string formatting,
       example: f'{number:.2f}'
    3. Run doctests - all must succeed

Polish:
    1. Liczba Eulra to 2.71828
    2. Zaokrąglij liczbę wykorzystując formatowanie f-string,
       przykład: f'{liczba:.2f}'
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

    >>> assert type(a) is str, \
    'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, \
    'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, \
    'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, \
    'Variable `d` has invalid type, should be str'

    >>> pprint(a)
    'Result: 2.718'

    >>> pprint(b)
    'Result: 2.72'

    >>> pprint(c)
    'Result: 2.7'

    >>> pprint(d)
    'Result: 3'

"""

EULER = 2.71828

# Round Euler's number to 3 decimal places
# Round number using f-string formatting
# type: str
a = f'Result: {EULER:.3f}'

# Round Euler's number to 2 decimal places
# Round number using f-string formatting
# type: str
b = f'Result: {EULER:.2f}'

# Round Euler's number to 1 decimal places
# Round number using f-string formatting
# type: str
c = f'Result: {EULER:.1f}'

# Round Euler's number to 0 decimal places
# Round number using f-string formatting
# type: str
d = f'Result: {EULER:.0f}'

