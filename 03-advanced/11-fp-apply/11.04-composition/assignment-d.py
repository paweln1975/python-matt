"""
Name: Functional Composition FilterMap
Difficulty: easy
Lines: 3
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(is_valid), \
'Object `is_valid` must be a function'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'

>>> result = list(result)
>>> assert type(result) is list, \
'Evaluated `result` has invalid type, should be list'

>>> assert all(type(x) is dict for x in result), \
'All rows in `result` should be dict'

>>> assert all(type(key) is str
...            for row in result
...            for key in row.keys()), \
'All rows in `result` should be dict'

>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']},
 {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']},
 {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
 {'ip': '::1', 'hosts': ['localhost']}]

Hints:
`filter()`
`map()`
`len()`
`str.split()`
`str.startswith()`

"""

# %% SetUp

result: list[dict]

DATA = """##
# `/etc/hosts` structure:
#    - ip: internet protocol address (IPv4 or IPv6)
#    - hosts: host names
##

127.0.0.1       localhost astromatt
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
# 1. Define `result: list[dict]`, where each dict has keys:
#    - ip: str
#    - hosts: list[str]
# 2. Skip comments (`#`) and empty lines
# 3. Extract from each line: `ip` and `hosts`
# 4. Add `ip` and `hosts` to `result` as a dict
#    example: {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
# 5. Each line must be a separate dict
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[dict]`, gdzie każdy dict ma klucze:
#    - ip: str
#    - hosts: list[str]
# 2. Pomiń komentarze (`#`) i puste linie
# 3. Wyciągnij z każdej linii: `ip` i `hosts`
# 4. Dodaj `ip` i `hosts` do `result` jako słownik
#    przykład: {'ip': '127.0.0.1', 'hosts': ['localhost', 'astromatt']}
# 5. Każda linia ma być osobnym słownikiem
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = map(transform, filter(is_valid, DATA.splitlines()))