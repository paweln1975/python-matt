class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    pass

class Settings(metaclass=Singleton):
    pass


db1 = Database()
db2 = Database()

set1 = Settings()
set2 = Settings()

print(db1 is db2)
print(set1 is set2)