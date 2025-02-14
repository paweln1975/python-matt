"""
Name: Django View About
Difficulty: easy
Lines: 3
Minutes: 3

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
# 0. Use `myproject.shop`
# 1. Create class based view `IndexView`
# 2. Create `shop/index.html` template with content: `Hello World!`
# 3. Use `django.views.generic.TemplateView` to render template
# 4. Register view in `urls.py` with name `shop-index-cbv`

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz widok oparty o klasę `IndexView`
# 2. Stwórz szablon `shop/index.html` z treścią: `Hello World!`
# 3. Użyj `django.views.generic.TemplateView` do renderowania szablonu
# 4. Zarejestruj widok w `urls.py` z nazwą `shop-index-cbv`

# %% Result
