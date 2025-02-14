#!/usr/bin/env python3
# https://python3.info/advanced/async-asyncio/queue.html


# %% AsyncIO Queue
# - asyncio queues are designed to be similar to classes of the queue module.
# - Although asyncio queues are not thread-safe, they are designed to be used specifically in async/await code.
# - Note that methods of asyncio queues don't have a timeout parameter; use asyncio.wait_for() function to do queue operations with a timeout.
# %%



# %% FIFO Queue
# - FIFO Queue - First In, First Out
# - class asyncio.Queue(maxsize=0)
# - If maxsize is less than or equal to zero, the queue size is infinite.
# - Unlike the standard library threading queue, the size of the queue is always known and can be returned by calling the qsize() method.
# - maxsize - Number of items allowed in the queue.
# - empty() - Return True if the queue is empty, False otherwise.
# - full() - Return True if there are maxsize items in the queue.
# - coroutine get() - Remove and return an item from the queue. If queue is empty, wait until an item is available.
# - get_nowait() - Return an item if one is immediately available, else raise QueueEmpty.
# - coroutine join() - Block until all items in the queue have been received and processed.
# - coroutine put(item) - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# - put_nowait(item) - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# - qsize() - Return the number of items in the queue.
# - task_done() - Indicate that a formerly enqueued task is complete.
# %%



# %% Priority Queue
# - class asyncio.PriorityQueue
# - Retrieves entries in priority order (lowest first).
# - Entries are typically tuples of the form (priority_number, data).
# %%



# %% LIFO Queue
# - LIFO Queue - Last In, First Out
# - class asyncio.LifoQueue
# - Retrieves most recently added entries first.
# %%



# %% Exceptions
# - exception asyncio.QueueEmpty - Raised when get_nowait() method is called on an empty queue.
# - exception asyncio.QueueFull - Raised when put_nowait() method is called on a queue that has reached its maxsize.
# %%



