#!/usr/bin/env python3
# https://python3.info/django/settings/caches.html


# %% Settings Caches
# - https://docs.djangoproject.com/en/stable/topics/cache/#memcached
# %%



# %% DummyCache
# - For development and testing purposes
# %%



# %% Database
# %%



# %% Filesystem
# %%



# %% Local-memory
# - Not a good choice for production environments
# - This is the default cache if another is not specified in your settings file
# - This cache is per-process (see below) and thread-safe
# - If you only have one locmem cache, you can omit the LOCATION
# - If you have more than one local memory cache, you will need to assign a name to at least one of them in order to keep them separate
# - Each process will have its own private cache instance, which means no cross-process caching is possible
# %%



# %% PyLibMCCache
# %%



# %% Redis
# %%



