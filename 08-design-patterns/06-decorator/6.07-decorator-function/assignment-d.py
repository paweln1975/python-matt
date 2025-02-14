"""
Name: Decorator Function Abspath
Difficulty: easy
Lines: 5
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(abspath), \
'Create abspath() function'

>>> assert isfunction(abspath(lambda: ...)), \
'abspath() should take function as an argument'

>>> @abspath
... def display(path):
...     return str(path)

>>> current_dir = str(Path().cwd())
>>> display('iris.csv').startswith(current_dir)
True
>>> display('iris.csv').endswith('iris.csv')
True
>>> display('/home/python/iris.csv')
'/home/python/iris.csv'

Hints:
`Path(filename).absolute()`

"""

# %% SetUp

from pathlib import Path

from typing import Callable
abspath: Callable[[Callable], Callable]

# English
# 1. Absolute path is when `path` starts with `current_directory`
# 2. Create function decorator `abspath`
# 3. If `path` is relative, then `abspath` will convert it to absolute
# 4. If `path` is absolute, then `abspath` will not modify it
# 5. Note: if you are using Windows operating system,
#    then one doctest (with absolute path) can fail
# 6. Run doctests - all must succeed

# Polish
# 1. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
# 2. Stwórz funkcję dekorator `abspath`
# 3. Jeżeli `path` jest względne, to `abspath` zamieni ją na bezwzględną
# 4. Jeżeli `path` jest bezwzględna, to `abspath` nie będzie jej modyfikował
# 5. Uwaga: jeżeli korzystasz z systemu operacyjnego Windows,
#    to jeden z doctestów (ścieżki bezwzględnej) może nie przejść pomyślnie
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
