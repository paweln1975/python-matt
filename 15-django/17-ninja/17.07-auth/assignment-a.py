"""
Name: Django Ninja Login
Difficulty: medium
Lines: 24
Minutes: 21

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

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()

# English
# 0. Use `myproject.shop`
# 1. Create an endpoint `GET /api/v2/auth/login`
# 2. Endpoint takes `username` and `password`
# 3. If `username` and `password` are invalid, then display error
# 4. If `username` and `password` are valid, then login user
# 5. If user is logged in, then return `request.session.session_key`

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz endpoint `GET /api/v2/auth/login`
# 2. Endpoint przyjmuje `username` i `password`
# 3. Jeżeli `username` i `password` są niepoprawne, to wyświetl błąd
# 4. Jeżeli `username` i `password` są poprawne, to zaloguj użytkownika
# 5. Jeżeli użytkownik jest zalogowany, to zwróć `request.session.session_key`

# %% Result
