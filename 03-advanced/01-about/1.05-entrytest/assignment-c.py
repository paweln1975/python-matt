"""
Name: About EntryTest Endswith
Difficulty: easy
Lines: 6
Minutes: 5

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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is list, \
'Result must be a list'
>>> assert len(result) > 0, \
'Result cannot be empty'
>>> assert all(type(element) is str for element in result), \
'All elements in result must be a str'

>>> from pprint import pprint
>>> result = sorted(result)
>>> pprint(result)
['avogel@esa.int',
 'bjohanssen@nasa.gov',
 'cbeck@nasa.gov',
 'mlewis@nasa.gov',
 'mwatney@nasa.gov',
 'rmartinez@nasa.gov']

Why:
Check if you can filter data
Check if you know string methods
Check if you know how to iterate over `list[dict]`

"""

# %% SetUp

result: list[str]

DATA = {
    'project': 'myproject',
    'app': 'ares',
    'model': 'User',
    'values': [
        {'pk': 1, 'firstname': 'Melissa', 'lastname': 'Lewis', 'email': 'mlewis@nasa.gov'},
        {'pk': 2, 'firstname': 'Rick', 'lastname': 'Martinez', 'email': 'rmartinez@nasa.gov'},
        {'pk': 3, 'firstname': 'Alex', 'lastname': 'Vogel', 'email': 'avogel@esa.int'},
        {'pk': 4, 'firstname': 'Pan', 'lastname': 'Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
        {'pk': 5, 'firstname': 'Chris', 'lastname': 'Beck', 'email': 'cbeck@nasa.gov'},
        {'pk': 6, 'firstname': 'Beth', 'lastname': 'Johanssen', 'email': 'bjohanssen@nasa.gov'},
        {'pk': 7, 'firstname': 'Mark', 'lastname': 'Watney', 'email': 'mwatney@nasa.gov'},
        {'pk': 8, 'firstname': 'Ivan', 'lastname': 'Ivanovich', 'email': 'iivanovich@roscosmos.ru'},
    ]}

DOMAINS = ('esa.int', 'nasa.gov')

# English
# 1. Define `result: list[str]` with all email addresses having domain name in `DOMAINS`
# 2. Search for emails only in `DATA` -> `values`
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[str]` z wszystkimi adresami email mającymi domenę z `DOMAINS`
# 2. Szukaj adresów email tylko w `DATA` -> `values`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def valid_email(email: str) -> bool:
    """
    >>> valid_email('ptwardowski@polsa.gov.pl')
    False
    >>> valid_email('mwatney@nasa.gov')
    True
    """
    _, domain = email.split('@')
    return domain in DOMAINS

emails = (user['email'] for user in DATA['values'])
result = list(filter(valid_email, emails))
