#!/usr/bin/env python3

# Reference:
# https://python3.info/fastapi/fastapi/docs-schema.html

#%% FastAPI Schema
# Schema - also known as Model
# Represents data in your system
# Pydantic class
# schema_extra is used by Swagger to show examples
# Ellipsis (...) in Pydantic indicates that a Field is required



#%% Validation
# Validators are "class methods", so the first argument value they receive is the Astronaut class, not an instance of Astronaut.
# The second argument is always the field value to validate; it can be named as you please
# Validators should either return the parsed value or raise a ValueError, TypeError, or AssertionError (assert statements may be used).
# Validation is done in the order fields are defined