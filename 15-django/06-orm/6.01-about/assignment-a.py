"""
Name: Database ORM Import
Difficulty: easy
Lines: 2
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

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from shop.models import Product

Product.objects.all().delete()

PRODUCTS = [
    {"barcode": "5039271113244", "name": "Alfa", "price": "123.00"},
    {"barcode": "5202038482222", "name": "Bravo", "price": "312.22"},
    {"barcode": "5308443764554", "name": "Charlie", "price": "812.00"},
    {"barcode": "5439667086587", "name": "Delta", "price": "332.18"},
    {"barcode": "5527865721147", "name": "Echo", "price": "114.00"},
    {"barcode": "5535686226512", "name": "Foxtrot", "price": "99.12"},
    {"barcode": "5721668602638", "name": "Golf", "price": "123.00"},
    {"barcode": "5776136485596", "name": "Hotel", "price": "444.40"},
    {"barcode": "5863969679442", "name": "India", "price": "674.21"},
    {"barcode": "5908105406923", "name": "Juliet", "price": "324.00"},
    {"barcode": "5957751061635", "name": "Kilo", "price": "932.20"},
    {"barcode": "6190780033092", "name": "Lima", "price": "128.00"},
    {"barcode": "6512625994397", "name": "Mike", "price": "91.00"},
    {"barcode": "6518235371269", "name": "November", "price": "12.00"},
    {"barcode": "6565923118590", "name": "Oscar", "price": "43.10"},
    {"barcode": "6650630136545", "name": "Papa", "price": "112.00"},
    {"barcode": "6692669560199", "name": "Quebec", "price": "997.10"},
    {"barcode": "6711341590108", "name": "Romeo", "price": "1337.00"},
    {"barcode": "6816011714454", "name": "Sierra", "price": "998.10"},
    {"barcode": "7050114819954", "name": "Tango", "price": "123.00"},
    {"barcode": "7251625012784", "name": "Uniform", "price": "564.99"},
    {"barcode": "7251925199277", "name": "Victor", "price": "990.50"},
    {"barcode": "7283004100423", "name": "Whisky", "price": "881.89"},
    {"barcode": "7309682004683", "name": "X-Ray", "price": "123.63"},
    {"barcode": "7324670042560", "name": "Zulu", "price": "311.00"}
]

# English
# 0. Use `myproject.shop`
# 1. Import data from `PRODUCTS`
# 2. Non-functional requirements:
#    - You may use any Python standard library module
#    - You can use Django with migrations
#    - Do not install any additional packages

# Polish
# 0. Użyj `myproject.shop`
# 1. Zaimportuj dane z `PRODUCTS`
# 2. Wymagania niefunkcjonalne:
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć Django
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result
