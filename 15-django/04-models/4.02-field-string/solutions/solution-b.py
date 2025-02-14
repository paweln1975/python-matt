class Person(models.Model):
    firstname = models.CharField(verbose_name=_('Firstname'), max_length=30, null=False, blank=False)