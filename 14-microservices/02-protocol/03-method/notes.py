#!/usr/bin/env python3

# Reference:
# https://python3.info/microservices/protocol/method.html

#%% HTTP Method
# GET - Read
# POST - Create
# PUT - Update/Replace
# PATCH - Partial Update/Modify
# DELETE - Delete
# HEAD - Show Headers
# CONNECT - Connect
# OPTIONS - Show HTTP Methods
# TRACE - Show Trace



#%% GET
# GET - Read
# Retrieve data
# No other effect



#%% POST
# POST - Create
# Stores information on the server
# Requires whole object
# Assigns a new URI



#%% PUT
# PUT - Update/Replace
# Stores information on the server
# Requires whole object
# Reuse URI



#%% PATCH
# PATCH - Partial Update/Modify
# Stores information on the server
# Requires part of object
# Reuse URI



#%% DELETE
# DELETE - Delete
# Removes information from the server
# Requires URI
# Discards URI



#%% HEAD
# HEAD - Show Headers
# Identical to GET request without the response body



#%% CONNECT
# CONNECT - Connect
# Request connection to a transparent TCP/IP tunnel
# Used for SSL-encryption (HTTPS) through an unencrypted HTTP proxy



#%% OPTIONS
# OPTIONS - Show HTTP Methods
# Returns HTTP methods for the specified URL



#%% TRACE
# TRACE - Show Trace
# Echoes the received request
# Debug what changes have been made by intermediate servers



#%% Match Block
# HTTP Request
# Match Block
# 'GET /index.html HTTP/2.0'