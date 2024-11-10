#!/usr/bin/env python3

# Reference:
# https://python3.info/django/models/field-special.html

#%% Models Field Special
# models.UUIDField - a field for storing UUID values (universally unique identifiers)
# models.CommaSeparatedIntegerField - a CharField that checks that the value is a comma-separated list of integers
# models.GenericIPAddressField - a CharField that checks that the value is a valid IPv4 or IPv6 address
# models.IPAddressField - deprecated in favor of GenericIPAddressField
# models.JSONField - stores a field for storing JSON-encoded data. In Python, it is a dict
# models.GeneratedField - a field that is automatically populated with a value when the model is saved



#%% GeneratedField
# https://docs.djangoproject.com/en/stable/ref/models/fields/#django.db.models.GeneratedField
# Example: slug, age, area, etc.
# db_persist: If True, the field value will be saved to the database
# db_persist: If False, the field will be calculated on the fly (like @property)



#%% Arguments
# blank
# choices
# db_column
# db_index
# default
# editable
# error_message
# help_text
# limit_choices_to
# max_length
# null
# primary_key
# unique
# validators
# verbose_name