class Person(models.Model):
    birthdate = models.DateField(verbose_name=_('Birthdate'), null=True, blank=True, default=None)