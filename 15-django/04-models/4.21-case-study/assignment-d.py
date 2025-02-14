"""
Name: Django Models Address
Difficulty: medium
Lines: 9
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _

Order: type

# English
# 0. Use `myproject.shop`
# 1. Create model `Order` with fields:
#    - `customer` - relation to `Customer` (one)
#    - `products` - relation to `Product` (many)
# 2. Non-functional requirements:
#    - Use project `myproject` and `shop` app
#    - Each field must have: `verbose_name`, `null`, `blank`, `default`
#    - Add `__str__` method to model
#    - Define `Meta` class with: `app_label`, `verbose_name`, `verbose_name_plural`
#    - Set strategy `on_delete=models.CASCADE` for field `customer`
#    - Use `django.utils.translation.gettext_lazy`
#    - Make migrations and migrate database
#    - Run doctests - all must pass

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz model `Order`:
#    - `customer` - relacja do `Customer` (jeden)
#    - `products` - relacja do `Product` (wiele)
# 2. Wymagania niefunkcjonalne:
#    - Użyj projektu `myproject` i aplikacji `shop`
#    - Każde pole musi mieć: `verbose_name`, `null`, `blank`, `default`
#    - Ustaw strategię `on_delete=models.CASCADE` dla relacji `customer`
#    - Dodaj metodę `__str__` do modelu
#    - Zdefiniuj klasę `Meta` z: `app_label`, `verbose_name`, `verbose_name_plural`
#    - Użyj `django.utils.translation.gettext_lazy`
#    - Wykonaj migracje i zaktualizuj bazę danych
#    - Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Order(models.Model):
    ...