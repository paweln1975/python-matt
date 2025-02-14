"""
Name: Protocol ContextManager Buffer
Difficulty: medium
Lines: 15
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from os import remove
>>> from inspect import isclass, ismethod

>>> assert isclass(File)
>>> assert hasattr(File, 'append')
>>> assert hasattr(File, 'BUFFER_LIMIT')
>>> assert hasattr(File, '__enter__')
>>> assert hasattr(File, '__exit__')
>>> assert ismethod(File(None).append)
>>> assert ismethod(File(None).__enter__)
>>> assert ismethod(File(None).__exit__)
>>> assert File.BUFFER_LIMIT == 100

>>> with File('_temporary.txt') as file:
...    file.append('One')
...    file.append('Two')
...    file.append('Three')
...    file.append('Four')
...    file.append('Five')
...    file.append('Six')

>>> open('_temporary.txt').read()
'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'

>>> remove('_temporary.txt')

Hints:
`sys.getsizeof(obj)` returns `obj` size in bytes

"""

# %% SetUp

from sys import getsizeof

from typing import Callable, Any
File: type
__init__: Callable[[object, str], None]
__enter__: Callable[[object], object]
__exit__: Callable[[object, Any, Any, Any], None]

# English
# 1. Define class attribute `BUFFER_LIMIT: int = 100` bytes
# 2. File has to be written to disk every X bytes of buffer
# 3. Writing and reading takes time,
#    how to make buffer save data in the background,
#    but it could be still used?
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasowy atrybut `BUFFER_LIMIT: int = 100` bajtów
# 2. Plik na dysku ma być zapisywany co X bajtów bufora
# 3. Operacje zapisu i odczytu trwają, jak zrobić,
#    aby do bufora podczas zapisu na dysk,
#    nadal można było pisać?
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class File:
    ...