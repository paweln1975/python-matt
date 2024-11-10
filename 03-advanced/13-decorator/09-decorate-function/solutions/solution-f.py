
def typecheck(func):

    def wrapper(*args, **kwargs):
        arguments = kwargs | dict(zip(func.__code__.co_varnames, args))
        for argname, argvalue in arguments.items():
            validate(argname, argvalue)
        result = func(*args, **kwargs)
        validate('return', result)
        return result

    def validate(argname, argvalue):
        argtype = type(argvalue)
        expected = func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')

    return wrapper
