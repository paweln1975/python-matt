"""
Name: Django Setup Runserver
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

>>> from urllib.request import urlopen
>>> response = urlopen('http://127.0.0.1:8000/')
>>> result = response.read().decode('utf-8')

>>> assert result is not None

Hints:
If port is blocked (you don't have the permission), use port 20_000

"""

# %% SetUp

# English
# 0. Use `myproject`
# 1. Run server:
#    - ip: 127.0.0.1
#    - port: 8000
# 2. Expected result: "Starting development server at http://localhost:8000/"
# 3. Open browser and goto http://127.0.0.1:8000/
# 4. Run doctests - all must succeed

# Polish
# 0. Użyj `myproject`
# 1. Uruchom serwer:
#    - ip: 127.0.0.1
#    - port: 8000
# 2. Oczekiwany rezultat: "Starting development server at http://localhost:8000/"
# 3. Otwórz przeglądarkę i przejdź na stronę http://127.0.0.1:8000/
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
