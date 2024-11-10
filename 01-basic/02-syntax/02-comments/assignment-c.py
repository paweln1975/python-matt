"""
* Assignment: Syntax Comments Inline
* Type: class assignment
* Complexity: easy
* Lines of code: 1 line
* Time: 2 min

English:
    1. Add inline comment to `DATA` variable definition
       with content: This is inline comment
    2. Remember to add space after `#` character
    3. Remember to add two spaces before `#` character
    4. Run doctests - all must succeed

Polish:
    1. Dodaj komentarz na końcu linii do definicji zmiennej `DATA`
       treść: This is inline comment
    2. Pamiętaj o dodaniu spacji po znaku `#`
    3. Pamiętaj o dodaniu dwóch spacji przed znakiem `#`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(__file__).read()
    >>> comment = '  ' + '#' + ' ' + 'This is inline comment'

    >>> assert DATA == 1, \
    'Do not change the value of the `DATA` variable.'

    >>> assert comment in result, \
    'Please write proper inline comment'

"""

DATA = 1  # This is inline comment

