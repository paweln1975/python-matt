
class Singleton:
    instance: Self

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        obj = cls.instance
        obj.__init__(*args, **kwargs)
        return obj
