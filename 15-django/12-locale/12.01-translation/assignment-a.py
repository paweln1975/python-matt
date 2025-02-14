"""
Name: Django Locale Translation
Difficulty: easy
Lines: 4
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
`python manage.py makemessages -l en -l pl`
`python manage.py compilemessages`
`python manage.py runserver`

"""

# %% SetUp

# English
# 0. Use `myproject`
# 1. Add locale middleware to `settings.MIDDLEWARE`
# 2. Create a directory `locale` in each app of `myproject`
# 3. Generate language files for English (en) and Polish (pl)
# 4. Translate language files using LLM (i.e., GitHub Copilot)
# 5. Compile language files
# 6. Restart server
# 7. Open your browser at `http://127.0.0.1:8000/admin`
# 8. Change preferred language in your browser: English <-> Polish

# Polish
# 0. Użyj `myproject.shop`
# 1. Dodaj locale middleware do `settings.MIDDLEWARE`
# 2. Stwórz katalog `locale` w każdej apce projektu `myproject`
# 3. Wygeneruj pliki językowe dla angielskiego (en) i polskiego (pl)
# 4. Przetłumacz pliki językowe wykorzystując LLM (np. GitHub Copilot)
# 5. Skompiluj pliki językowe
# 6. Zrestartuj serwer
# 7. Otwórz przeglądarkę na `http://localhost:8000/admin`
# 8. Zmień preferowany język w przeglądarce: angielski <-> polski

# %% Result
