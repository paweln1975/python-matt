#!/usr/bin/env python3
# https://python3.info/microservices/http/status.html


# %% HTTP Status
# - 1XX - Informational
# - 2XX - Successful
# - 3XX - Redirection
# - 4XX - Client Error
# - 5XX - Server Error
# %%



# %% 1xx Informational response
# - 100 - Continue
# - 101 - Switching Protocols
# - 102 - Processing (WebDAV)
# - 103 - Early Hints
# %%



# %% 2xx Success
# - 200 - OK
# - 201 - Created
# - 202 - Accepted
# - 203 - Non-Authoritative Information
# - 204 - No Content
# - 205 - Reset Content
# - 206 - Partial Content
# - 207 - Multi-Status (WebDAV)
# - 208 - Already Reported (WebDAV)
# - 209 - IM Used
# %%



# %% 3xx Redirection
# - 300 - Multiple Choices
# - 301 - Moved Permanently
# - 302 - Found (Previously 'Moved temporarily')
# - 303 - See Other
# - 304 - Not Modified
# - 305 - Use Proxy
# - 306 - Switch Proxy
# - 307 - Temporary Redirect
# - 308 - Permanent Redirect
# %%



# %% 4xx Client errors
# - 400 - Bad Request
# - 401 - Unauthorized
# - 402 - Payment Required
# - 403 - Forbidden
# - 404 - Not Found
# - 405 - Method Not Allowed
# - 406 - Not Acceptable
# - 407 - Proxy Authentication Required
# - 408 - Request Timeout
# - 409 - Conflict
# - 410 - Gone
# - 411 - Length Required
# - 412 - Precondition Failed
# - 413 - Payload Too Large
# - 414 - URI Too Long
# - 415 - Unsupported Media Type
# - 416 - Range Not Satisfiable
# - 417 - Expectation Failed
# - 418 - I'm a teapot - This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324
# - 421 - Misdirected Request
# - 422 - Unprocessable Entity (WebDAV)
# - 423 - Locked (WebDAV)
# - 424 - Failed Dependency (WebDAV)
# - 426 - Upgrade Required
# - 428 - Precondition Required
# - 429 - Too Many Requests
# - 431 - Request Header Fields Too Large
# - 451 - Unavailable For Legal Reasons
# %%



# %% 5xx Server errors
# - 500 - Internal Server Error
# - 501 - Not Implemented
# - 502 - Bad Gateway
# - 503 - Service Unavailable
# - 504 - Gateway Timeout
# - 505 - HTTP Version Not Supported
# - 506 - Variant Also Negotiates
# - 507 - Insufficient Storage (WebDAV)
# - 508 - Loop Detected (WebDAV)
# - 510 - Not Extended
# - 511 - Network Authentication Required
# %%



# %% Built-in Match
# - HTTP Status
# %%



# %% Custom Enum
# - from enum import Enum
# %%



# %% Built-in Enum
# - from http import HTTPStatus
# %%



