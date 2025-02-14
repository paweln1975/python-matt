"""
Name: Django Settings SECURITY_KEY
Difficulty: easy
Lines: 7
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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

Hints:
`os.getenv(..., default=...)` - get the environment variable
`bool(...)` - convert to boolean
default value is `False`

"""

# %% SetUp

# English
# 0. Use `myproject.shop`
# 1. Modify the file: `myproject/settings.py`
# 2. Set `SECRET_KEY` as a content from file `../secret-key.txt`
# 3. If file not exist, or it is empty, rase `ImproperlyConfigured` exception
# 4. Run doctests - all must succeed

# Polish
# 0. Użyj `myproject.shop`
# 1. Zmodyfikuj plik: `myproject/settings.py`
# 2. Ustaw `SECRET_KEY` jako zawartość pliku `../secret-key.txt`
# 3. Jeżeli plik nie istnieje lub jest pusty, podnieś wyjątek `ImproperlyConfigured`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
