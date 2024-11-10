"""
* Assignment: Conditional If Color
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. If variable COLOR is:
        a. 'red' then increment variable `red` by 1
        b. 'green' then increment variable `green` by 1
        c. 'blue' then increment variable `blue` by 1
    2. Run doctests - all must succeed

Polish:
    1. Jeżeli zmienna COLOR jest:
        a. 'red' to zwiększ zmienną `red` o 1
        b. 'green' to zwiększ zmienną `green` o 1
        c. 'blue' to zwiększ zmienną `blue` o 1
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert red is not Ellipsis, \
    'Assign your result to variable `red`'
    >>> assert green is not Ellipsis, \
    'Assign your result to variable `green`'
    >>> assert blue is not Ellipsis, \
    'Assign your result to variable `blue`'

    >>> assert type(red) is int, \
    'Variable `red` has invalid type, should be int'
    >>> assert type(green) is int, \
    'Variable `green` has invalid type, should be int'
    >>> assert type(blue) is int, \
    'Variable `blue` has invalid type, should be int'

    >>> pprint(red)
    1
    >>> pprint(green)
    0
    >>> pprint(blue)
    0
"""

COLOR = 'red'

red = 0
green = 0
blue = 0

# If variable COLOR is:
# - 'red' then increment variable `red` by 1
# - 'green' then increment variable `green` by 1
# - 'blue' then increment variable `blue` by 1
if COLOR == 'red':
    red += 1
elif COLOR == 'green':
    green += 1
elif COLOR == 'blue':
    blue += 1


