
class Account:
    def __new__(cls, line):
        records = line.split(':')
        username = records[0]
        uid = int(records[2])
        if uid < 1000:
            return SystemAccount(username, uid)
        else:
            return UserAccount(username, uid)


result = [Account(line) for line in DATA.splitlines()]
