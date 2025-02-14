"""
Name: Django View FBV
Difficulty: easy
Lines: 6
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
# 1. Create function based view `product_details()`
# 2. View must return HTML with details of the product
# 3. Primary Key of the product will be passed in `pk` parameter
# 4. Use `django.shortcuts.render` to render template
# 5. Create `shop/product-detail.html` template
# 6. Register view in `urls.py` with name `shop-product-details-fbv`

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz widok oparty o funkcję `product_details()`
# 2. Widok ma zwrócić HTML z detalami produktu
# 3. Primary Key produktu zostanie przekazany w parametrze `pk`
# 4. Użyj `django.shortcuts.render` do renderowania szablonu
# 5. Stwórz szablon `shop/product-detail.html`
# 6. Zarejestruj widok w `urls.py` z nazwą `shop-product-details-fbv`

# %% Result
