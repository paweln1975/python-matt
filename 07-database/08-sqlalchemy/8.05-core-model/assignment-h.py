"""
Name: Model Data AddresBook
Difficulty: easy
Lines: 10
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
Terminal: `python -m doctest -v assignment-h.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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

# %% SetUp

from dataclasses import dataclass

Astronaut: type
Address: type
result: list[object]

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

# English
# 1. In `DATA` we have two classes
# 2. Model data using classes and relations
# 3. Create instances dynamically based on `DATA`
# 4. Non-functional requirements:
#    - Use SQLAlchemy ORM to create models
#    - Do not convert data, just model it
#    - You can use any Python standard library module
#    - You can use SQLAlchemy and Alembic
#    - Do not install or use 3rd party modules
# 5. Run doctests - all must succeed

# Polish
# 1. W `DATA` mamy dwie klasy
# 2. Zamodeluj problem wykorzystując klasy i relacje między nimi
# 3. Twórz instancje dynamicznie na podstawie `DATA`
# 4. Wymagania niefunkcjonalne:
#    - Użyj SQLAlchemy ORM do stworzenia modeli
#    - Nie konwertuj danych, tylko je zamodeluj
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Astronaut:
    ...

class Address:
    ...

result = ...