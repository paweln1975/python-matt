
@dataclass
class Address:
    street: Optional[str]
    city: str
    post_code: Optional[int]
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: list[Address] = field(default_factory=list)
