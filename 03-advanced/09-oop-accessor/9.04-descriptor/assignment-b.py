"""
Name: Accessor Descriptor ValueRange
Difficulty: medium
Lines: 9
Minutes: 13

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> mark = User('Mark', 'Watney', age=36, height=170, weight=80)

>>> melissa = User('Melissa', 'Lewis', age=66, height=170, weight=80)
Traceback (most recent call last):
ValueError: age is not between 18 and 65

>>> rick = User('Rick', 'Martinez', age=39, height=201, weight=75)
Traceback (most recent call last):
ValueError: height is not between 150 and 200

>>> alex = User('Alex', 'Vogel', age=41, height=175, weight=151)
Traceback (most recent call last):
ValueError: weight is not between 50 and 150

"""

# %% SetUp

from dataclasses import dataclass

ValueRange: type
User: type

# English
# 1. Define descriptor class `ValueRange` with attributes:
#    - `name: str`
#    - `min: float`
#    - `max: float`
# 2. Define class `User` with attributes:
#    - `firstname: str`
#    - `lastname: str`
#    - `age: int` range from 18 to 65
#    - `height: float` range from 150 to 200
#    - `weight: float` range from 50 to 150
# 3. Setting `User` attribute should invoke boundary check
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę-deskryptor `ValueRange` z atrybutami:
#    - `name: str`
#    - `min: float`
#    - `max: float`
# 2. Zdefiniuj klasę `User` z atrybutami:
#    - `firstname: str`
#    - `lastname: str`
#    - `age: int` zakres od 18 do 65
#    - `height: float` zakres od 150 do 200
#    - `weight: float` zakres od 50 do 150
# 3. Ustawianie atrybutu `User` powinno wywołać sprawdzanie zakresu
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class ValueRange:
    name: str
    min: float
    max: float

@dataclass
class User:
    firstname: str
    lastname: str
    age: int
    height: float
    weight: float