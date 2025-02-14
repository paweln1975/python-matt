class Group(models.Model):
    name = models.CharField(verbose_name=_('Group'), max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'demo'
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ['name']