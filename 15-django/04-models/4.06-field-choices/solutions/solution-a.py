class Language(models.TextChoices):
    ENGLISH = 'en', _('English')
    POLISH = 'pl', _('Polish')


class Person(models.Model):
    language = models.CharField(verbose_name=_('Language'), max_length=2, choices=Language, null=True, blank=True, default=Language.ENGLISH)