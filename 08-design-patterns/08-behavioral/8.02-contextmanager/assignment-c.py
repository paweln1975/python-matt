"""
Name: Protocol Context Manager AutoSave
Difficulty: hard
Lines: 13
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from os import remove
>>> from inspect import isclass, ismethod
>>> from time import sleep

>>> assert isclass(File)
>>> assert hasattr(File, 'append')
>>> assert hasattr(File, 'AUTOSAVE_SECONDS')
>>> assert hasattr(File, '__enter__')
>>> assert hasattr(File, '__exit__')
>>> assert ismethod(File(None).append)
>>> assert ismethod(File(None).__enter__)
>>> assert ismethod(File(None).__exit__)
>>> assert File.AUTOSAVE_SECONDS == 1.0

>>> with File('_temporary.txt') as file:
...     file.append('One')
...     file.append('Two')
...     sleep(0.5)
...     file.append('Three')
...     file.append('Four')
...     sleep(2.0)
...     file.append('Five')
...     file.append('Six')

>>> open('_temporary.txt').read()
'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'

>>> remove('_temporary.txt')

Hints:
`from threading import Timer`
`timer = Timer(interval, function)`
`timer.start()`
`timer.cancel()`
`ctrl+c` or stop button kills infinite loop

"""

# %% SetUp

from threading import Timer

from typing import Callable, Any
File: type
__init__: Callable[[object, str], None]
__enter__: Callable[[object], object]
__exit__: Callable[[object, Any, Any, Any], None]

# English
# 1. Modify class `File`
# 2. Add class configuration attribute `AUTOSAVE_SECONDS: float = 1.0`
# 3. Save buffer content to file every `AUTOSAVE_SECONDS` seconds
# 4. Writing and reading takes time, how to make buffer save data in the background, but it could be still used?
# 5. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `File`
# 2. Dodaj klasowy atrybut konfiguracyjny `AUTOSAVE_SECONDS: float = 1.0`
# 3. Zapisuj zawartość bufora do pliku co `AUTOSAVE_SECONDS` sekund
# 4. Operacje zapisu i odczytu trwają, jak zrobić, aby do bufora podczas zapisu na dysk, nadal można było pisać?
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class File:
    ...