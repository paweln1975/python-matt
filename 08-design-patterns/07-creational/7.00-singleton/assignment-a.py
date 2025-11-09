"""
Singleton design pattern.
Implemented with __new__
"""

class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

class Config(Singleton):
    def __init__(self, host="localhost", port=3306, username="root", password=""):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

config1 = Config()
config2 = Config()
config3 = Config(host='localhost', port=3306, username='mwatney', password='newsecret')


print(config1 is config2)
print(config1.password)
