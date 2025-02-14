"""
Name: Decorator Class Abspath
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(Abspath), \
'Abspath should be a decorator class'

>>> assert Abspath(lambda: ...), \
'Abspath should take function as an argument'

>>> assert isinstance(Abspath(lambda: ...), Abspath), \
'Abspath() should return an object which is an instance of Abspath'

>>> @Abspath
... def display(path):
...     return str(path)

>>> current_dir = str(Path().cwd())
>>> display('iris.csv').startswith(current_dir)
True
>>> display('iris.csv').endswith('iris.csv')
True
>>> display('/home/python/iris.csv')  # Should pass regardless your OS
'/home/python/iris.csv'

Hints:
`path = Path(path).absolute()`

"""

# %% SetUp

from pathlib import Path

Abspath: type

def abspath(func):
    def wrapper(filepath):
        abspath = Path(filepath).absolute()
        return func(abspath)
    return wrapper

# English
# 1. Absolute path is when `path` starts with `current_directory`
# 2. Create class decorator `Abspath`
# 3. If `path` is relative, then `Abspath` will convert it to absolute
# 4. If `path` is absolute, then `Abspath` will not modify it
# 5. Note: if you are using Windows operating system,
#    then one doctest (with absolute path) can fail
# 6. Run doctests - all must succeed

# Polish
# 1. Ścieżka bezwzględna jest gdy `path` zaczyna się od `current_directory`
# 2. Stwórz klasę dekorator `Abspath`
# 3. Jeżeli `path` jest względne, to `Abspath` zamieni ją na bezwzględną
# 4. Jeżeli `path` jest bezwzględna, to `Abspath` nie będzie jej modyfikował
# 5. Uwaga: jeżeli korzystasz z systemu operacyjnego Windows,
#    to jeden z doctestów (ścieżki bezwzględnej) może nie przejść pomyślnie
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
