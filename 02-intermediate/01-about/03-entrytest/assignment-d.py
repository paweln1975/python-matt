"""
* Assignment: About EntryTest ListDict
* Complexity: hard
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Define `result: list[dict]`, where each dict has keys:
       * ip: str
       * hosts: list[str]
    2. Iterate over lines in `DATA` skipping comments (`#`) and empty lines
    3. Extract from each line: `ip` and `hosts`
    4. Add `ip` and `hosts` to `result` as a dict, example:
       {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
    5. Each line must be a separate dict
    6. Mind, that for 127.0.0.1 there will be two separate entries
    7. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[dict]`, gdzie każdy dict ma klucze:
       * ip: str
       * hosts: list[str]
    2. Iteruj po liniach w `DATA` pomijając komentarze (`#`) i puste linie
    3. Wyciągnij z każdej linii: `ip` i `hosts`
    4. Dodaj `ip` i `hosts` do `result` jako słownik, przykład:
       {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
    5. Każda linia ma być osobnym słownikiem
    6. Zwróć uwagę, że dla 127.0.0.1 będą dwa osobne wiersze
    7. Uruchom doctesty - wszystkie muszą się powieść

Why:
    * Check if you know how to parse files
    * Check if you can filter strings
    * Check if you know string methods
    * Check if you know how to iterate over list[dict]

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All keys in `result` should be dict'

    >>> pprint(result, width=120, sort_dicts=False)
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

# Skip comments (`#`) and empty lines
# Extract from each line: `ip` and `hosts`
# Add `ip` and `hosts` to `result` as a dict, example:
# {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
# Each line must be a separate dict
# Mind, that for 127.0.0.1 there will be two separate entries
# type: list[dict]

result = [{'ip': ip, 'hosts': hosts} for line in DATA.splitlines()
          if not (line.strip().startswith('#') or line.strip() == '')
          for ip, *hosts in [line.split()]]

# for line in DATA.splitlines():
#     if line.strip().startswith('#') or line.strip() == '':
#         continue
#     ip, *hosts = line.split()
#     result.append()
