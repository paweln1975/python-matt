"""
Name: Django Model Choices
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _

Language: type
Person: type

# English
# 0. Use `myproject.demo`
# 1. Add class `Language` as `models.TextChoices`:
#    - ENGLISH = 'en', _('English')
#    - POLISH = 'pl', _('Polish')
# 2. Alter model `Person`, add field `language` as `models.CharField`:
#    - verbose_name=_('Language')
#    - max_length=2
#    - choices=Language
#    - null=True
#    - blank=True
#    - default=Language.ENGLISH
# 3. Use `gettext_lazy`
# 4. Run `makemigrations`
# 5. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Dodaj klasę `Language` jako `models.TextChoices`:
#    - ENGLISH = 'en', _('English')
#    - POLISH = 'pl', _('Polish')
# 2. Zmień model `Person`, dodaj pole `language` jako `models.CharField`:
#    - verbose_name=_('Language')
#    - max_length=2
#    - choices=Language
#    - null=True
#    - blank=True
#    - default=Language.ENGLISH
# 3. Użyj `gettext_lazy`
# 4. Uruchom `makemigrations`
# 5. Uruchom `migrate`

# - `Add field language to person`
# - `Applying demo.0007_person_language... OK`

# %% Result
class Person(models.Model):
    language = ...