#!/usr/bin/env python3

# Reference:
# https://python3.info/django/manage/locale.html

#%% Manage Translation
# gettext
# from django.utils.translation import gettext_lazy as _
# _('string')
# {% blocktranslate %} and {% endblocktranslate %}
# {% translate "string" %}
# django-admin makemessages -l pl
# django-admin compilemessages
# LANGUAGE_CODE = 'en-us'
# USE_I18N = True
# django.middleware.locale.LocaleMiddleware
# .po and .mo files
# locale directory



#%% Timezone
# django.utils.timezone
# from django.conf.locale.en import formats as en_formats



#%% Gettext
# .po files
# .mo files
# Using gettext in code
# Generating translation files
# Compiling translation files
# Updating translation files
# Transifex (tx push and tx pull)



#%% i18n - internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
# from django.utils.translation import gettext_lazy as _
# {% blocktranslate %} and {% endblocktranslate %}
# {% translate %}
# django-admin makemessages -l en
# django-admin compilemessages
# transifex-client
# gettext
# poedit