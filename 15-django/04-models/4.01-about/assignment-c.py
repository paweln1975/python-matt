"""
Name: Django Model About
Difficulty: easy
Lines: 5
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

Hints:
`class Meta`

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _

Group: type

# English
# 0. Use `myproject.demo`
# 1. Alter model `Group`
# 2. Add class `Meta` with:
#    - app_label = 'demo'
#    - verbose_name = _('Group')
#    - verbose_name_plural = _('Groups')
#    - ordering = ['name']
# 3. Use `gettext_lazy`
# 4. Run `makemigrations`
# 5. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Zmień model `Group`
# 2. Dodaj klasę `Meta` z:
#    - app_label = 'demo'
#    - verbose_name = _('Group')
#    - verbose_name_plural = _('Groups')
#    - ordering = ['name']
# 3. Użyj `gettext_lazy`
# 4. Uruchom `makemigrations`
# 5. Uruchom `migrate`

# - `Create model Person`
# - `Applying demo.0003_create_person... OK`

# %% Result
class Group(models.Model):
    name = models.CharField(verbose_name=_('Group'), max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'