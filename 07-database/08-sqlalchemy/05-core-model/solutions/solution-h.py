
@dataclass
class Address:
    street: str | None
    city: str
    postcode: int | float | None
    region: str
    country: str


@dataclass
class Astronaut:
    firstname: str
    lastname: str
    addresses: list[Address] | None


result = []

for row in DATA:
    addresses = [Address(**addr) for addr in row.pop('addresses')]
    user = Astronaut(**row, addresses=addresses)
    result.append(user)
