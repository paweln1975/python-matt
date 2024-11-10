
def isnumeric(*args, **kwargs):
    args += tuple(kwargs.values())

    if not args:
        raise TypeError('At least one argument is required')

    for arg in args:
        if type(arg) not in (float, int):
            return False

    return True
