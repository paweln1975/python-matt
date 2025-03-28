"""
Name: Django Model String
Difficulty: easy
Lines: 1
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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _

Person: type

# English
# 0. Use `myproject.demo`
# 1. Alter model `Person`
# 2. Add field `website` as `models.URLField`:
#    - verbose_name=_('Website')
#    - null=True
#    - blank=True
#    - default=None
# 3. Use `gettext_lazy`
# 4. Run `makemigrations`
# 5. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Zmień model `Person`
# 2. Dodaj pole `website` jako `models.URLField`:
#    - verbose_name=_('Website')
#    - null=True
#    - blank=True
#    - default=None
# 3. Użyj `gettext_lazy`
# 4. Uruchom `makemigrations`
# 5. Uruchom `migrate`

# - `Add field website to person`
# - `Applying demo.0004_person_website... OK`

# %% Result
class Person(models.Model):
    lastname = models.CharField(verbose_name=_('Lastname'), max_length=30, null=False, blank=False, db_index=True)
    firstname = models.CharField(verbose_name=_('Firstname'), max_length=30, null=True, blank=True)
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True, default=None)
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.lastname}, {self.firstname}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        ordering = ['lastname']