#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/structural/proxy.html

#%% Proxy
# EN: Proxy
# PL: Pełnomocnik
# Type: object



#%% Pattern
# Create a proxy, or agent for a remote object
# Agent takes message and forwards to remote object
# Proxy can log, authenticate or cache messages



#%% Problem
# Creating Ebook object is costly, because we have to read it from the disk and store it in memory
# It will load all ebooks in our library, just to select one



#%% Solution
# Lazy evaluation
# Open/Close Principle