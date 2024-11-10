"""
* Assignment: Loop For Count
* Type: class assignment
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Count occurrences of each color
    2. Do not use `list.count()`
    3. Run doctests - all must succeed

Polish:
    1. Zlicz wystąpienia każdego z kolorów
    2. Nie używaj `list.count()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert red is not Ellipsis, \
    'Assign your result to variable `red`'
    >>> assert green is not Ellipsis, \
    'Assign your result to variable `green`'
    >>> assert blue is not Ellipsis, \
    'Assign your result to variable `blue`'

    >>> assert type(red) is int, \
    'Variable `red` has invalid type, should be list'
    >>> assert type(green) is int, \
    'Variable `green` has invalid type, should be list'
    >>> assert type(blue) is int, \
    'Variable `blue` has invalid type, should be list'

    >>> red
    3
    >>> green
    2
    >>> blue
    2
"""

DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

red = 0
green = 0
blue = 0

# If variable COLOR is:
# - 'red' then increment variable `red` by 1
# - 'green' then increment variable `green` by 1
# - 'blue' then increment variable `blue` by 1
for color in DATA:
    match color:
        case 'red':
            red += 1
        case 'green':
            green += 1
        case 'blue':
            blue += 1
