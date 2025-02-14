class Order(models.Model):
    customer = models.ForeignKey(verbose_name=_('Customer'), to='shop.Customer', on_delete=models.CASCADE, null=False, blank=False)
    products = models.ManyToManyField(verbose_name=_('Products'), to='shop.Product', blank=True)

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        app_label = 'shop'