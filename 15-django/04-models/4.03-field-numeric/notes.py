#!/usr/bin/env python3
# https://python3.info/django/models/field-numeric.html


# %% Models Field Numeric
# - models.IntegerField - stores a 32-bit value, minimum -2,147,483,648 and maximum 2,147,483,647
# - models.FloatField - stores a 64-bit floating-point number, minimum -1.79E+308 and maximum 1.79E+308
# - models.DecimalField - stores a fixed-point number (e.g. a monetary amount), requires two arguments: max_digits and decimal_places
# - models.SmallIntegerField - stores a 16-bit value, minimum -32,768 and maximum 32,767
# - models.BigIntegerField - stores a 64-bit value, minimum -9,223,372,036,854,775,808 and maximum 9,223,372,036,854,775,807
# - models.PositiveSmallIntegerField - stores a positive 16-bit value (unsigned int16), minimum 0 and maximum 65,535
# - models.PositiveIntegerField - stores a positive 32-bit value (unsigned int32), minimum 0 and maximum 4,294,967,295
# - models.PositiveBigIntegerField - stores a positive 64-bit value (unsigned int64), minimum 0 and maximum 18,446,744,073,709,551,615
# - models.AutoField - stores an IntegerField that automatically increments according to available IDs
# - models.BigAutoField - stores a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from -9223372036854775808 to 9223372036854775807
# - models.SmallAutoField - like an AutoField, but only allows values under a certain (database-dependent) point
# - float vs. decimal (IEEE-754)
# %%



# %% Arguments
# - decimal_places (DecimalField)
# - max_digits (DecimalField)
# - blank
# - choices
# - db_column
# - db_index
# - default
# - editable
# - error_message
# - help_text
# - limit_choices_to
# - max_length
# - null
# - primary_key
# - unique
# - validators
# - verbose_name
# %%



# %% IntegerField
# - IntegerField
# - SmallIntegerField
# - BigIntegerField
# %%



# %% PositiveIntegerField
# - PositiveIntegerField
# - PositiveSmallIntegerField
# - PositiveBigIntegerField
# %%



# %% FloatField
# - FloatField
# %%



# %% DecimalField
# - DecimalField
# %%



# %% AutoField
# - AutoField
# - BigAutoField
# - SmallAutoField
# %%



# %% Validators
# - MinLengthValidator
# - MaxLengthValidator
# %%



