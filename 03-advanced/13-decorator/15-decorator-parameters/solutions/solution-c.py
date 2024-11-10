
def typecheck(check_return):
    def decorator(func):
        annotations = get_annotations(func)

        def merge(args, kwargs) -> dict:
            args = dict(zip(annotations, args))
            return args | kwargs

        def check(argname, argvalue):
            argtype = type(argvalue)
            expected = annotations[argname]
            if argtype is not expected:
                raise TypeError(f'"{argname}" is {argtype}, '
                                f'but {expected} was expected')

        def wrapper(*args, **kwargs):
            arguments = merge(args, kwargs).items()
            for argname, argvalue in arguments:
                check(argname, argvalue)
            result = func(*args, **kwargs)
            if check_return:
                check('return', result)
            return result

        return wrapper
    return decorator

