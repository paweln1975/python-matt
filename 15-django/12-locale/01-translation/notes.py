#!/usr/bin/env python3

# Reference:
# https://python3.info/django/locale/translation.html

#%% Localization Translation
# i18n - Internationalization
# l10n - Localization



#%% Gettext
# .po files
# .mo files
# Using gettext in code
# Generating translation files
# Compiling translation files
# Updating translation files



#%% Settings
# https://docs.djangoproject.com/en/stable/topics/i18n/



#%% Change
# from django.conf.locale.en import formats as en_formats



#%% Manage
# django-admin makemessages -l en
# django-admin compilemessages



#%% Templates
# {% load i18n %}
# {% translate %}
# {% blocktranslate %} and {% endblocktranslate %}



#%% Files
# from django.utils.translation import gettext_lazy as _
# _('My string to translate')



#%% Poedit



#%% Transifex
# https://www.transifex.com/
# python -m pip install transifex-client
# tx push
# tx pull



#%% Further Reading
# https://github.com/django/django/blob/master/django/utils/formats.py
# https://github.com/django/django/blob/master/django/conf/locale/pl/formats.py
# https://github.com/django/django/blob/master/django/conf/locale/en/formats.py
# https://github.com/django/django/blob/main/django/conf/locale/hi/formats.py