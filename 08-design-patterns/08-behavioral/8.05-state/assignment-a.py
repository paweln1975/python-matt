"""
Name: DesignPatterns Behavioral State
Difficulty: medium
Lines: 34
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> polish = Translation(Polish())
>>> english = Translation(English())
>>> chinese = Translation(Chinese())

>>> polish.hello()
'Cześć'
>>> polish.goodbye()
'Do widzenia'

>>> english.hello()
'Hello'
>>> english.goodbye()
'Goodbye'

>>> chinese.hello()
'你好'
>>> chinese.goodbye()
'再见'

"""
from abc import abstractmethod, ABC
# %% SetUp

from enum import Enum

# English
# 1. Implement State pattern
# 2. Then add another language:
#    - Chinese hello: 你好
#    - Chinese goodbye: 再见
# 3. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj wzorzec State
# 2. Następnie dodaj nowy język:
#    - Chinese hello: 你好
#    - Chinese goodbye: 再见
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
# class Language(Enum):
#     POLISH = 'pl'
#     ENGLISH = 'en'
#     SPANISH = 'es'

class Language(ABC):
    @abstractmethod
    def hello(self) -> str:
        pass

    @abstractmethod
    def goodbye(self) -> str:
        pass

class Polish(Language):
    def hello(self) -> str:
        return 'Cześć'

    def goodbye(self) -> str:
        return 'Do widzenia'

class English(Language):
    def hello(self) -> str:
        return 'Hello'

    def goodbye(self) -> str:
        return 'Goodbye'

class Chinese(Language):
    def hello(self) -> str:
        return '你好'

    def goodbye(self) -> str:
        return '再见'

class Spanish(Language):
    def hello(self) -> str:
        return 'Buenos Días'

    def goodbye(self) -> str:
        return 'Adiós'


class Translation:
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def hello(self) -> str:
        if self.language is None:
            return 'Unknown language'
        else:
            return self.language.hello()

    def goodbye(self) -> str:
        if self.language is None:
            return 'Unknown language'
        else:
            return self.language.goodbye()