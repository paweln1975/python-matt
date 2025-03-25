from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'
    label = 'demo'
    verbose_name = _('Demo Application')
    verbose_name_plural = _('Demos Applications')