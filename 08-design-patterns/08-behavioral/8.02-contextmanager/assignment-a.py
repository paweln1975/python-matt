"""
Name: Protocol ContextManager File
Difficulty: easy
Lines: 14
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from os import remove
>>> from inspect import isclass, ismethod

>>> assert isclass(File)
>>> assert hasattr(File, 'append')
>>> assert hasattr(File, '__enter__')
>>> assert hasattr(File, '__exit__')
>>> assert ismethod(File(None).append)
>>> assert ismethod(File(None).__enter__)
>>> assert ismethod(File(None).__exit__)

>>> with File('_temporary.txt') as file:
...    file.append('One')
...    file.append('Two')

>>> open('_temporary.txt').read()
'One\\nTwo\\n'

>>> remove('_temporary.txt')

Hints:
Append newline character (`\n`) before adding to buffer

"""

# %% SetUp

from typing import Callable, Any
File: type
__init__: Callable[[object, str], None]
__enter__: Callable[[object], object]
__exit__: Callable[[object, Any, Any, Any], None]

# English
# 1. Define class `File` with parameter: `filename: str`
# 2. `File` must implement Context Manager protocol
# 3. `File` buffers lines added using `File.append(text: str)` method
# 4. On `with` block exit, `File` class:
#    - Creates file (if not exists)
#    - Opens file
#    - Writes buffer to file
#    - Clears buffer
#    - Closes file
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `File` z parametrem: `filename: str`
# 2. `File` ma implementować protokół Context Manager
# 3. `File` buforuje linie dodawane za pomocą metody `File.append(text: str)`
# 4. Na wyjściu z bloku `with`, klasa `File`:
#    - Tworzy plik (jeżeli nie istnieje)
#    - Otwiera plik
#    - Zapisuje bufor do pliku
#    - Czyści bufor
#    - Zamyka plik
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class File:
    ...