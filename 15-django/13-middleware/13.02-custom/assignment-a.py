"""
Name: Django Middleware Logger
Difficulty: easy
Lines: 15
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

Hints:
`Middleware.__init__(self, get_response)`
`Middleware.__call__(self, request)`
`time.time()`
`duration = stop - start`

"""

# %% SetUp

# English
# 0. Use `myproject.myproject`
# 1. Create a file `myproject/middleware.py`
# 2. Create middleware `Debug`, which:
#    - log to console all HTTP requests
#    - log to console all HTTP responses
#    - log to console processing time from request to response
# 3. Add middleware to `settings.MIDDLEWARE`

# Polish
# 0. Użyj `myproject.myproject`
# 1. Stwórz plik `myproject/middleware.py`
# 2. Stwórz middleware `Debug`, który:
#    - loguje na konsoli wszystkie requesty HTTP
#    - loguje na konsoli wszystkie response'y HTTP
#    - loguje na konsoli czas przetwarzania od requestu do response'a
# 3. Dodaj middleware do `settings.MIDDLEWARE`

# %% Result
