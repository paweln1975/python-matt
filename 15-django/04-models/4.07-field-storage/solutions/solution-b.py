class Person(models.Model):
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/', null=True, blank=True, default=None)