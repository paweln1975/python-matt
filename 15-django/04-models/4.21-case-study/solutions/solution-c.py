class Product(models.Model):
    barcode = models.CharField(verbose_name=_('Barcode'), max_length=13, null=False, blank=False, default=None)
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=False, blank=False, default=None)
    price = models.DecimalField(verbose_name=_('Price'), help_text=_('Net price'), max_digits=10, decimal_places=2, null=False, blank=False, default=None)

    def __str__(self):
        return f'{self.name} ({self.barcode})'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        app_label = 'shop'