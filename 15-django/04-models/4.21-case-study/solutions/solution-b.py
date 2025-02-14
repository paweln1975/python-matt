class AddressType(models.TextChoices):
    BILLING = 'billing', _('Billing')
    SHIPPING = 'shipping', _('Shipping')


class Address(models.Model):
    customer = models.ForeignKey(verbose_name=_('Customer'), to='shop.Customer', on_delete=models.CASCADE, null=False, blank=False)
    type = models.CharField(verbose_name=_('Type'), max_length=20, choices=AddressType, null=False, blank=False, default=AddressType.BILLING, db_index=True)
    street = models.CharField(verbose_name=_('Street'), max_length=100, null=True, blank=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=True, blank=True, default=None)
    postcode = models.CharField(verbose_name=_('Postcode'), max_length=20, null=True, blank=True, default=None)
    region = models.CharField(verbose_name=_('Region'), max_length=100, null=True, blank=True, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.customer} {self.type}: {self.street}, {self.city}, {self.country}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        app_label = 'shop'