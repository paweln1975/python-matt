class Person(models.Model):
    is_active = models.BooleanField(verbose_name=_('Is Active?'), null=False, blank=False, default=True)