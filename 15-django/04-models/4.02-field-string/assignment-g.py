"""
Name: Django Model String
Difficulty: easy
Lines: 2
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
Terminal: `python -m doctest -v assignment-g.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

Person: type

# English
# 0. Use `myproject.demo`
# 1. Alter model `Person`
# 2. Alter field `comment`, add validators:
#    - MinLengthValidator(0)
#    - MaxLengthValidator(20)
# 3. Run `makemigrations`
# 4. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Zmień model `Person`
# 2. Zmień pole `comment`, dodaj walidatory:
#    - MinLengthValidator(0)
#    - MaxLengthValidator(20)
# 3. Uruchom `makemigrations`
# 4. Uruchom `migrate`

# - `Alter field comment on person`
# - `Applying demo.0006_alter_person_comment... OK`

# %% Result
class Person(models.Model):
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None,
                               validators=[MinLengthValidator(0), MaxLengthValidator(20)])