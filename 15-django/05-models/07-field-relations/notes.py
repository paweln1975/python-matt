#!/usr/bin/env python3

# Reference:
# https://python3.info/django/models/field-relations.html

#%% Models Field Relation
# models.ForeignKeyField - represents many-to-one relationship, requires two arguments: to and on_delete
# models.OneToOneField - represents one-to-one relationship, requires two arguments: to and on_delete
# models.ManyToManyField - represents many-to-many relationship, requires one argument: to



#%% Arguments
# on_delete (ForeignKey, ManyToManyField)
# related_name (ForeignKey, ManyToManyField)
# to (ForeignKey, ManyToManyField)
# limit_choices_to (ForeignKey, ManyToManyField)
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