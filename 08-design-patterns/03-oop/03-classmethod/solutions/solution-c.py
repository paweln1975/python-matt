
class Account:
    def __init__(self, username, password, uid, gid, gecos, home, shell):
        self.username = username
        self.password = password
        self.uid = uid
        self.gid = gid
        self.gecos = gecos
        self.home = home
        self.shell = shell

    @classmethod
    def from_passwd(cls, data: str):
        username, password, uid, gid, gecos, home, shell = data.split(':')
        return cls(username, password, int(uid), int(gid), gecos, home, shell)


class SystemAccount(Account):
    pass


class UserAccount(Account):
    pass
