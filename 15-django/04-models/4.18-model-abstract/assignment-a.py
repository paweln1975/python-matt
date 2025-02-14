"""
Name: Django Model Abstract
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

BaseModel: type

# English
# 0. Use `myproject`
# 1. Create abstract model `BaseModel` with:
#    - `uuid` jako UUIDField with null: no, blank: no, editable: no, default: uuid4, help_text
#    - `created_user` jako ForeignKey with related_name: '+', to: 'auth.User', null: yes, blank: yes, on_delete: set null, help_text
#    - `created_date` jako DateTimeField with null: no, blank: no, auto_now_add: yes, help_text
#    - `modified_user` jako ForeignKey with to: 'auth.User', related_name: '+', null: yes, blank: yes, on_delete: set null, help_text
#    - `modified_date` jako DateTimeField with null: no, blank: false, auto_now: yes, help_text
#    - `is_deleted` jako BooleanField with null: no, blank: no, default: false, help_text
# 2. Use `gettext_lazy`
# 3. Run `makemigrations`
# 4. Run `migrate`

# Polish
# 0. Użyj `myproject`
# 1. Stwórz abstrakcyjny model `BaseModel` z:
#    - `uuid` jako UUIDField with null: nie, blank: nie, editable: nie, default: uuid4, help_text
#    - `created_user` jako ForeignKey with related_name: '+', to: 'auth.User', null: tak, blank: tak, on_delete: set null, help_text
#    - `created_date` jako DateTimeField with null: nie, blank: nie, auto_now_add: tak, help_text
#    - `modified_user` jako ForeignKey with to: 'auth.User', related_name: '+', null: tak, blank: tak, on_delete: set null, help_text
#    - `modified_date` jako DateTimeField with null: nie, blank: false, auto_now: tak, help_text
#    - `is_deleted` jako BooleanField with null: nie, blank: nie, default: false, help_text
# 2. Użyj `gettext_lazy`
# 3. Uruchom `makemigrations`
# 4. Uruchom `migrate`

# %% Result
class BaseModel(models.Model):
    uuid = models.UUIDField(verbose_name=_('UUID'), null=False, blank=False, editable=False, default=uuid4, help_text=_('Object Unique Identifier'))
    created_user = models.ForeignKey(verbose_name=_('Created User'), related_name='+', to='auth.User', null=True, blank=True, on_delete=models.SET_NULL, help_text=_('User'))
    created_date = models.DateTimeField(verbose_name=_('Created Date'), null=False, blank=False, auto_now_add=True, help_text=_('UTC Date and Time'))
    modified_user = models.ForeignKey(verbose_name=_('Modified User'), to='auth.User', related_name='+',  null=True, blank=True, on_delete=models.SET_NULL, help_text=_('User'))
    modified_date = models.DateTimeField(verbose_name=_('Modified Date'), null=False, blank=False, auto_now=True, help_text=_('UTC Date and Time'))
    is_deleted = models.BooleanField(verbose_name=_('Is Deleted?'), null=False, blank=False, default=False, help_text=_('Is record deleted?'))

    class Meta:
        ...
        ordering = ['-created_date']
        verbose_name = _('Base Model')
        verbose_name_plural = _('Base Models')