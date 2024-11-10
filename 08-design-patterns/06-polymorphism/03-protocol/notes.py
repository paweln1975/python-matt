#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/polymorphism/protocol.html

#%% Abstract Protocol
# :pep:544 -- Protocols: Structural subtyping (static duck typing)
# Since Python 3.8
# Protocol describe an interface, not an implementation
# Protocol classes should not have method implementations
# Protocol can describe both methods and attributes



#%% Standard Library Protocols
# from collections.abc import *
# Container
# Hashable
# Iterable
# Iterator
# Reversible
# Generator
# Callable
# Collection
# Sequence
# MutableSequence
# ByteString
# Set
# MutableSet
# Mapping
# MutableMapping
# MappingView
# ItemsView
# KeysView
# ValuesView
# Awaitable
# Coroutine
# AsyncIterator
# AsyncGenerator



#%% Terminology



#%% Explicit Subtyping
# Email is explicit subclass of the protocol



#%% Structural Subtyping
# If an object that has all the protocol attributes it implements it
# Structural subtyping is natural for Python programmers
# Matches the runtime semantics of duck typing
# Email is structural subtype of a protocol (it conforms to structure)
# Email is implicit subtype of the protocol Message (not inherits)
# Email implement the protocol Message
# Email is compatible with a protocol Message



#%% What Protocols are Not?
# At runtime, protocol classes is simple ABC
# No runtime type check
# Protocols are completely optional



#%% Covariance, Contravariance, Invariance
# https://www.youtube.com/watch?v=1IiL31tUEVk&t=445s
# Covariance - Enables you to use a more derived type than originally specified
# Contravariance - Enables you to use a more generic (less derived) type than originally specified
# Invariance - Means that you can use only the type originally specified.
# Invariance is important for example in np.ndarray, where all items must be exactly the same type



#%% Default Value



#%% Merging and extending protocols



#%% Generic Protocols



#%% Recursive Protocols
# Since 3.11 :pep:673 –- Self Type
# Since 3.7 from __future__ import annotations
# Future :pep:563 -- Postponed Evaluation of Annotations



#%% Unions



#%% Modules as implementations of protocols



#%% Callbacks



#%% Runtime Checkable
# By default isinstance() and issubclass() won't work with protocols
# You can use typing.runtime_checkable decorator to make it work