
def abspath(func):
    def wrapper(relpath):
        abspath = Path(relpath).absolute()
        return func(abspath)
    return wrapper
