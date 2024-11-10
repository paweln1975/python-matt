"""
* Assignment: Loop Dict Endswith
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define `result: list[str]`
    2. Collect in `result` all email addresses from `DATA` -> `crew`
       with domain names mentioned in `DOMAINS`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[str]`
    2. Zbierz w `result` wszystkie adresy email z `DATA` -> `crew`
       z nazwami domenowymi wymienionymi w `DOMAINS`
    3. Uruchom doctesty - wszystkie muszą się powieść

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

DATA = {
    'group': 'staff',
    'created': '2000-01-02',
    'modified': '2000-01-05',
    'users': [
        {'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'},
        {'name': 'Melissa Lewis', 'email': 'mlewis@nasa.gov'},
        {'name': 'Rick Martinez', 'email': 'rmartinez@nasa.gov'},
        {'name': 'Pan Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
        {'name': 'Alex Vogel', 'email': 'avogel@esa.int'},
        {'name': 'Chris Beck', 'email': 'cbeck@nasa.gov'},
        {'name': 'Ivan Ivanovich', 'email': 'iivanovich@roscosmos.ru'},
        {'name': 'Beth Johanssen', 'email': 'bjohanssen@nasa.gov'},
]}

DOMAINS = ('esa.int', 'nasa.gov')

# Email addresses with top-level domain in DOMAINS
# type: list[str]
result = []
users = DATA['users']
for user in users:
    email = user['email']
    if email.endswith(DOMAINS):
        result.append(email)


# advanced

result = []
users = DATA['users']
result = [email for user in users
          if (email := user['email'])
          and email.endswith(DOMAINS)]

