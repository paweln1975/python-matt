class Person(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'), null=True, blank=True, default=None)