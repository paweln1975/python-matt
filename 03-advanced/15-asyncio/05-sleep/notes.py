#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/asyncio/sleep.html

#%% AsyncIO Sleep
# Coroutine asyncio.sleep(delay, result=None)
# Delay can be int or float
# Block for delay seconds.
# If result is provided, it is returned to the caller when the coroutine completes
# Delay is not guaranteed
# It means that this is at least X number of seconds
# This us due, that after that time of delay, there might still be an other function running
# This does not interrupt or preempt