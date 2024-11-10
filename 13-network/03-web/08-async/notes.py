#!/usr/bin/env python3

# Reference:
# https://python3.info/network/web/async.html

#%% Asynchronous processing
# You want your *WSGI* server to respond to incoming requests as quickly as possible.
# Each request ties up a worker process until the response is finished.
# Moving work off those workers by spinning up asynchronous jobs as tasks in a queue is a straightforward way to improve *WSGI* server response times.



#%% ASGI
# https://asgi.readthedocs.io/en/latest/



#%% ``Celery``



#%% Celery daemon
# celeryd
# Executes tasks
# Workers that handle whatever tasks you put
# Each worker will perform a task
# When the task is completed will pick up the next one
# The cycle will repeat continuously
# Waiting idly when there are no more tasks



#%% Celerybeat
# scheduler
# cron like
# example execution:



#%% Install
# Requires RabbitMQ



#%% Basic usage



#%% More info
# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
# https://www.youtube.com/watch?v=68QWZU_gCDA
# https://www.youtube.com/watch?v=-ISgjBQDnhw



#%% ``RabbitMQ``
# *RabbitMQ* is the most widely deployed open source message broker
# Implementation of the *Advanced Message Queuing Protocol* (*AQMP*)
# *AQMP* is an open standard



#%% Install



#%% Config



#%% Management Console
# Manage users and their permissions and roles
# Create new queues
# Manage queues, monitor their consumption rate etc.
# Purge data which is currently on queues
# Send and receive messages
# Memory usage against each queue and by the overall process



#%% Manage RabbitMQ