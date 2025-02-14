#!/usr/bin/env python3
# https://python3.info/fastapi/pydantic/types-pydantic.html


# %% Pydantic Types Custom
# - FilePath - like Path, but the path must exist and be a file
# - DirectoryPath - like Path, but the path must exist and be a directory
# - PastDate - like date, but the date should be in the past
# - FutureDate - like date, but the date should be in the future
# - EmailStr - the input string must be a valid email address, and the output is a simple string
# - NameEmail - the input string must be either a valid email address or in the format Fred Bloggs <fred.bloggs@example.com>, and the output is a NameEmail object which has two properties: name and email.
# - PyObject - expects a string and loads the python object importable at that dotted path; e.g. if 'math.cos' was provided, the resulting field value would be the function cos
# - Color - for parsing HTML and CSS colors
# - Json - a special type wrapper which loads JSON before parsing
# - PaymentCardNumber - for parsing and validating payment cards
# - AnyUrl - any URL
# - AnyHttpUrl - an HTTP URL
# - HttpUrl - a stricter HTTP URL
# - FileUrl - a file path URL
# - PostgresDsn - a postgres DSN style URL
# - RabbitMqDsn - an AMQP DSN style URL as used by RabbitMQ, StormMQ, ActiveMQ etc.
# - RedisDsn - a redis DSN style URL
# - stricturl - a type method for arbitrary URL constraints
# - UUID1 - requires a valid UUID of type 1
# - UUID3 - requires a valid UUID of type 3
# - UUID4 - requires a valid UUID of type 4
# - UUID5 - requires a valid UUID of type 5
# - SecretBytes - bytes where the value is kept partially secret
# - SecretStr - string where the value is kept partially secret
# - IPvAnyAddress - allows either an IPv4Address or an IPv6Address
# - IPvAnyInterface - allows either an IPv4Interface or an IPv6Interface
# - IPvAnyNetwork - allows either an IPv4Network or an IPv6Network
# - NegativeFloat - allows a float which is negative; uses standard float parsing then checks the value is less than 0
# - NegativeInt - allows an int which is negative; uses standard int parsing then checks the value is less than 0
# - PositiveFloat - allows a float which is positive; uses standard float parsing then checks the value is greater than 0
# - PositiveInt - allows an int which is positive; uses standard int parsing then checks the value is greater than 0
# %%



# %% Email Types
# %%



# %% URL Fields
# %%



# %% URL Properties
# %%



# %% International Domains
# %%



# %% Color Type
# %%



# %% Secret Types
# %%



# %% Json Type
# %%



# %% Payment Card Numbers
# %%



# %% Strict Types
# %%



# %% ByteSize
# %%



# %% Custom Data Types
# %%



# %% Classes with _get_validators__
# %%



# %% Arbitrary Types Allowed
# %%



