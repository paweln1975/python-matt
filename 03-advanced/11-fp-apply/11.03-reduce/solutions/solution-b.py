def myreduce(function, iterable):
    if len(iterable) == 1:
        return iterable[0]
    *head, tail = iterable
    return function(myreduce(function,head), tail)


# %% Alternatively
def myreduce(function, iterable):
    if len(iterable) == 1:
        return iterable[0]
    result = myreduce(function, iterable[:-1])
    last = iterable[-1]
    return function(result, last)