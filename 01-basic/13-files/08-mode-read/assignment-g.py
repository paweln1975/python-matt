"""
* Assignment: File Read DirtyFile
* Type: homework
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Modify code below:
    2. Read `FILE` to `result: dict`:
        a. key: str - IP address
        b. value: list[str] - list of hosts
    3. Skip line if:
        a. is empty
        b. has only whitespaces
        c. starts with comment `#`
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Wczytaj `FILE` do `result: dict`:
        a. klucz: str - adres IP
        b. wartość: list[str] - lista hostów
    3. Pomiń linię jeżeli:
        a. jest pusta
        b. ma same białe znaki
        c. zaczyna się od komentarza `#`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `with`
    * `open()`
    * `str.strip()`
    * `str.split()` - without an argument
    * `len()`
    * `str.startswith()`
    * `result = True if ... else False`

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

DATA = """
##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)


# Read `FILE` to `result: list[dict]`:
# - key: str - IP address
# - value: list[str] - list of hosts
# Skip line if:
# - is empty
# - has only whitespaces
# - starts with comment `#`
# Example {'10.13.37.1': ['nasa.gov', 'esa.int'], ...}
# type: dict[str,list[str]]
result = {}

with open(FILE, mode='rt') as file:
    for line in file:
        line = line.strip()

        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue

        ip = line.split()[0]
        hosts = line.split()[1:]

        result[ip] = hosts

    file.close()

