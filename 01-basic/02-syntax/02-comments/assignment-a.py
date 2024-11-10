"""
* Assignment: Syntax Comments Line
* Type: class assignment
* Complexity: easy
* Lines of code: 1 line
* Time: 2 min

English:
    1. Add line comment: This is my first Python script
    2. Remember to add space after `#` character
    3. Run doctests - all must succeed

Polish:
    1. Dodaj komentarz liniowy: This is my first Python script
    2. Pamiętaj o dodaniu spacji po znaku `#`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(__file__).read()
    >>> comment = '#' + ' ' + 'This is my first Python script'

    >>> assert comment in result, \
    'Please write proper line comment'
"""

# This is my first Python script
