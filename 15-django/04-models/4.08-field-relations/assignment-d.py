"""
Name: Django Model Relations
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _

Address: type
Person: type

class Person(models.Model):
    firstname = models.CharField(verbose_name=_('Firstname'), max_length=30, null=True, blank=True, default=None)
    lastname = models.CharField(verbose_name=_('Lastname'), max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        ordering = ['lastname', 'firstname']

# English
# 0. Use `myproject.demo`
# 1. Alter model `Address`
# 2. Add field `person` as `models.ForeignKey`:
#    - verbose_name=_('Person')
#    - on_delete=models.CASCADE
#    - null=True
#    - blank=True
# 3. Use `gettext_lazy`
# 4. Run `makemigrations`
# 5. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Zmień model `Address`
# 2. Dodaj pole `person` jako `models.ForeignKey`:
#    - verbose_name=_('Person')
#    - on_delete=models.CASCADE
#    - null=True
#    - blank=True
# 3. Użyj `gettext_lazy`
# 4. Uruchom `makemigrations`
# 5. Uruchom `migrate`

# - `Add field person to address`
# - `Applying demo.0007_address_person... OK`

# %% Result
class Address(models.Model):
    street = models.CharField(verbose_name=_('Street'), max_length=20, null=True, blank=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=20, null=False, blank=False)
    postcode = models.CharField(verbose_name=_('Postcode'), max_length=20, null=True, blank=True, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=20, null=False, blank=False)

    def __str__(self):
        return f'{self.city}, {self.country}'

    class Meta:
        app_label = 'demo'
        ordering = ['country', 'city']
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')