"""
Name: Django Models Customer
Difficulty: medium
Lines: 20
Minutes: 11

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
`django.db.models.CharField`
`django.db.models.DateField`
`django.db.models.ImageField`
`django.db.models.EmailField`
`django.db.models.BooleanField`
`django.db.models.TextChoices`
`django.core.validators.MinLengthValidator`

"""

# %% SetUp

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

Gender: type
Customer: type

# English
# 0. Use `myproject.shop`
# 1. Create model `Customer`:
#    - `firstname` - first name (minimum 2 characters)
#    - `lastname` - last name (minimum 2 characters)
#    - `birthdate` - date of birth
#    - `gender` - gender (choice: male, female, other)
#    - `tax_number` - Tax Identification Number (with help text)
#    - `email` - email address (unique, database index)
#    - `phone` - phone including country code (with help text)
#    - `image` - Profile picture (upload to: images/)
#    - `is_verified` - if profile is verified (true, false, default: false)
# 2. Non-functional requirements:
#    - Install `Pillow` package: `python -m pip install --upgrade pillow`
#    - Use project `myproject` and `shop` app
#    - Each field must have: `verbose_name`, `null`, `blank`, `default`
#    - Add `__str__` method to model
#    - Define `Meta` class with: `app_label`, `verbose_name`, `verbose_name_plural`
#    - Use `django.utils.translation.gettext_lazy`
#    - Make migrations and migrate database
#    - Run doctests - all must pass

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz model `Customer` z polami:
#    - `firstname` - imię (minimum 2 znaki)
#    - `lastname` - nazwisko (minimum 2 znaki)
#    - `birthdate` - data urodzenia
#    - `gender` - płeć (wybór: male, female, other)
#    - `tax_number` - Numer Identyfikacji Podatkowej (NIP) (z tekstem pomocy)
#    - `email` - adres email (unikalny, indeks bazy danych)
#    - `phone` - telefon z numerem kierunkowym kraju (z tekstem pomocy)
#    - `image` - Profile picture (upload to: images/)
#    - `is_verified` - czy profil jest sprawdzony (true, false, default: false)
# 2. Wymagania niefunkcjonalne:
#    - Zainstaluj pakiet `Pillow`: `python -m pip install --upgrade pillow`
#    - Użyj projektu `myproject` i aplikacji `shop`
#    - Każde pole musi mieć: `verbose_name`, `null`, `blank`, `default`
#    - Dodaj metodę `__str__` do modelu
#    - Zdefiniuj klasę `Meta` z: `app_label`, `verbose_name`, `verbose_name_plural`
#    - Użyj `django.utils.translation.gettext_lazy`
#    - Wykonaj migracje i zaktualizuj bazę danych
#    - Uruchom doctesty - wszystkie muszą się powieść

# %% Result
