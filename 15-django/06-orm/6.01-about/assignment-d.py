"""
Name: Database ORM Import
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from shop.models import Order, Customer, Product

Order.objects.all().delete()

ORDERS = [
    {"customer": "mwatney@nasa.gov", "product": "Sierra"},
    {"customer": "mwatney@nasa.gov", "product": "Victor"},
    {"customer": "bjohanssen@nasa.gov", "product": "Delta"},
    {"customer": "mlewis@nasa.gov", "product": "November"},
    {"customer": "rmartinez@nasa.gov", "product": "Mike"},
    {"customer": "mwatney@nasa.gov", "product": "Bravo"},
    {"customer": "mwatney@nasa.gov", "product": "Kilo"},
    {"customer": "avogel@esa.int", "product": "Victor"},
    {"customer": "bjohanssen@nasa.gov", "product": "Romeo"},
    {"customer": "bjohanssen@nasa.gov", "product": "Whisky"},
    {"customer": "cbeck@nasa.gov", "product": "Zulu"},
    {"customer": "mwatney@nasa.gov", "product": "Romeo"},
    {"customer": "avogel@esa.int", "product": "Romeo"},
    {"customer": "bjohanssen@nasa.gov", "product": "Victor"},
    {"customer": "bjohanssen@nasa.gov", "product": "Whisky"},
    {"customer": "mlewis@nasa.gov", "product": "Whisky"},
    {"customer": "rmartinez@nasa.gov", "product": "Mike"},
    {"customer": "mwatney@nasa.gov", "product": "November"},
    {"customer": "mwatney@nasa.gov", "product": "Kilo"},
    {"customer": "avogel@esa.int", "product": "Bravo"},
    {"customer": "bjohanssen@nasa.gov", "product": "X-Ray"},
    {"customer": "avogel@esa.int", "product": "Romeo"},
    {"customer": "bjohanssen@nasa.gov", "product": "Victor"},
    {"customer": "bjohanssen@nasa.gov", "product": "India"},
    {"customer": "mlewis@nasa.gov", "product": "Juliet"},
    {"customer": "rmartinez@nasa.gov", "product": "Foxtrot"},
    {"customer": "avogel@esa.int", "product": "Victor"},
    {"customer": "bjohanssen@nasa.gov", "product": "Romeo"},
    {"customer": "bjohanssen@nasa.gov", "product": "Whisky"},
    {"customer": "cbeck@nasa.gov", "product": "Zulu"},
    {"customer": "mwatney@nasa.gov", "product": "Alfa"},
    {"customer": "avogel@esa.int", "product": "Romeo"},
    {"customer": "bjohanssen@nasa.gov", "product": "Quebec"},
]

# English
# 0. Use `myproject.shop`
# 1. Import data from `ORDERS`
# 2. Non-functional requirements:
#    - You may use any Python standard library module
#    - You can use Django with migrations
#    - Do not install any additional packages

# Polish
# 0. Użyj `myproject.shop`
# 1. Zaimportuj dane z `ORDERS`
# 2. Wymagania niefunkcjonalne:
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć Django
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result
