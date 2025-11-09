"""
Singleton design pattern.
Implemented as metaclass
"""

class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

class Config(metaclass=Singleton):
    host = "localhost"
    port = 3306
    user = "root"
    password = ""

config1 = Config()
config2 = Config()

print(config1 is config2)
config2.host = "localhost2"

print(config1.host)