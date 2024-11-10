
def mydecorator(cls):
    class Wrapper(cls):
        __doc__ = cls.__doc__
        __name__ = cls.__name__

    return Wrapper
