class Person(models.Model):
    wakeup = models.TimeField(verbose_name=_('Wakeup'), null=True, blank=True, default=None)