"""
* Assignment: Iterator MapFilter Apply
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    0. Note, this assignment differs from previous by one character in `DATA`
    1. Filter-out lines from `DATA` when:
        a. line is empty
        b. line has only spaces
        c. starts with # (comment)
    2. Use `filter()` to apply function `valid_line()` to DATA
    3. Define `result: map` with result
    4. Run doctests - all must succeed

Polish:
    0. Zauważ, że to zadanie od poprzedniego różni się jednym znakiem w `DATA`
    1. Odfiltruj linie z `DATA` gdy:
        a. linia jest pusta
        b. linia ma tylko spacje
        c. zaczyna się od # (komentarz)
    2. Użyj `filter()` aby zaaplikować funkcję `valid_line()` do DATA
    3. Zdefiniuj `result: map` z wynikiem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * filter()
    * map()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(transform), \
    'Object `parse` must be a function'

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is map, \
    'Variable `result` has invalid type, should be map'

    >>> result = list(result)
    >>> assert type(result) is list, \
    'Evaluated `result` has invalid type, should be list'

    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [{'ip': '127.0.0.1', 'hosts': ['localhost']},
     {'ip': '127.0.0.1', 'hosts': ['astromatt']},
     {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']},
     {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
     {'ip': '::1', 'hosts': ['localhost']}]

"""

DATA = """##
# `/etc/hosts` structure:
#   - IPv4 or IPv6
#   - Hostnames
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""


def valid_line(line):
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True


def transform(line):
    ip, *hosts = line.split()
    return {'ip': ip, 'hosts': hosts}


# Note, this assignment differs from previous by one character in `DATA`
# Filter-out lines from `DATA` when:
# - line is empty
# - line has only spaces
# - starts with # (comment)
# Use `filter()` to apply function `valid_line()` to DATA
# type: map
result = ...

