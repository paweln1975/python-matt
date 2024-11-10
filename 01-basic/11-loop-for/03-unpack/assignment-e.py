"""
* Assignment: Loop Unpack Endswith
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use `DATA: list[tuple]`
    2. Define `result: list` with:
       email addresses from `DATA` with domain names listed in `DOMAINS`
    3. Use unpack syntax in a for loop
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: list[tuple]`
    2. Zdefiniuj `result: list` z:
       adresami email z `DATA` z domenami wymienionymi w `DOMAINS`
    3. Użyj składni rozpakowania w pętli for
    4. Uruchom doctesty - wszystkie muszą się powieść

Why:
    * Check if you can filter data
    * Check if you know string methods
    * Check if you know how to iterate over list[dict]

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Result must be a list'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is str for element in result), \
    'All elements in result must be a str'

    >>> result = sorted(result)
    >>> pprint(result)
    ['avogel@esa.int',
     'bjohanssen@nasa.gov',
     'cbeck@nasa.gov',
     'mlewis@nasa.gov',
     'mwatney@nasa.gov',
     'rmartinez@nasa.gov']
"""

DATA = [
    ('Mark', 'Watney', 'mwatney@nasa.gov'),
    ('Melissa', 'Lewis', 'mlewis@nasa.gov'),
    ('Rick', 'Martinez', 'rmartinez@nasa.gov'),
    ('Alex', 'Vogel', 'avogel@esa.int'),
    ('Chris', 'Beck', 'cbeck@nasa.gov'),
    ('Beth', 'Johanssen', 'bjohanssen@nasa.gov'),
    ('Pan', 'Twardowski', 'ptwardowski@polsa.gov.pl'),
    ('Ivan', 'Ivanovich', 'iivanovich@roscosmos.ru'),
]

DOMAINS = ('esa.int', 'nasa.gov')

# Define `result: list` with:
# email addresses from `DATA` with domain names listed in `DOMAINS`
# Use unpack syntax in a for loop
# type: list[str]

result = []
for *names, email in DATA:
    if email.endswith(DOMAINS):
        result.append(email)

# advanced
result = [email
          for *names, email in DATA
          if email.endswith(DOMAINS)]

