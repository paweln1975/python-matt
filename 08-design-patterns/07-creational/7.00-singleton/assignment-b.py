"""
Singleton design pattern.
Implemented with get_instance class method
"""

class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Config(Singleton):
    host = "localhost"
    port = 3306
    username = "root"
    password = ""

config1 = Config.get_instance()
config2 = Config.get_instance()

print(config1 is config2)
config2.host = "localhost1"

print(config1.host)
