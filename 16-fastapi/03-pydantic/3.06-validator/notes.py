#!/usr/bin/env python3
# https://python3.info/fastapi/pydantic/validator.html


# %% Pydantic Validator
# - Source: https://pydantic-docs.helpmanual.io/usage/validators/
# - validators are "class methods", so the first argument value they receive is the UserModel class, not an instance of UserModel.
# - the second argument is always the field value to validate; it can be named as you please
# - you can also add any subset of the following arguments to the signature (the names must match):
# - values: a dict containing the name-to-value mapping of any previously-validated fields
# - config: the model config
# - field: the field being validated. Type of object is pydantic.fields.ModelField.
# - kwargs: if provided, this will include the arguments above not explicitly listed in the signature
# - validators should either return the parsed value or raise a ValueError, TypeError, or AssertionError (assert statements may be used).
# %%



# %% Validator
# - Validation is done in the order fields are defined. E.g. in the example above, password2 has access to password1 (and name), but password1 does not have access to password2. See Field Ordering for more information on how fields are ordered
# - If validation fails on another field (or that field is missing) it will not be included in values, hence if 'password1' in values and ... in this example.
# %%



# %% Root Validator
# - Validation performed on the entire model's data.
# %%



# %% Pre and Per-item Validator
# %%



