
def cache(func):
    def wrapper(n):
        if n not in _cache:
            _cache[n] = func(n)
        return _cache[n]

    return wrapper
