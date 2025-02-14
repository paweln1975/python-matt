class Person(models.Model):
    username = models.SlugField(verbose_name=_('Website'))

    def save(self, *args, **kwargs):
        self.username = slugify(f'{self.firstname[0]}{self.lastname}')
        return super().save(*args, **kwargs)