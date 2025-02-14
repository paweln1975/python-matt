class Person(models.Model):
    weight = models.FloatField(verbose_name=_('Weight'), help_text=_('kg'), validators=[MinValueValidator(50), MaxValueValidator(150)], null=True, blank=True, default=None)