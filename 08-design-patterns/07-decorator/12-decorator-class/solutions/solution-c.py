
class TypeCheck:
    def __init__(self, func):
        self.func = func
        self.annotations = get_annotations(func)

    def merge(self, args, kwargs):
        args = dict(zip(self.annotations, args))
        return args | kwargs

    def check(self, argname, argvalue):
        argtype = type(argvalue)
        expected = self.annotations[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')

    def __call__(self, *args, **kwargs):
        arguments = self.merge(args, kwargs).items()
        for argname, argvalue in arguments:
            self.check(argname, argvalue)
        result = self.func(*args, **kwargs)
        self.check('return', result)
        return result
