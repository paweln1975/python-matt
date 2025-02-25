"""
Name: Dataclass Relations Addressbook
Difficulty: easy
Lines: 8
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass
>>> from dataclasses import is_dataclass
>>> from typing import get_type_hints

>>> assert isclass(User)
>>> assert isclass(Address)
>>> assert is_dataclass(User)
>>> assert is_dataclass(Address)

>>> user = get_type_hints(User)
>>> address = get_type_hints(Address)

>>> assert 'firstname' in user, \
'Class User is missing field: firstname'
>>> assert 'lastname' in user, \
'Class User is missing field: lastname'
>>> assert 'addresses' in user, \
'Class User is missing field: addresses'
>>> assert 'street' in address, \
'Class Address is missing field: street'
>>> assert 'city' in address, \
'Class Address is missing field: city'
>>> assert 'postcode' in address, \
'Class Address is missing field: postcode'
>>> assert 'region' in address, \
'Class Address is missing field: region'
>>> assert 'country' in address, \
'Class Address is missing field: country'
>>> assert user['firstname'] is str, \
'User.firstname has invalid type annotation, expected: str'
>>> assert user['lastname'] is str, \
'User.lastname has invalid type annotation, expected: str'
>>> assert user['addresses'] == list[Address], \
'User.addresses has invalid type annotation, expected: list[Address]'
>>> assert address['street'] == str, \
'Address.street has invalid type annotation, expected: str'
>>> assert address['city'] is str, \
'Address.city has invalid type annotation, expected: str'
>>> assert address['postcode'] is int, \
'Address.postcode has invalid type annotation, expected: int'
>>> assert address['region'] is str, \
'Address.region has invalid type annotation, expected: str'
>>> assert address['country'] is str, \
'Address.country has invalid type annotation, expected: str'

"""

# %% SetUp

from dataclasses import dataclass

Address: type
User: type

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
# 1. Model `DATA` using `dataclasses`
# 2. Create class definition, fields and their types
# 3. Do not write code converting `DATA` to your classes
# 4. Run doctests - all must succeed

# Polish
# 1. Zamodeluj `DATA` wykorzystując `dataclass`
# 2. Stwórz definicję klas, pól i ich typów
# 3. Nie pisz kodu konwertującego `DATA` do Twoich klas
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Address:
    street: str
    city: str
    postcode: int
    region: str
    country: str

@dataclass
class User:
    firstname: str
    lastname: str
    addresses: list[Address]
