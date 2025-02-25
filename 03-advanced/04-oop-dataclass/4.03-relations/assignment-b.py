"""
Name: Dataclass Relations Syntax
Difficulty: easy
Lines: 6
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isclass
>>> from dataclasses import is_dataclass
>>> import json

>>> assert isclass(Pet)
>>> assert isclass(Category)
>>> assert isclass(Tag)
>>> assert is_dataclass(Pet)
>>> assert is_dataclass(Category)
>>> assert is_dataclass(Tag)

>>> fields = {'id', 'category', 'name', 'photoUrls', 'tags', 'status'}
>>> assert set(Pet.__dataclass_fields__.keys()) == fields, \
f'Invalid fields, your fields should be: {fields}'

>>> data = json.loads(DATA)
>>> result = Pet(**data)
>>> result.category = Category(**result.category)
>>> result.tags = [Tag(**tag) for tag in result.tags]

>>> result  # doctest: +NORMALIZE_WHITESPACE
Pet(id=0, category=Category(id=0, name='dogs'), name='doggie',
    photoUrls=['img/dogs/0.png'], tags=[Tag(id=0, name='dog'),
                                        Tag(id=1, name='hot-dog')],
    status='available')

"""

# %% SetUp

from dataclasses import dataclass

# Category: type
# Tag: type
# Pet: type

DATA = """
{
  "id": 0,
  "category": {
    "id": 0,
    "name": "dogs"
  },
  "name": "doggie",
  "photoUrls": [
    "img/dogs/0.png"
  ],
  "tags": [
    {
      "id": 0,
      "name": "dog"
    },
    {
      "id": 1,
      "name": "hot-dog"
    }
  ],
  "status": "available"
}
"""

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Tag:
    id: int
    name: str

# English
# 1. You received input data in JSON format from the API
# 2. Using `dataclass` model `DATA`:
#    - Create class `Pet`
#    - Create class `Category`
#    - Create class `Tags`
# 3. Model relations between classes
# 4. Run doctests - all must succeed

# Polish
# 1. Otrzymałeś z API dane wejściowe w formacie JSON
# 2. Wykorzystując `dataclass` zamodeluj `DATA`:
#    - Stwórz klasę `Pet`
#    - Stwórz klasę `Category`
#    - Stwórz klasę `Tags`
# 3. Zamodeluj relacje między klasami
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Pet:
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str
