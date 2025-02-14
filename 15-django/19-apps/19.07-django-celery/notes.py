#!/usr/bin/env python3
# https://python3.info/django/apps/django-celery.html


# %% Django Celery
# - https://www.djangoproject.com/weblog/2024/may/29/django-enhancement-proposal-14-background-workers/
# - https://github.com/django/deps/blob/main/accepted/0014-background-workers.rst
# - A task queue implementation for *Python* web applications
# - Asynchronously execute work outside the *HTTP* request-response cycle
# - Can run batch jobs in the background on a regular schedule
# %%



# %% Install
# %%



# %% Configuration
# - https://docs.celeryq.dev/en/stable/userguide/configuration.html#new-lowercase-settings
# - Version 4.0 introduced new lower case settings and setting organization.
# - The major difference between previous versions, apart from the lower case names, are the renaming of some prefixes, like celery_beat to beat, celeryd to worker, and most of the top level celery settings have been moved into a new task prefix.
# - Celery will still be able to read old configuration files until Celery 6.0. Afterwards, support for the old configuration files will be removed. We provide the celery upgrade command that should handle plenty of cases (including Django).
# %%



# %% Worker
# - Executes tasks
# - Workers that handle whatever tasks you put
# - Each worker will perform a task
# - When the task is completed will pick up the next one
# - The cycle will repeat continuously
# - Waiting idly when there are no more tasks
# %%



# %% Run Tasks
# - T.delay(arg, kwarg=value) - Star arguments shortcut to .apply_async. (.delay(*args, **kwargs) calls .apply_async(args, kwargs)).
# - T.apply_async((arg,), {'kwarg': value})
# - T.apply_async(countdown=10) - executes in 10 seconds from now.
# - T.apply_async(eta=now + timedelta(seconds=10)) - executes in 10 seconds from now, specified using eta
# - T.apply_async(countdown=60, expires=120) - executes in one minute from now, but expires after 2 minutes.
# - T.apply_async(expires=now + timedelta(days=2)) - expires in 2 days, set using datetime.
# %%



# %% Status
# - PENDING -> STARTED -> SUCCESS
# %%



# %% Beat
# - Scheduler
# - Cron like
# - Example: at time intervals (every 5 seconds or once a week),
# - Example: on a specific date or time (at 5:03pm every Sunday)
# %%



# %% Retry
# - https://docs.celeryq.dev/en/stable/userguide/tasks.html#automatic-retry-for-known-exceptions
# %%



# %% Reject
# - https://docs.celeryq.dev/en/stable/userguide/tasks.html#reject
# %%



# %% Security
# %%



# %% Good Practices
# %%



# %% State
# %%



# %% Further Reading
# - https://medium.com/pythonistas/a-complete-guide-to-production-ready-celery-configuration-5777780b3166
# %%



