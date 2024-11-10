
def disable(func):
    def wrapper(*args, **kwargs):
        raise PermissionError('Function is disabled')

    return wrapper
