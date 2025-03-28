from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify

# Create your models here.

class Group(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=False, blank=False, db_index=True)
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ['name']


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
