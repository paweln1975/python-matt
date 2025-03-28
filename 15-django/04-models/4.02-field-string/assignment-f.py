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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify

Person: type

# English
# 0. Use `myproject.demo`
# 1. Alter model `Person`
# 2. Add field `username` as `models.SlugField`:
#    - verbose_name=_('Username')
#    - null=True
#    - blank=True
#    - default=None
# 3. Define method `.save()`, which generates `username`
#    from first letter of a `firstname` and whole `lastname`
#    ie. Mark Watney => mwatney
# 4. Use `gettext_lazy`
# 5. Run `makemigrations`
# 6. Run `migrate`

# Polish
# 0. Użyj `myproject.demo`
# 1. Zmień model `Person`
# 2. Dodaj pole `username` jako `models.SlugField`:
#    - verbose_name=_('Username')
#    - null=True
#    - blank=True
#    - default=None
# 3. Zdefiniuj metodę `.save()`, która generuje `username`
#    z pierwszej litery `firstname` + całe `lastname`,
#    np. Mark Watney => mwatney
# 4. Użyj `gettext_lazy`
# 5. Uruchom `makemigrations`
# 6. Uruchom `migrate`

# - `Add field username to person`
# - `Applying demo.0005_person_username... OK`

# %% Result
class Person(models.Model):
    lastname = models.CharField(verbose_name=_('Lastname'), max_length=30, null=False, blank=False, db_index=True)
    firstname = models.CharField(verbose_name=_('Firstname'), max_length=30, null=True, blank=True)
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None,
                               validators=[MinLengthValidator(0), MaxLengthValidator(20)])
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True, default=None)
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True, default=None)
    username = models.SlugField(verbose_name=_('Username'), null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        if len(self.firstname) > 0:
            self.username = slugify(self.firstname[0] + self.lastname)
        else:
            self.username = slugify(self.lastname)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.lastname}, {self.firstname}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        ordering = ['lastname']


