"""
Name: OOP ObjectRelations Model
Difficulty: easy
Lines: 16
Minutes: 8

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
>>> from pprint import pprint

>>> result = list(result)
>>> assert type(result) is list
>>> assert all(type(user) is User for user in result)

>>> assert all(type(addr) is Address
...            for user in result
...            for addr in user.addresses)

>>> pprint(result, sort_dicts=False)
[User(firstname='Mark',
      lastname='Watney',
      addresses=[Address(street='2101 E NASA Pkwy',
                         city='Houston',
                         postcode=77058,
                         region='Texas',
                         country='USA'),
                 Address(street='',
                         city='Kennedy Space Center',
                         postcode=32899,
                         region='Florida',
                         country='USA')]),
 User(firstname='Melissa',
      lastname='Lewis',
      addresses=[Address(street='4800 Oak Grove Dr',
                         city='Pasadena',
                         postcode=91109,
                         region='California',
                         country='USA'),
                 Address(street='2825 E Ave P',
                         city='Palmdale',
                         postcode=93550,
                         region='California',
                         country='USA')]),
 User(firstname='Rick', lastname='Martinez', addresses=[]),
 User(firstname='Alex',
      lastname='Vogel',
      addresses=[Address(street='Linder Hoehe',
                         city='Cologne',
                         postcode=51147,
                         region='North Rhine-Westphalia',
                         country='Germany')])]

"""

# %% SetUp

from dataclasses import dataclass

result: list[object]

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
# 1. In `DATA` we have two classes
# 2. Model data using classes and relations
# 3. Create instances dynamically based on `DATA`
# 4. Run doctests - all must succeed

# Polish
# 1. W `DATA` mamy dwie klasy
# 2. Zamodeluj problem wykorzystując klasy i relacje między nimi
# 3. Twórz instancje dynamicznie na podstawie `DATA`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Address:
    ...

@dataclass
class User:
    ...

result = ...