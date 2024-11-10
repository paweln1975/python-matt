
class Database:
    instance: Self

    @classmethod
    def connect(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        return cls.instance
