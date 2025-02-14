@dataclass
class User:
    firstname: str
    lastname: str
    since: datetime = field(default_factory=datetime.now)