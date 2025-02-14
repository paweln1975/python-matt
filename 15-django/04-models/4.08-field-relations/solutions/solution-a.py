class Person(models.Model):
    o2o = models.OneToOneField(verbose_name=_('One To One'), to='...', blank=True, null=True, default=None)