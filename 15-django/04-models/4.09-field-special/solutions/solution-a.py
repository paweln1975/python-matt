class Person(models.Model):
    identifier = models.UUIDField(verbose_name=_('UUID'), unique=True, null=False, blank=False, editable=False, default=uuid4)