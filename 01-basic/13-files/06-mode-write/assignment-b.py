"""
* Assignment: File Write Multiline
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Write `DATA` to file `FILE`
    2. Use newline as line terminator
    3. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Użyj newline jako terminator linii
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * There is already a newline `\n` at the end of file
    * `with`
    * `open`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> print(result)
    Fist line
    Second line
    Third line
    <BLANKLINE>
"""

FILE = '_temporary.txt'

DATA = """Fist line
Second line
Third line
"""

# Write `DATA` to file `FILE`
# Use newline as line terminator
with open(FILE, 'wt') as file:
    file.write(DATA)
    file.close()

