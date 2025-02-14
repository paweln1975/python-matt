"""
Name: Django Ninja SessionAuth
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
Terminal: `python -m doctest -v assignment-b.py`

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
# 1. Create class `SessionAuth()`
# 2. Class should inherit from `ninja.security.APIKeyHeader`
# 3. Define `param_name = "X-SESSIONID"`
# 4. Define method `authenticate(self, request, sessionid)`
# 5. Method should return `Session` object with given `session_key`
# 6. In case of missing session, or error should return `None`

# Polish
# 0. Użyj `myproject.core`
# 1. Stwórz klasę `SessionAuth()`
# 2. Klasa ma dziedziczyć po `ninja.security.APIKeyHeader`
# 3. Zdefiniuj `param_name = "X-SESSIONID"`
# 4. Zdefiniuj metodę `authenticate(self, request, sessionid)`
# 5. Metoda ma zwracać objekt `Session` o podanym `session_key`
# 6. W przypadku braku sesji, lub błędu ma zwracać `None`

# %% Result
