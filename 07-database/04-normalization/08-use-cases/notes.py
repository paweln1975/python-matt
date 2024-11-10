#!/usr/bin/env python3

# Reference:
# https://python3.info/database/normalization/use-cases.html

#%% Theory Relations



#%% Base



#%% Extend



#%% Boolean Vector



#%% FFill



#%% Relations



#%% Serialization



#%% Normal forms
# UNF: Unnormalized form
# 1NF: First normal form
# 2NF: Second normal form
# 3NF: Third normal form
# EKNF: Elementary key normal form
# BCNF: Boyce–Codd normal form
# 4NF: Fourth normal form
# ETNF: Essential tuple normal form
# 5NF: Fifth normal form
# DKNF: Domain-key normal form
# 6NF: Sixth normal form



#%% Recap
# DBA and Programmers use different data format than Data Scientists
# Data Scientists prefer flat formats, without relations and joins
# DBA and Programmers prefer relational data
# For DBA and Programmers flat data formats represents data duplication
# Normalization make data manipulation more consistent
# Normalization uses less space and makes UPDATEs easier
# Normalization causes a lot of SELECT and JOINs, which requires computation
# In XXI century storage is cheap, computing power cost money
# Currently SELECTs are far more common than INSERTs and UPDATEs (let say