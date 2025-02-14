"""
Name: Functional Recap Json2Csv
Difficulty: medium
Lines: 10
Minutes: 13

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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint

>>> result = list(result)
>>> assert type(result) is list
>>> assert len(result) > 0
>>> assert all(type(x) is dict for x in result)

>>> pprint(result, width=112, sort_dicts=False)  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Mark',
  'lastname': 'Watney',
  'addresses': '2101 E NASA Pkwy,Houston,77058,Texas,USA;,Kennedy Space Center,32899,Florida,USA'},
 {'firstname': 'Melissa',
  'lastname': 'Lewis',
  'addresses': '4800 Oak Grove Dr,Pasadena,91109,California,USA;2825 E Ave P,Palmdale,93550,California,USA'},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'addresses': ''},
 {'firstname': 'Alex',
  'lastname': 'Vogel',
  'addresses': 'Linder Hoehe,Cologne,51147,North Rhine-Westphalia,Germany'}]

Hints:
`map()`
`dict()`
`dict.values()`
`dict.get()`
`str.join()`

"""

# %% SetUp

result: map

DATA = [
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "2101 E NASA Pkwy",
         "city": "Houston",
         "postcode": 77058,
         "region": "Texas",
         "country": "USA"},
        {"street": "",
         "city": "Kennedy Space Center",
         "postcode": 32899,
         "region": "Florida",
         "country": "USA"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": [
        {"street": "4800 Oak Grove Dr",
         "city": "Pasadena",
         "postcode": 91109,
         "region": "California",
         "country": "USA"},
        {"street": "2825 E Ave P",
         "city": "Palmdale",
         "postcode": 93550,
         "region": "California",
         "country": "USA"}]},

    {"firstname": "Rick", "lastname": "Martinez", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe",
         "city": "Cologne",
         "postcode": 51147,
         "region": "North Rhine-Westphalia",
         "country": "Germany"}]}
]

# English
# 1. Write data with relations to CSV format
# 2. Convert `DATA` to `result: list[dict[str,str]]`
# 3. Non-functional requirements:
#    - Use `,` to separate fields
#    - Use `;` to separate instances
# 4. Contact has zero or many addresses
# 5. Run doctests - all must succeed

# Polish
# 1. Zapisz dane relacyjne do formatu CSV
# 2. Przekonwertuj `DATA` do `result: list[dict[str,str]]`
# 3. Wymagania niefunkcjonalne:
#    - Użyj `,` do oddzielenia pól
#    - Użyj `;` do oddzielenia instancji
# 4. Kontakt ma zero lub wiele adresów
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...