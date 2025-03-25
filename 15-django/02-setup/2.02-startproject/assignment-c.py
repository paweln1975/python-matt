"""
Name: Django Conf Superuser
Difficulty: easy
Lines: 1
Minutes: 2

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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> import sqlite3

>>> from pathlib import Path
>>> DATABASE = Path(__file__).parent.parent.parent.parent / 'django_project' / 'db.sqlite3'
>>> SQL = 'SELECT date_joined FROM auth_user WHERE username="admin"'
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     result = db.execute(SQL).fetchone()
>>>
>>> assert result is not None

"""

# %% SetUp

# English
# 0. Use `myproject`
# 1. Create superuser:
#    - username: `admin`
#    - email: `admin@example.com`
#    - password: `valid`
# 2. Bypass password validation and create user anyway
# 3. Run doctests - all must succeed

# Polish
# 0. Użyj `myproject`
# 1. Stwórz superuser:
#    - username: `admin`
#    - email: `admin@example.com`
#    - password: `valid`
# 2. Omiń walidację hasła i stwórz użytkownika
# 3. Uruchom doctesty - wszystkie muszą się powieść

# - `This password is too short. It must contain at least 8 characters.`
# - `Bypass password validation and create user anyway? [y/N]: y`
# - `Superuser created successfully`

# %% Result
from pathlib import Path
DATABASE = Path(__file__).parent.parent.parent.parent / 'django_project' / 'db.sqlite3'
print(DATABASE)