class Gender(models.TextChoices):
    MALE = 'male', _('Male')
    FEMALE = 'female', _('Female')
    OTHER = 'other', _('Other')


class Customer(models.Model):
    firstname = models.CharField(verbose_name=_('First name'), validators=[MinLengthValidator(2)], max_length=64, null=False, blank=False)
    lastname = models.CharField(verbose_name=_('Last name'), validators=[MinLengthValidator(2)], max_length=64, null=False, blank=False)
    birthdate = models.DateField(verbose_name=_('Birthdate'), null=True, blank=True, default=None)
    gender = models.CharField(verbose_name=_('Gender'), choices=Gender, max_length=20, null=True, blank=True, default=None)
    tax_number = models.CharField(verbose_name=_('Tax number'), max_length=20, null=True, blank=True, default=None, help_text=_('Tax Identification Number'))
    email = models.EmailField(verbose_name=_('Email'), max_length=100, unique=True, null=True, blank=True, default=None, db_index=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=20, null=True, blank=True, default=None, help_text=_('Phone including country code'))
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/', null=True, blank=True, default=None)
    is_verified = models.BooleanField(verbose_name=_('Is verified'), max_length=20, null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        app_label = 'shop'