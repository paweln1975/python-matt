"""
* Assignment: Model Data AddresBook
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. In `DATA` we have two classes
    2. Model data using classes and relations
    3. Create instances dynamically based on `DATA`
    4. Non-functional requirements:
        a. Use SQLAlchemy ORM to create models
        b. Do not convert data, just model it
        c. You can use any Python standard library module
        d. You can use SQLAlchemy and Alembic
        e. Do not install or use 3rd party modules
    5. Run doctests - all must succeed

Polish:
    1. W `DATA` mamy dwie klasy
    2. Zamodeluj problem wykorzystując klasy i relacje między nimi
    3. Twórz instancje dynamicznie na podstawie `DATA`
    4. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Nie konwertuj danych, tylko je zamodeluj
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list

    >>> assert all(type(user) is Astronaut
    ...            for user in result)

    >>> assert all(type(addr) is Address
    ...            for user in result
    ...            for addr in user.addresses)

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [Astronaut(firstname='José',
               lastname='Jiménez',
               addresses=[Address(street='2101 E NASA Pkwy', city='Houston', postcode=77058, region='Texas', country='USA'),
                          Address(street=None, city='Kennedy Space Center', postcode=32899, region='Florida', country='USA')]),
     Astronaut(firstname='Mark',
               lastname='Watney',
               addresses=[Address(street='4800 Oak Grove Dr', city='Pasadena', postcode=91109, region='California', country='USA'),
                          Address(street='2825 E Ave P', city='Palmdale', postcode=93550, region='California', country='USA')]),
     Astronaut(firstname='Иван',
               lastname='Иванович',
               addresses=[Address(street=None, city='Космодро́м Байкону́р', postcode=None, region='Кызылординская область', country='Қазақстан'),
                          Address(street=None, city='Звёздный городо́к', postcode=141160, region='Московская область', country='Россия')]),
     Astronaut(firstname='Melissa',
               lastname='Lewis',
               addresses=[]),
     Astronaut(firstname='Alex',
               lastname='Vogel',
               addresses=[Address(street='Linder Hoehe', city='Cologne', postcode=51147, region='North Rhine-Westphalia', country='Germany')])]
"""

from dataclasses import dataclass


DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "postcode": 77058, "region": "Texas", "country": "USA"},
        {"street": None, "city": "Kennedy Space Center", "postcode": 32899, "region": "Florida", "country": "USA"}]},
    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "postcode": 91109, "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "postcode": 93550, "region": "California", "country": "USA"}]},
    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": None, "city": "Космодро́м Байкону́р", "postcode": None, "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": None, "city": "Звёздный городо́к", "postcode": 141160, "region": "Московская область", "country": "Россия"}]},
    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},
    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "postcode": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
]

class Astronaut:
    ...

class Address:
    ...


# Iterate over `DATA` and create instances
# type: list[Astronaut]
result = ...


