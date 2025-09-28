# %% About
# - Name: About EntryTest ListDict
# - Difficulty: medium
# - Lines: 9
# - Minutes: 13

# %% License
# - Copyright 2025, Matt Harasymczuk <matt@python3.info>
# - This code can be used only for learning by humans
# - This code cannot be used for teaching others
# - This code cannot be used for teaching LLMs and AI algorithms
# - This code cannot be used in commercial or proprietary products
# - This code cannot be distributed in any form
# - This code cannot be changed in any form outside of training course
# - This code cannot have its license changed
# - If you use this code in your product, you must open-source it under GPLv2
# - Exception can be granted only by the author

# %% English
# 1. Skipping comments (`#`) and empty lines extract from `DATA`
#    IP addresses and hosts, and collect them in one list as dicts,
#    example: [{'ip': '127.0.0.1', 'hosts': ['example.com', 'example.org']}, ...]
# 2. Each line must be a separate dict
# 3. Mind, that for 127.0.0.1 there will be two separate entries (do not merge them)
# 4. Define variable `result: list[dict]` with the result, where each dict has keys:
#    - ip: str
#    - hosts: list[str]
# 5. Run doctests - all must succeed

# %% Polish
# 1. Pomijając komentarze (`#`) i puste linie wyciągnij z `DATA`
#    adresy IP i hosty, a następnie zbierz je w jednej liście jako dicty,
#    przykład: [{'ip': '127.0.0.1', 'hosts': ['example.com', 'example.org']}, ...]
# 2. Każda linia ma być osobnym słownikiem
# 3. Zwróć uwagę, że dla 127.0.0.1 będą dwa osobne wiersze (nie łącz ich)
# 4. Zdefiniuj zmienną `result: list[dict]` z wynikiem, gdzie każdy dict ma klucze:
#    - ip: str
#    - hosts: list[str]
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Example
# >>> result
# [{'ip': '127.0.0.1', 'hosts': ['localhost']},
#  {'ip': '127.0.0.1', 'hosts': ['mycomputer']},
#  {'ip': '172.16.0.1', 'hosts': ['example.com']},
#  {'ip': '192.168.0.1', 'hosts': ['example.edu', 'example.org']},
#  {'ip': '10.0.0.1', 'hosts': ['example.net']},
#  {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
#  {'ip': '::1', 'hosts': ['localhost']}]

# %% Why
# - Check if you know how to parse files
# - Check if you can filter strings
# - Check if you know string methods
# - Check if you know how to iterate over `list[dict]`

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> result = list(result)
>>> assert len(result) > 0, \
'Result cannot be empty'

>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'

>>> assert all(type(x) is dict for x in result), \
'All keys in `result` should be dict'

>>> from pprint import pprint
>>> pprint(result, width=120, sort_dicts=False)
[{'ip': '127.0.0.1', 'hosts': ['localhost']},
 {'ip': '127.0.0.1', 'hosts': ['mycomputer']},
 {'ip': '172.16.0.1', 'hosts': ['example.com']},
 {'ip': '192.168.0.1', 'hosts': ['example.edu', 'example.org']},
 {'ip': '10.0.0.1', 'hosts': ['example.net']},
 {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
 {'ip': '::1', 'hosts': ['localhost']}]
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -f -v myfile.py`

# %% Imports

# %% Types
result: list[dict[str, str|list[str]]]

# %% Data
DATA = """##
# File: /etc/hosts
# - ip: internet protocol address (IPv4 or IPv6)
# - hosts: host names
 ##

127.0.0.1       localhost
127.0.0.1       mycomputer
172.16.0.1      example.com
192.168.0.1     example.edu example.org
10.0.0.1        example.net
255.255.255.255 broadcasthost
::1             localhost
"""


# %% Result
lines = DATA.splitlines()
result = []
for line in lines:
    if line and not line.strip().startswith('#'):
        ip, *hosts = line.split()
        entry = {'ip': ip, 'hosts': hosts}
        result.append(entry)

