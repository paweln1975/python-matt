def check(func):
    def wrapper(*args, **kwargs):
        return 'hello from wrapper'
    return wrapper


def hello():
    return 'hello from function'


result = check(hello)
del check
result()