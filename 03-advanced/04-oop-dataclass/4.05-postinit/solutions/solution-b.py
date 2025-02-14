@dataclass
class User:
    firstname: str
    lastname: str
    role: str
    username: str
    password: str
    email: str
    birthdate: date
    last_login: datetime | None
    is_active: bool
    is_staff: bool
    is_superuser: bool
    user_permissions: list[dict]

    def __post_init__(self):
        if isinstance(self.birthdate, str):
            self.birthdate = date.fromisoformat(self.birthdate)
        if isinstance(self.last_login, str):
            self.last_login = datetime.fromisoformat(self.last_login)