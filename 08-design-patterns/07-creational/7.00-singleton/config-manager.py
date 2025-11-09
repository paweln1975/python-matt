from typing import Any


class ConfigManager:
    settings: dict[str, Any]
    instance: ConfigManager | None = None

    def __init__(self) -> None:
        self.settings = {}

    @classmethod
    def get_instance(cls) -> 'ConfigManager':
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.__init__()
        return cls.instance

    def set(self, key: str, value: Any) -> None:
        self.settings[key] = value

    def get(self, key: str) -> Any:
        return self.settings.get(key)


manager = ConfigManager.get_instance()
manager.set('name', 'Mark')

other = ConfigManager.get_instance()
print(other.get('name'))
print(other.get('name'))
print(other.get('missing_key'))


