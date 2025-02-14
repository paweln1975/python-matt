#!/usr/bin/env python3
# https://python3.info/django/models/field-storage.html


# %% Models Field Storage
# - models.ImageField - stores an image, in database it stores the path to the image
# - models.FileField - stores a file, in database it stores the path to the file
# - models.FilePathField - stores a file path, in database it stores the path to the file
# - models.BinaryField - stores a binary data, in database it stores the binary data (BLOB)
# %%



# %% Arguments
# - upload_to (str) - The directory to which the file is uploaded.
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



# %% ImageField
# - ImageField
# - pip install Pillow
# - settings.MEDIA_ROOT
# - settings.MEDIA_URL
# %%



# %% FileField
# - FileField
# - settings.MEDIA_ROOT
# - settings.MEDIA_URL
# %%



# %% FilePathField
# - FilePathField
# %%



# %% BinaryField
# - BinaryField
# %%



