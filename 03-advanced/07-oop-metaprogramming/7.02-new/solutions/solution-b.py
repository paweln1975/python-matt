class Account:
    def __new__(cls, username, password, uid, *args, **kwargs):
        if int(uid) < 1000:
            return SystemAccount(username)
        return UserAccount(username)


result = [Account(*records)
          for line in DATA.splitlines()
          if (records := line.split(':'))]