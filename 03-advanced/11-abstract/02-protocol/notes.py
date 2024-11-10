#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/abstract/protocol.html

#%% Abstract Protocol
# Protocol describe an interface, not an implementation
# Protocol classes should not have method implementations
# Protocol can describe both methods and attributes
# Since Python 3.8
# :pep:544 -- Protocols: Structural subtyping (static duck typing)



#%% Problem



#%% Solution: Abstract Class
# Implementation is through the inheritance
# Validation is dynamic (in the runtime)



#%% Solution: Protocol
# Implementation is through structural subtyping
# No inheritance, just complying to the structure (having the same methods)



#%% Duck Typing
# If it walks like a duck, and it quacks like a duck, then it must be a duck.
# If it logins like an Account, and it logouts like an Account, then it must be an Account.
# If it have method login like an Account, and it have method logout like an Account, then it adheres to the protocol Account.



#%% Terminology



#%% Explicit Subtyping
# Email is explicit subclass of the protocol



#%% Structural Subtyping
# If an object that has all the protocol attributes it implements it
# Structural subtyping is natural for Python programmers
# Matches the runtime semantics of duck typing
# User is structural subtype of a protocol (it conforms to structure)
# User is implicit subtype of the protocol Account (does not inherits)
# User implement the protocol Account
# User is compatible with a protocol Account



#%% What Protocols are Not?
# At runtime, protocol classes is simple ABC
# No runtime type check
# Protocols are completely optional



#%% Runtime Checkable
# By default isinstance() and issubclass() won't work with protocols
# You can use typing.runtime_checkable decorator to make it work



#%% Unions



#%% Merging Protocols



#%% Interface Segregation Principle
# S.O.L.I.D. Principles
# ISP - Interface Segregation Principle
# Clients should not be forced to depend upon interfaces that they do not use.



#%% Generic Protocols



#%% Recursive Protocols
# Since 3.11 :pep:673 –- Self Type



#%% Modules as Implementations of Protocols



#%% Callbacks