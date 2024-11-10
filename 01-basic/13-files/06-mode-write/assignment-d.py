"""
* Assignment: File Write Non-Str
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Write `DATA` to file `FILE`
    2. Use newline as line terminator
    3. Use comma as field separator
    4. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Użyj newline jako terminator linii
    3. Użyj przecinek jako separatora pól
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Add newline `\n` at the end of line and file
    * Comprehension
    * `str.join()`
    * `with`
    * `open`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> result
    '5.1,3.5,1.4,0.2,setosa\\n'
"""

FILE = '_temporary.txt'
DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

# Write `DATA` to file `FILE`
# Use newline as line terminator
# Use comma as field separator
data = ','.join(str(x) for x in DATA)
with open(FILE, 'wt') as file:
    file.write(data + '\n')
    file.close()

