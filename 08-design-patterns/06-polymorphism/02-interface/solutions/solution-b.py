
class User(Account):
    username: str
    password: str

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login(self) -> str:
        return 'User login'

    def logout(self) -> str:
        return 'User logout'
