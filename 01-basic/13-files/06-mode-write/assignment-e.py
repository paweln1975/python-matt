"""
* Assignment: File Write CSV
* Type: class assignment
* Complexity: medium
* Lines of code: 6 lines
* Time: 5 min

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
    * `','.join(...)`
    * `[str(x) for x in ...]`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> print(result)
    sepal_length,sepal_width,petal_length,petal_width,species
    5.8,2.7,5.1,1.9,virginica
    5.1,3.5,1.4,0.2,setosa
    5.7,2.8,4.1,1.3,versicolor
    6.3,2.9,5.6,1.8,virginica
    6.4,3.2,4.5,1.5,versicolor
    4.7,3.2,1.3,0.2,setosa
    <BLANKLINE>
"""

FILE = '_temporary.csv'

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# Write `DATA` to file `FILE`
# Use newline as line terminator
# Use comma as field separator

data = ''
for row in DATA:
    data_row = ','.join(str(x) for x in row)
    data += data_row + '\n'
    
with open(FILE, 'wt') as file:
    file.write(data)
    file.close()

