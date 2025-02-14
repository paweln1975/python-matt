class Person(models.Model):
    data = models.JSONField(verbose_name=_('Data'), null=True, blank=True, default=None)