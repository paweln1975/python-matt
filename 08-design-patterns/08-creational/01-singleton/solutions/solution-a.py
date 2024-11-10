

class Settings:
    instance: Self

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        return cls.instance
