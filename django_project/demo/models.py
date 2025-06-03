from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
class BaseModel(models.Model):
    created_user = models.ForeignKey(verbose_name=_('Created User'), related_name='+', to='auth.User', null=True, blank=True, on_delete=models.SET_NULL, help_text=_('User'))
    created_date = models.DateTimeField(verbose_name=_('Created Date'), null=False, blank=False, auto_now_add=True, help_text=_('UTC Date and Time'))
    modified_user = models.ForeignKey(verbose_name=_('Modified User'), to='auth.User', related_name='+',  null=True, blank=True, on_delete=models.SET_NULL, help_text=_('User'))
    modified_date = models.DateTimeField(verbose_name=_('Modified Date'), null=False, blank=False, auto_now=True, help_text=_('UTC Date and Time'))
    is_deleted = models.BooleanField(verbose_name=_('Is Deleted?'), null=False, blank=False, default=False, help_text=_('Is record deleted?'))

    class Meta:
        abstract = True
        ordering = ['-created_date']
        verbose_name = _('Base Model')
        verbose_name_plural = _('Base Models')


class Language(models.TextChoices):
    POLISH = 'pl', _('Polish')
    ENGLISH = 'en', _('English')

class Currency(models.IntegerChoices):
    USD = 10, _('USD')
    PLN = 20, _('PLN')

class Role(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=False, blank=False, db_index=True)
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Role')
        verbose_name_plural = _('Role')
        ordering = ['name']


class Person(BaseModel):
    lastname = models.CharField(verbose_name=_('Lastname'), max_length=30, null=False, blank=False, db_index=True)
    firstname = models.CharField(verbose_name=_('Firstname'), max_length=30, null=False, blank=False)
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None,
                               validators=[MinLengthValidator(0), MaxLengthValidator(20)])
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True, default=None)
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True, default=None)
    username = models.SlugField(verbose_name=_('Username'), null=True, blank=True, default=None)
    height = models.IntegerField(verbose_name=_('Height'), help_text=_('cm'),
                                 validators=[MinValueValidator(150), MaxValueValidator(250)],
                                 null=True, blank=True, default=None)
    weight = models.FloatField(verbose_name=_('Weight'), help_text=_('kg'),
                                 validators=[MinValueValidator(50), MaxValueValidator(150)],
                                 null=True, blank=True, default=None)
    salary = models.DecimalField(verbose_name=_('Salary'), max_digits=12, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True, null=False, blank=False)
    birthdate = models.DateField(verbose_name=_('Birthdate'), null=True, blank=True, default=None)
    wakeup = models.TimeField(verbose_name=_('Wakeup'), null=True, blank=True, default=None)
    since = models.DateTimeField(verbose_name=_('Since'), null=True, blank=True, default=None)
    duration = models.DurationField(verbose_name=_('Duration'), null=True, blank=True, default=None)
    language = models.CharField(verbose_name=_('Language'), max_length=2, null=False, blank=False,
                                default=Language.POLISH, choices=Language)
    currency = models.IntegerField(verbose_name=_('Currency'), null=False, blank=False,
                                   default=Currency.PLN, choices=Currency)
    roles = models.ManyToManyField(verbose_name=_('Roles'), to='Role', related_name='persons', blank=True)

    def get_absolute_url(self):
        return reverse("demo-person-detail", kwargs={"pk": self.pk})

    @staticmethod
    def add(firstname, lastname):
        person = Person(firstname=firstname, lastname=lastname)
        person.full_clean()
        person.save()
        return person

    def clean(self):
        if '@' in self.firstname:
            raise ValidationError('Firstname contains invalid character')
        if '@' in self.lastname:
            raise ValidationError('Lastname contains invalid character')

    def save(self, *args, **kwargs):
        if len(self.firstname) > 0:
            self.username = slugify(self.firstname[0] + self.lastname)
        else:
            self.username = slugify(self.lastname)

        return super().save(*args, **kwargs)

    def __str__(self):
        # Check if both firstname and lastname are empty or just whitespace
        if not self.firstname.strip() and not self.lastname.strip():
            return '-'
        else:
            # If at least one is not empty, return the concatenated string
            return f'{self.firstname} {self.lastname}'.strip()

    def get_full_name(self):
        return str(self)

    class Meta:
        app_label = 'demo'
        verbose_name = _('Person')
        verbose_name_plural = _('People')
        ordering = ['lastname']


class Address(models.Model):
    street = models.CharField(verbose_name=_('Street'), max_length=20, null=True, blank=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=20, null=False, blank=False)
    postcode = models.CharField(verbose_name=_('Postcode'), max_length=20, null=True, blank=True, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=20, null=False, blank=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('Person'), related_name='addresses')

    def __str__(self):
        return f'{self.city}, {self.country}'

    class Meta:
        app_label = 'demo'
        ordering = ['country', 'city']
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')