"""
* Assignment: OOP Relations Model
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    1. In `DATA` we have two classes
    2. Model data using classes and relations
    3. Create instances dynamically based on `DATA`
    4. Run doctests - all must succeed

Polish:
    1. W `DATA` mamy dwie klasy
    2. Zamodeluj problem wykorzystując klasy i relacje między nimi
    3. Twórz instancje dynamicznie na podstawie `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result = list(result)
    >>> assert type(result) is list
    >>> assert all(type(user) is User for user in result)

    >>> assert all(type(addr) is Address
    ...            for user in result
    ...            for addr in user.addresses)

    >>> pprint(result, sort_dicts=False)  # doctest: +NORMALIZE_WHITESPACE
    [User('Mark', 'Watney', addresses=[Address('Houston', 'USA'), Address('Kennedy Space Center', 'USA')]),
     User('Melissa', 'Lewis', addresses=[Address('Pasadena', 'USA'), Address('Palmdale', 'USA')]),
     User('Rick', 'Martinez', addresses=[]),
     User('Alex', 'Vogel', addresses=[Address('Cologne', 'Germany')])]
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


# Model `DATA`
# type: type
class Address:
    def __repr__(self):
        return f"Address('...', '...')"


# Model `DATA`
# type: type
class User:
    def __repr__(self):
        return f"User('...', '...', addresses=...)"



# Iterate over `DATA` and create instances
# type: list[User]
result = ...


