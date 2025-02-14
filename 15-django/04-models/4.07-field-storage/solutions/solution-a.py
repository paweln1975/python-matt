class Person(models.Model):
    file = models.FileField(verbose_name=_('File'), upload_to='files/', null=True, blank=True, default=None)