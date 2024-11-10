#!/usr/bin/env python3

# Reference:
# https://python3.info/django/models/model-directory.html

#%% Models Directory
# Fat model architecture
# Single File vs. Models per file
# Important, add app_label to model's Meta class
# Important, add __init__.py to the shop/models/ directory
# Important, import from .customer import * in shop/models/__init__.py



#%% Files and Directory Structure



#%% Models
# One model per file
# Important, add app_label to model's Meta class
# Use string in ForeignKey to avoid circular import
# Supporting classes like choices, relations and helper functions, etc. can be in the same file



#%% Init File
# Important, add __init__.py to the shop/models/ directory
# Important, import from .customer import * in shop/models/__init__.py