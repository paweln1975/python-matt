"""
* Assignment: Syntax Comments Multiline
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Add multiline comment:
       a. first line: This is a first line of a multiline comment
       b. second line: This is a second line of a multiline comment
       b. third line: This is a third line of a multiline comment
    2. Remember to add space after `#` character
    3. Run doctests - all must succeed

Polish:
    1. Dodaj komentarz wieloliniowy:
       a. pierwsza linia: This is a first line of a multiline comment
       b. druga linia: This is a second line of a multiline comment
       c. trzecia linia: This is a third line of a multiline comment
    2. Pamiętaj o dodaniu spacji po znaku `#`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Each line of a multiline comment should start with `# ` characters

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(__file__).read()
    >>> comment = '\\n'.join([
    ...     '#' + ' ' + 'This is a first line of a multiline comment',
    ...     '#' + ' ' + 'This is a second line of a multiline comment',
    ...     '#' + ' ' + 'This is a third line of a multiline comment',
    ... ])

    >>> assert comment in result, \
    'Please write proper multiline comment'
"""

# This is a first line of a multiline comment
# This is a second line of a multiline comment
# This is a third line of a multiline comment
