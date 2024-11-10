"""
* Assignment: File Read List of Dicts
* Type: homework
* Complexity: hard
* Lines of code: 21 lines
* Time: 13 min

English:
    1. Modify code below
    2. Read `FILE` to `result: list[dict]`:
        a. ip: str - IP address
        b. hosts: list[str] - list of hosts
        c. protocol: str - 'IPv4' or 'IPv6'
    3. Skip line if:
        a. is empty
        b. has only whitespaces
        c. starts with comment `#`
    4. Merge hosts for the same IP address
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj kod poniżej
    2. Wczytaj `FILE` do `result: list[dict]`:
        a. ip: str - adres IP
        b. hosts: list[str] - lista hostów
    3. Pomiń linię jeżeli:
        a. jest pusta
        b. ma same białe znaki
        c. zaczyna się od komentarza `#`
    4. Scal hosty dla tego samego adresu IP
    5. Uruchom doctesty - wszystkie muszą się powieść

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
    >>> from pprint import pformat
    >>> from os import remove; remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All keys in `result` should be dict'
    >>> assert [x['ip'] for x in result].count('127.0.0.1') == 1, \
    'You did not merge hostnames for the same ip (127.0.0.1)'

    >>> result = pformat(result, sort_dicts=False, width=120)
    >>> print(result)
    [{'ip': '127.0.0.1', 'hostnames': ['localhost', 'astromatt']},
     {'ip': '10.13.37.1', 'hostnames': ['nasa.gov', 'esa.int']},
     {'ip': '255.255.255.255', 'hostnames': ['broadcasthost']},
     {'ip': '::1', 'hostnames': ['localhost']}]
"""

FILE = '_temporary.txt'

DATA = """
##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost
"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# Read `FILE` to `result: list[dict]`:
# - ip: str - IP address
# - hosts: list[str] - list of hosts
# - protocol: str - 'IPv4' or 'IPv6'
# Skip line if:
# - is empty
# - has only whitespaces
# - starts with comment `#`
# Merge hosts for the same IP address
# Example [{'ip': '127.0.0.1', 'hostnames': ['localhost', 'astromatt']}, ...]
# type: list[dict]
result = []

with open(FILE) as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue
        ip = line.split()[0]
        hosts = line.split()[1:]

        for mapping in result:
            if mapping['ip'] == ip:
                mapping['hostnames'] += hosts
                break
        else:
            result.append(
                dict(ip=ip,
                     hostnames=hosts)
            )
