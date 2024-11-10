#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/asyncio/about.html

#%% AsyncIO About
# asyncio in Python standard library
# async and await builtin keywords
# Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]
# Async is the future of programming



#%% Advantages
# Maximize the usage of a single thread
# Handling I/O asynchronously
# Enabling concurrent code using coroutines
# Async will fill the gaps, otherwise wasted on waiting for I/O
# You control when tasks switches occur, so locks and other synchronization are no longer needed
# Async is the cheapest way to task switch
# Cost task switches is incredibly low; calling a pure Python function has more overhead than restarting a generator or awaitable
# Function builds stack each time it's called, whereas async uses generators underneath, which already has stack created
# In terms of speed async servers blows threaded servers in means of thousands
# Async is very cheap in means of resources
# Async world has a huge ecosystem of support tools
# Coding is easier to get right, than threads



#%% Disadvantages
# Async switches cooperatively, so you do need to add explicit code yield or await to cause a task to switch
# Everything you do need a non-blocking version (for example open())
# Increased learning curve
# Create event loop, acquire, crate non-blocking versions of your code
# You think you know Python, there is a second half to learn (async)



#%% Sync vs Async



#%% Execution



#%% Further Reading
# Kennedy, M. Demystifying Python's Async and Await Keywords [#Kennedy2019]_
# Kennedy, M. Async Techniques and Examples in Python [#Kennedy2022]_
# Abdalla, A. Creating a Bittorrent Client using Asyncio [#Abdalla2017]_
# Langa, Ł. import asyncio: Learn Python's AsyncIO [#Langa2020]_