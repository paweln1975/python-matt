class Person(models.Model):
    comment = models.TextField(verbose_name=_('Comment'), null=True, blank=True, default=None)