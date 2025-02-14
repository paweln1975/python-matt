"""
Name: Django Ninja Logout
Difficulty: easy
Lines: 8
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()

# English
# 0. Use `myproject.core`
# 1. Create an endpoint `POST /api/v2/auth/login`
# 2. Endpoint should be available only for logged in users
# 3. Endpoint logs-out user
# 4. Endpoint returns `200 OK` and `{"detail": "User logout successful"}`

# Polish
# 0. Użyj `myproject.core`
# 1. Stwórz endpoint `POST /api/v2/auth/login`
# 2. Dostęp do endpointu ma być możliwy tylko dla zalogowanych użytkowników
# 3. Endpoint wylogowuje użytkownika
# 4. Endpoint zwraca `200 OK` i `{"detail": "User logout successful"}`

# %% Result
