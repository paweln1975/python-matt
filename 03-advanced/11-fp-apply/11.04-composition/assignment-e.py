"""
Name: Functional Composition FilterMap
Difficulty: easy
Lines: 4
Minutes: 3

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(is_valid), \
'Object `is_valid` must be a function'
>>> assert isfunction(transform), \
'Object `transform` must be a function'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'

>>> assert type(result) is tuple, \
'Variable `result` has invalid type, should be tuple'

>>> assert all(type(x) is dict for x in result), \
'All rows in `result` should be dict'

>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'ip': '127.0.0.1', 'hosts': ['localhost']},
 {'ip': '127.0.0.1', 'hosts': ['astromatt']},
 {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']},
 {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
 {'ip': '::1', 'hosts': ['localhost']}]

Hints:
`filter()`
`map()`

"""

# %% SetUp

result: map

DATA = """##
# `/etc/hosts` structure:
#    - ip: internet protocol address (IPv4 or IPv6)
#    - hosts: host names
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""

def is_valid(line):
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True

def transform(line):
    ip, *hosts = line.split()
    return {'ip': ip, 'hosts': hosts}

# English
# 0. Note, this assignment differs from previous by one character in `DATA`
# 1. Filter-out lines from `DATA` when:
#    - line is empty
#    - line has only spaces
#    - starts with # (comment)
# 2. Use `filter()` to apply function `is_valid()` to DATA
# 3. Define `result: map` with result
# 4. Run doctests - all must succeed

# Polish
# 0. Zauważ, że to zadanie od poprzedniego różni się jednym znakiem w `DATA`
# 1. Odfiltruj linie z `DATA` gdy:
#    - linia jest pusta
#    - linia ma tylko spacje
#    - zaczyna się od # (komentarz)
# 2. Użyj `filter()` aby zaaplikować funkcję `is_valid()` do DATA
# 3. Zdefiniuj `result: map` z wynikiem
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = tuple(map(transform, filter(is_valid, map(str.strip, DATA.splitlines()))))