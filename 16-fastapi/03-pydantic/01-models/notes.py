#!/usr/bin/env python3

# Reference:
# https://python3.info/fastapi/pydantic/models.html

#%% Pydantic Models
# Source: https://pydantic-docs.helpmanual.io/usage/models/#private-model-attributes



#%% Basic model usage



#%% Model properties
# dict() - returns a dictionary of the model's fields and values
# json() - returns a JSON string representation dict()
# copy() - returns a copy (by default, shallow copy) of the model
# parse_obj() - a utility for loading any object into a model with error handling if the object is not a dictionary
# parse_raw() - a utility for loading strings of numerous formats
# parse_file() - like parse_raw() but for file paths
# from_orm() - loads data into a model from an arbitrary class
# schema() - returns a dictionary representing the model as JSON Schema
# schema_json() - returns a JSON string representation of schema()
# construct() - a class method for creating models without running validation
# _fields_set__ - Set of names of fields which were set when the model instance was initialised
# _fields__ - a dictionary of the model's fields
# _config__ - the configuration class for the model



#%% Recursive Models



#%% ORM Mode (aka Arbitrary Class Instances)



#%% Reserved names



#%% Recursive ORM models



#%% Data binding



#%% Error Handling
# pydantic will raise ValidationError whenever it finds an error in the data it's validating.



#%% Custom Errors



#%% Helper Functions



#%% Creating models without validation



#%% Generic Models



#%% Dynamic model creation



#%% Model creation from ``NamedTuple`` or ``TypedDict``



#%% Custom Root Types



#%% Faux Immutability



#%% Abstract Base Classes



#%% Field Ordering



#%% Required fields



#%% Required Optional fields



#%% Field with dynamic default value



#%% Automatically excluded attributes



#%% Private model attributes



#%% Parsing data into a specified type



#%% Data Conversion



#%% Model signature