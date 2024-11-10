#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/structural/adapter.html

#%% Adapter
# EN: Adapter
# PL: Adapter
# Type: class and object



#%% Pattern
# Convert an interface of an object to a different form
# Like power socket adapter for US and EU
# Refactoring of a large application
# Working with legacy code / database
# Niekompatybilne API dwóch systemów
# Wymagające różnych sposobów uwierzytelniania (OAuth2, BasicAuth)
# Tłumaczenie pomiędzy różnymi formatami danych (SOAP/XML, REST/JSON)
# Iteracyjne przepisywanie legacy systemu na nowy, ale tak, aby móc wciąż korzystać ze starego



#%% Problem
# BlackAndWhite3rdPartyFilter is from external library
# Does not conform to Filter interface
# Do not have apply() method
# Need manual call of init() at initialization
# Need manual call of render()



#%% Solution
# Inheritance is simpler
# Composition is more flexible
# Favor Composition over Inheritance