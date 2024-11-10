#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/datetime/timestamp.html

#%% Datetime Timestamp



#%% What is timestamp?
# Seconds since midnight of January 1st, 1970 (1970-01-01 00:00:00 UTC)
# Unix era, also known as "epoch"
# In most systems represented as 32-bit integer
# Max value is 2,147,483,647 (2038-01-19 03:14:07 UTC)
# Min value is -2,147,483,647 (1901-12-13 20:45:52 UTC)
# If you add 1 to max value, you will get overflow to min value
# Linux kernel 5.6 (released 29 March 2020) has a fix for this problem so that 32-bit systems can run beyond the year 2038
# https://itsfoss.com/linux-kernel-5-6/
# https://lore.kernel.org/lkml/CAHk-=wi9ZT7Stg-uSpX0UWQzam6OP9Jzz6Xu1CkYu1cicpD5OA@mail.gmail.com/
# https://en.wikipedia.org/wiki/Year_2038_problem
# Excel error: https://learn.microsoft.com/en-US/office/troubleshoot/excel/wrongly-assumes-1900-is-leap-year



#%% Get current timestamp



#%% Convert timestamp to ``datetime``