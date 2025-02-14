"""
Name: OOP MethodClassmethod CSVMixin
Difficulty: medium
Lines: 4
Minutes: 5

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
Terminal: `python -m doctest -v assignment-i.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from os import remove

>>> mark = User('Mark', 'Watney')
>>> melissa = Admin('Melissa', 'Lewis')

>>> mark.to_csv()
'Mark,Watney\\n'
>>> melissa.to_csv()
'Melissa,Lewis\\n'

>>> with open('_temporary.txt', mode='wt') as file:
...     data = mark.to_csv() + melissa.to_csv()
...     file.writelines(data)

>>> result = []
>>> with open('_temporary.txt', mode='rt') as file:
...     lines = file.readlines()
...     result += [User.from_csv(lines[0])]
...     result += [Admin.from_csv(lines[1])]

>>> result  # doctest: +NORMALIZE_WHITESPACE
[User(firstname='Mark', lastname='Watney'),
 Admin(firstname='Melissa', lastname='Lewis')]

>>> remove('_temporary.txt')

Hints:
`CSVMixin.to_csv()` should add newline `\n` at the end of line
`CSVMixin.from_csv()` should remove newline `\n` at the end of line

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
CSVMixin: type
to_csv: Callable[[object], str]
from_csv: Callable[[type, str], object]

# English
# 1. Modify class `CSVMixin`
# 2. Define classmethod `.to_csv()`
#    - parameter: none
#    - returns: str with class attributes values separated with coma
#    - add newline `\n` at the end of line (this is POSIX standard)
# 3. Define classmethod `.from_csv()`
#    - parameter: `line: str`, example: 'Mark,Watney\n'
#    - returns: instance of a class on which it was called
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `CSVMixin`
# 2. Zdefiniuj classmethod `.to_csv()`
#    - parametr: brak
#    - zwraca: str z wartościami atrybutów klasy oddzielonymi przecinkiem
#    - dodaj znak nowej linii `\n` na końcu linii (jest to standard POSIX)
# 3. Zdefiniuj classmethod `.from_csv()`
#    - parametr: `line: str`, przykład: 'Mark,Watney\n'
#    - zwraca: instancję klasy na której została wykonana
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class CSVMixin:
    def to_csv(self) -> str:
        ...

    @classmethod
    def from_csv(cls, line: str):
        ...

@dataclass
class User(CSVMixin):
    firstname: str
    lastname: str

@dataclass
class Admin(CSVMixin):
    firstname: str
    lastname: str