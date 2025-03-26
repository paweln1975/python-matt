from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Group(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ['name']