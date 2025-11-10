class Borg(object):
    _state: dict = {}
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__ = cls._state
        return instance

class Config(Borg):
    def __init__(self, value = None):
        if not value is None:
            self.value = value


a = Config('localhost')

b = Config()
print(b.value)