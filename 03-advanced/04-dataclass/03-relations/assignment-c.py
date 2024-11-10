"""
* Assignment: Dataclass Relations Addressbook
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Model `DATA` using `dataclasses`
    2. Create class definition, fields and their types
    3. Do not write code converting `DATA` to your classes
    4. Run doctests - all must succeed

Polish:
    1. Zamodeluj `DATA` wykorzystując `dataclass`
    2. Stwórz definicję klas, pól i ich typów
    3. Nie pisz kodu konwertującego `DATA` do Twoich klas
    4. Uruchom doctesty - wszystkie muszą się powieść

Non-functional Requirements:
   * Use optionals syntax, ie: `str | None`

Tests:
    >>> import sys; sys.tracebacklimit = 0
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

from dataclasses import dataclass


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


# Model `DATA` using `dataclass`
# type: type
@dataclass
class Address:
    ...


# Model `DATA` using `dataclass`
# type: type
@dataclass
class User:
    ...


