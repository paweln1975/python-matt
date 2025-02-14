class Person(models.Model):
    comment = models.TextField(verbose_name=_('Comment'), validators=[MinLengthValidator(2), MaxLengthValidator(20)], null=True, blank=True, default=None)