
def isnumeric(*args):
    if not args:
        raise TypeError('At least one argument is required')

    for arg in args:
        if type(arg) not in (int, float):
            return False

    return True
