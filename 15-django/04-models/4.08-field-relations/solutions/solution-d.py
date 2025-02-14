class Address(models.Model):
    person = models.ForeignKey(verbose_name=_('Person'), to='demo.Person', on_delete=models.CASCADE, null=True, blank=True)