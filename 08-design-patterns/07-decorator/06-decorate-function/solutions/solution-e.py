
def numeric(func):
    def wrapper(a, b):
        if type(a) not in (int, float):
            raise TypeError('Argument "a" must be int or float')
        if type(b) not in (int, float):
            raise TypeError('Argument "b" must be int or float')
        return func(a, b)
    return wrapper
