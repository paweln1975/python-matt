"""
Name: OOP MethodClassmethod FromDict
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass
>>> from types import NoneType

>>> assert isclass(Animal)
>>> assert isclass(Cat)
>>> assert isclass(Dog)

>>> CAT = {'english_name': 'Cat', 'latin_name': 'Felis catus'}
>>> cat = Cat.from_dict(CAT)
>>> assert type(cat.english_name) is str
>>> assert type(cat.latin_name) is str
>>> assert cat.english_name == 'Cat'
>>> assert cat.latin_name == 'Felis catus'

>>> DOG = {'english_name': 'Dog', 'latin_name': 'Canis familiaris'}
>>> dog = Dog.from_dict(DOG)
>>> assert type(dog.english_name) is str
>>> assert type(dog.latin_name) is str
>>> assert dog.english_name == 'Dog'
>>> assert dog.latin_name == 'Canis familiaris'

>>> PLATYPUS = {'english_name': 'Platypus'}
>>> platypus = Platypus.from_dict(PLATYPUS)
>>> assert type(platypus.english_name) is str
>>> assert type(platypus.latin_name) is NoneType
>>> assert platypus.english_name == 'Platypus'
>>> assert platypus.latin_name is None

Hints:
`dict.get()`

"""

# %% SetUp

from typing import Callable
Animal: type
from_dict: Callable[[type, dict[str,str]], object]

# English
# 1. Modify class `Animal`
# 2. Define classmethod `from_dict()`:
#    - parameter `data: dict[str,str]`, example: {'english_name': 'Cat', 'latin_name': 'Felis catus'}
#    - returns instance of a class on which was called
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Animal`
# 2. Zdefiniuj classmethod `from_dict()`:
#    - parametr `data: dict[str,str]`, przykład: {'english_name': 'Cat', 'latin_name': 'Felis catus'}
#    - zwraca instancję klasy na której została wykonana
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Animal:
    def __init__(self, english_name, latin_name):
        self.english_name = english_name
        self.latin_name = latin_name

    @classmethod
    def from_dict(cls, data: dict):
        ...

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Platypus(Animal):
    pass