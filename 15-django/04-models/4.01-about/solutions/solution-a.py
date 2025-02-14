class Group(models.Model):
    name = models.CharField(verbose_name=_('Group'), max_length=30, null=False, blank=False)