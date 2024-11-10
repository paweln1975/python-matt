
@dataclass
class Address:
    street: str
    city: str
    postcode: int
    region: str
    country: str


@dataclass
class User:
    firstname: str
    lastname: str
    addresses: list[Address]
