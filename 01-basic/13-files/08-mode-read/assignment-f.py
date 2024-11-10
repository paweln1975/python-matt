"""
* Assignment: File Read CleanFile
* Type: homework
* Complexity: medium
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Read `FILE` to `result: dict`:
        a. key: str - IP address
        b. value: list[str] - list of hosts
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: dict`:
        a. klucz: str - adres IP
        b. wartość: list[str] - lista hostów
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.split()`
    * `str.strip()`
    * `with`
    * `open()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'
    >>> assert all(type(x) is str for x in result.keys()), \
    'All keys in `result` should be str'
    >>> assert all(type(x) is list for x in result.values()), \
    'All values in `result` should be list'

    >>> pprint(result, sort_dicts=False)
    {'127.0.0.1': ['localhost'],
     '10.13.37.1': ['nasa.gov', 'esa.int'],
     '255.255.255.255': ['broadcasthost'],
     '::1': ['localhost']}
"""

FILE = '_temporary.txt'

DATA = """127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# Read `FILE` to `result: list[dict]`:
# - key: str - IP address
# - value: list[str] - list of hosts
# Example {'10.13.37.1': ['nasa.gov', 'esa.int'], ...}
# type: dict[str,list[str]]
result = {}

with open(FILE, mode='rt') as file:
    for line in file:
        line = line.strip()
        ip = line.split()[0]
        host = line.split()[1:]
        result[ip] = host
    file.close()



