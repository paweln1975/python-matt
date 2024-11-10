
def check(func):
    def wrapper(*args, **kwargs):
        if not wrapper.disabled:
            return func(*args, **kwargs)
        else:
            raise PermissionError('Function is disabled')

    return wrapper
