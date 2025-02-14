class Person(models.Model):
    roles = models.ManyToManyField(verbose_name=_('Roles'), to='demo.Role', blank=True)