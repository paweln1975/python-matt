
def abspath(func):
    def wrapper(path):
        path = Path(path).absolute()
        return func(path)

    return wrapper
