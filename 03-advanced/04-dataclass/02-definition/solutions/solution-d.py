
@dataclass
class Pet:
    id: int
    category: dict
    name: str
    photoUrls: list[str]
    tags: list[dict]
    status: str
