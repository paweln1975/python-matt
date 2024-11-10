"""
* Assignment: Match Literal Color
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Refactor `if` statement to `match` statement
    2. Use a literal pattern
    3. Run doctests - all must succeed

Polish:
    1. Zrefaktoruj instrukcję warunkową `if` na instrukcję `match`
    2. Użyj literal pattern
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path
    >>> code = Path(__file__).read_text()
    >>> assert 'match' + ' ' + 'color' in code
    >>> assert 'case' in code
"""

color = 'r'

# Refactor `if` statement to `match` statement
# Use a literal pattern
if color == 'r':
    result = 'red'
elif color == 'g':
    result = 'green'
elif color == 'b':
    result = 'blue'


