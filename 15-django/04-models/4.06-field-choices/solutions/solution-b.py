class Currency(models.IntegerChoices):
    USD = 1, _('US Dollar')
    PLN = 2, _('Polish Zloty')


class Person(models.Model):
    currency = models.IntegerField(verbose_name=_('Currency'), choices=Currency, null=True, blank=True, default=Currency.USD)