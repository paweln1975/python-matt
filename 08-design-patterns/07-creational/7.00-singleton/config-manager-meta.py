from typing import Any

class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

class ConfigManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.settings: dict = {}

    def set(self, key: str, value: Any) -> None:
        self.settings[key] = value

    def get(self, key: str) -> Any:
        return self.settings.get(key)


manager = ConfigManager()
manager.set('name', 'Mark')

other = ConfigManager()
print(other.get('name'))
print(other.get('name'))
print(other.get('missing_key'))