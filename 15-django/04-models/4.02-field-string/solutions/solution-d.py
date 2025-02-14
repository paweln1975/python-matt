class Person(models.Model):
    email = models.EmailField(verbose_name=_('Email'), null=False, blank=False, unique=True)