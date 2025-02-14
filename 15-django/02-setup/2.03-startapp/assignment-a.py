"""
Name: Django Setup StartApp
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

"""

# %% SetUp

# English
# 0. Use `myproject`
# 1. Create app `demo`
# 2. Modify file `myproject/demo/apps.py`:
#    - add `from django.utils.translation import gettext_lazy as _`
#    - add `verbose_name = _('Demo')` in class `DemoConfig`
# 2. Add app to `INSTALLED_APPS` in `myproject/settings.py`
# 3. Run doctests - all must succeed

# Polish
# 0. Użyj `myproject`
# 1. Stwórz aplikację `demo`
# 2. Zmodyfikuj plik `myproject/demo/apps.py`:
#    - dodaj `from django.utils.translation import gettext_lazy as _`
#    - dodaj `verbose_name = _('Demo')` w klasie `DemoConfig`
# 2. Dodaj aplikację do `INSTALLED_APPS` w `myproject/settings.py`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
