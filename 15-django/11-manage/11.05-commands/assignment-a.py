"""
Name: Django Utils ManagementCommand
Difficulty: medium
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

"""

# %% SetUp

# English
# 0. Use `myproject.shop`
# 1. Create management command `shop/management/commands/i18n.py`
# 2. Program should scan all directories that have `locale` directory
# 3. In each such directory run command `python manage.py makemessages -l pl`
# 4. At the end run command `python manage.py compilemessages`

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz komendę zarządzania `shop/management/commands/i18n.py`
# 2. Program powinien przeskanować wszystkie katalogi, które posiadają katalog `locale`
# 3. W każdym takim katalogu uruchom polecenie `python manage.py makemessages -l pl`
# 4. Na końcu uruchom polecenie `python manage.py compilemessages`

# %% Result
