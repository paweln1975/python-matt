"""
Name: Django API List
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
from http import HTTPStatus
from django.views import View
from django.http import JsonResponse
from shop.models import Product

# English
# 0. Use `myproject.shop`
# 1. Create an endpoint `GET /api/v1/shop/products`
# 2. Endpoint should list all products in a database
# 3. You can use view based on class or function
# 4. Restrict, that only GET method is handled
# 5. Do not use `ninja`

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz endpoint `GET /api/v1/shop/products`
# 2. Endpoint ma wylistować wszystkie produkty w bazie danych
# 3. Możesz użyć widoku bazującego na klasach lub na funkcjach
# 4. Ogranicz, aby tylko metoda GET była obsługiwana
# 5. Nie używaj `ninja`

# %% Result
