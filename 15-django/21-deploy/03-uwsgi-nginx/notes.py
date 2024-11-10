#!/usr/bin/env python3

# Reference:
# https://python3.info/django/deploy/uwsgi-nginx.html

#%% Deploy Nginx and uWSGI
# File socket: server unix:///data/myproject/myproject.sock;
# TCP socket: server 127.0.0.1:8000;
# File sockets are a bit faster and can be more secure (no TCP overhead)



#%% Nginx



#%% uWSGI