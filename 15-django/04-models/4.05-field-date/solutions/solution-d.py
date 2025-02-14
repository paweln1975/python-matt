class Person(models.Model):
    duration = models.DurationField(verbose_name=_('Duration'), null=True, blank=True, default=None)