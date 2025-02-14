@dataclass
class Pet:
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tag]
    status: str