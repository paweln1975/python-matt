#!/usr/bin/env python3
# https://python3.info/microservices/http/identifier.html


# %% HTTP Identifier
# - URN - name (i.e. book title)
# - URI - resource (i.e. one particular unit of book with that title)
# - URL - location (i.e. where to get it)
# - Locators are also identifiers, so every URL is also a URI
# - There are URIs which are not URLs
# %%



# %% URI
# - URI - Uniform Resource Identifier
# - URI - resource (i.e. one particular unit of book with that title)
# - Example: https://example.com/path/resource.txt#fragment
# - Example: //example.com/path/resource.txt
# - Example: /path/resource.txt
# - Example: path/resource.txt
# - Example: ../resource.txt
# - Example: ./resource.txt
# - Example: resource.txt
# - Example: #fragment
# %%



# %% URN
# - URN - Uniform Resource Name
# - URN - name (i.e. book title)
# - It says what is it, but not where to get it
# - Example: urn:isbn:9788395718625 - Python - from None to AI book, identified by its book number.
# - Example: urn:ISSN:0167-6423 - The scientific journal Science of Computer Programming, identified by its serial number.
# - Example: urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66 - A version 1 UUID.
# %%



# %% URL
# - URL - Uniform Resource Locator
# - URL - location (i.e. where to get it)
# - Example: https://john.doe@www.example.com:123/forum/questions/?tag=networking&order=newest#top
# - Example: ldap://[2001:db8::7]/c=GB?objectClass?one
# - Example: mailto:John.Doe@example.com
# - Example: news:comp.infosystems.www.servers.unix
# - Example: tel:+1-816-555-1212
# - Example: telnet://192.0.2.16:80/
# - Example: urn:oasis:names:specification:docbook:dtd:xml:4.1.2
# %%



