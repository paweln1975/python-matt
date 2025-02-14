"""
Name: Model Data Addressbook
Difficulty: easy
Lines: 12
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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isclass
>>> from dataclasses import is_dataclass

>>> assert isclass(Astronaut)
>>> assert isclass(Address)
>>> assert is_dataclass(Astronaut)
>>> assert is_dataclass(Address)

>>> astronaut = Astronaut.__dataclass_fields__
>>> address = Address.__dataclass_fields__

>>> assert 'firstname' in astronaut, \
'Class Astronaut is missing field: firstname'
>>> assert 'lastname' in astronaut, \
'Class Astronaut is missing field: lastname'
>>> assert 'addresses' in astronaut, \
'Class Astronaut is missing field: addresses'
>>> assert 'street' in address, \
'Class Address is missing field: street'
>>> assert 'city' in address, \
'Class Address is missing field: city'
>>> assert 'post_code' in address, \
'Class Address is missing field: post_code'
>>> assert 'region' in address, \
'Class Address is missing field: region'
>>> assert 'country' in address, \
'Class Address is missing field: country'
>>> assert astronaut['firstname'].type is str, \
'Astronaut.firstname has invalid type annotation, expected: str'
>>> assert astronaut['lastname'].type is str, \
'Astronaut.lastname has invalid type annotation, expected: str'
>>> assert astronaut['addresses'].type.__name__ == 'list', \
'Astronaut.addresses has invalid type annotation, expected: list[Address]'
>>> assert address['street'].type is Optional[str], \
'Address.street has invalid type annotation, expected: Optional[str]'
>>> assert address['city'].type is str, \
'Address.city has invalid type annotation, expected: str'
>>> assert address['post_code'].type is Optional[int], \
'Address.post_code has invalid type annotation, expected: Optional[int]'
>>> assert address['region'].type is str, \
'Address.region has invalid type annotation, expected: str'
>>> assert address['country'].type is str, \
'Address.country has invalid type annotation, expected: str'

"""

# %% SetUp

from typing import Optional
from dataclasses import dataclass, field

Address: type
Astronaut: type

DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058,
         "region": "Texas", "country": "USA"},
        {"street": None, "city": "Kennedy Space Center", "post_code": 32899,
         "region": "Florida", "country": "USA"}]},

    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109,
         "region": "California", "country": "USA"},
        {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550,
         "region": "California", "country": "USA"}]},

    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": None, "city": "Космодро́м Байкону́р", "post_code": None,
         "region": "Кызылординская область", "country": "Қазақстан"},
        {"street": None, "city": "Звёздный городо́к", "post_code": 141160,
         "region": "Московская область", "country": "Россия"}]},

    {"firstname": "Melissa", "lastname": "Lewis"},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "post_code": 51147,
         "region": "North Rhine-Westphalia", "country": "Germany"}]}
]

# English
# 1. Model `DATA` using `dataclasses`
# 2. Create class definition, fields and their types:
#    - Do not use Python 3.10 syntax for Optionals, ie: `str | None`
#    - Use old style `Optional[str]` instead
# 3. Non-functional requirements:
#    - Use SQLAlchemy ORM to create models
#    - Do not convert data, just model it
#    - You can use any Python standard library module
#    - You can use SQLAlchemy and Alembic
#    - Do not install or use 3rd party modules
# 4. Run doctests - all must succeed

# Polish
# 1. Zamodeluj `DATA` wykorzystując `dataclass`
# 2. Stwórz definicję klas, pól i ich typów
#    - Nie używaj składni Optionali z Python 3.10, np.: `str | None`
#    - Użyj starego sposobu, tj. `Optional[str]`
# 3. Wymagania niefunkcjonalne:
#    - Użyj SQLAlchemy ORM do stworzenia modeli
#    - Nie konwertuj danych, tylko je zamodeluj
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Address:
    ...

class Astronaut:
    ...