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
class Language(Enum):
    POLISH = 'pl'
    ENGLISH = 'en'
    SPANISH = 'es'

class Translation:
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def hello(self) -> str:
        if self.language is Language.POLISH:
            return 'Cześć'
        elif self.language is Language.ENGLISH:
            return 'Hello'
        elif self.language is Language.SPANISH:
            return 'Buenos Días'
        else:
            return 'Unknown language'

    def goodbye(self) -> str:
        if self.language is Language.POLISH:
            return 'Do widzenia'
        elif self.language is Language.ENGLISH:
            return 'Goodbye'
        elif self.language is Language.SPANISH:
            return 'Adiós'
        else:
            return 'Unknown language'