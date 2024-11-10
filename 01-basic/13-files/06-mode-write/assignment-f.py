"""
* Assignment: File Write Iris
* Type: class assignment
* Complexity: easy
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Flatten `DATA` to list of strings
    2. Write `DATA` to file `FILE`
    3. Use newline as line terminator
    4. Use tab as field separator
    5. Run doctests - all must succeed

Polish:
    1. Spłaszcz `DATA` do listy stringów
    2. Zapisz `DATA` do pliku `FILE`
    3. Użyj newline jako terminator linii
    4. Użyj tab jako separatora pól
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `\t` - tab
    * `str.join()`
    * `list.append()`
    * Add newline `\n` at the end of line and file

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    127.0.0.1 localhost
    10.13.37.1 nasa.gov esa.int
    255.255.255.255 broadcasthost
    ::1 localhost
    <BLANKLINE>
"""

FILE = '_temporary.txt'

DATA = {
    '127.0.0.1': ['localhost'],
    '10.13.37.1': ['nasa.gov', 'esa.int'],
    '255.255.255.255': ['broadcasthost'],
    '::1': ['localhost']
}

# Flatten `DATA` to list of strings
# Write `DATA` to file `FILE`
# Use newline as line terminator
# Use tab as field separator
data = ''
for ip, hosts in DATA.items():
    print (ip, hosts)
    data += ip + ' ' + ' '.join(host for host in hosts) + '\n'


with open(FILE, 'wt') as file:
    file.write(data)
    file.close()



