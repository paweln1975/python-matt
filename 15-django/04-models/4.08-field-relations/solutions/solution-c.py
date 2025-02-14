class Person(models.Model):
    groups = models.ManyToManyField(verbose_name=_('Group'), to='auth.Group', limit_choices_to={'name__startswith': 'customer_'}, blank=True)