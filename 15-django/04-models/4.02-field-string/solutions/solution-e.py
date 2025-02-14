class Person(models.Model):
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True, default=None)