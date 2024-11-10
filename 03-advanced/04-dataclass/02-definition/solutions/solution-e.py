
@dataclass
class User:
    firstname: str
    lastname: str
    age: int
    AGE_MIN: ClassVar[int] = 18
    AGE_MAX: ClassVar[int] = 65
