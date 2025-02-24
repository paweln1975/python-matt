"""
Name: Dataclass Definition Flat
Difficulty: easy
Lines: 6
Minutes: 2

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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass
>>> from dataclasses import is_dataclass
>>> import json

>>> assert isclass(Pet)
>>> assert is_dataclass(Pet)

>>> fields = {'id', 'category', 'name', 'photoUrls', 'tags', 'status'}
>>> assert set(Pet.__dataclass_fields__.keys()) == fields, \
f'Invalid fields, your fields should be: {fields}'

>>> from typing import get_type_hints
>>> annotations = get_type_hints(Pet)
>>>
>>> assert annotations['id'] == int
>>> assert annotations['category'] == str
>>> assert annotations['name'] == str
>>> assert annotations['photoUrls'] == str
>>> assert annotations['tags'] == list[str]
>>> assert annotations['status'] == str

>>> from hashlib import sha1
>>> hex = sha1(DATA.encode()).hexdigest()
>>> assert hex == '678056047aaf56a0435073d4ca43cc493bc9288e' , \
'Do not modify the `DATA` variable'

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
# 3. Run doctests - all must succeed

# Polish
# 1. Otrzymałeś z API dane wejściowe w formacie JSON
# 2. Wykorzystując `dataclass` zamodeluj dane aby stwórzyć klasę `Pet`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Pet:
    id: int
    category: str
    name: str
    photoUrls: str
    tags: list[str]
    status: str
