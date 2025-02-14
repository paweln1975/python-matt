"""
Name: Django Templatetag Simple
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
# 1. Create simple template tag that will display details of `Product`
# 2. Primary Key of product will be passed in `pk` parameter
# 3. Register template tag and use it in `product-detail.html` template

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz prosty templatetag wyświetlający szczegóły `Product`
# 2. Primary Key produktu zostanie przekazany w parametrze `pk`
# 3. Zarejestruj templatetag i użyj go w szablonie `product-detail.html`

# %% Result
