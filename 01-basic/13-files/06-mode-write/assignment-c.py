"""
* Assignment: File Write List
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
    * `str.join()`
    * `with`
    * `open`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> result
    'sepal_length,sepal_width,petal_length,petal_width,species\\n'
"""

FILE = '_temporary.txt'
DATA = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')

# Write `DATA` to file `FILE`
# Use newline as line terminator
# Use comma as field separator
data = ','.join(DATA) + '\n'
with open(FILE, 'wt') as file:
    file.write(data)
    file.close()



