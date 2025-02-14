"""
Name: Model Data PetstoreFlat
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
>>> from inspect import isclass
>>> from dataclasses import is_dataclass
>>> import json

>>> assert isclass(Pet)
>>> assert is_dataclass(Pet)

>>> fields = {'id', 'category', 'name', 'photoUrls', 'tags', 'status'}
>>> assert set(Pet.__dataclass_fields__.keys()) == fields, \
f'Invalid fields, your fields should be: {fields}'

>>> data = json.loads(DATA)
>>> result = Pet(**data)

>>> result  # doctest: +NORMALIZE_WHITESPACE
Pet(id=0, category='dogs', name='doggie', photoUrls='img/dogs/0.png',
    tags=['dog', 'hot-dog'], status='available')

"""

# %% SetUp

from dataclasses import dataclass

Pet: type

DATA = """
{
  "id": 0,
  "category": "dogs",
  "name": "doggie",
  "photoUrls": "img/dogs/0.png",
  "tags": ["dog", "hot-dog"],
  "status": "available"
}
"""

# English
# 1. You received input data in JSON format from the API
# 2. Using `dataclass` model data to create class `Pet`
# 3. Non-functional requirements:
#    - Use SQLAlchemy ORM to create models
#    - Do not convert data, just model it
#    - You can use any Python standard library module
#    - You can use SQLAlchemy and Alembic
#    - Do not install or use 3rd party modules
# 4. Run doctests - all must succeed

# Polish
# 1. Otrzymałeś z API dane wejściowe w formacie JSON
# 2. Wykorzystując `dataclass` zamodeluj dane aby stwórzyć klasę `Pet`
# 3. Wymagania niefunkcjonalne:
#    - Użyj SQLAlchemy ORM do stworzenia modeli
#    - Nie konwertuj danych, tylko je zamodeluj
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Pet:
    ...