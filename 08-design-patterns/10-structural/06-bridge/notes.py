#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/structural/bridge.html

#%% Bridge
# EN: Bridge
# PL: Most
# Type: object



#%% Pattern
# Nested hierarchies of classes



#%% Problem
# Every time you want to add new manufacturers remote control, you need to add two classes of ManufacturerRemoteControl and ManufacturerAdvancedRemoteControl
# If you add new another type of remote control, such as MovieRemoteControl you now has to implement three classes



#%% Solution
# Hierarchy grows in two different directions
# We can split complex hierarchy into two hierarchies which grows independently