
class Account:
    def __new__(cls, records):
        username, _, uid, *_ = records.split(':')
        uid = int(uid)
        if uid < 1000:
            return SystemAccount(username, uid)
        else:
            return UserAccount(username, uid)


# Parse DATA and convert to UserAccount or SystemAccount
# type: list[Account]
result = map(Account, DATA.splitlines())
