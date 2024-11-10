
def mydecorator(method):
    def wrapper(self, *args, **kwargs):
        return method(self, *args, **kwargs)

    return wrapper
