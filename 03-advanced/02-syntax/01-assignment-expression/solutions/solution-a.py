
result = [username
          for row in DATA.splitlines()
          if (values := row.strip().split(':'))
          and (username := values[0])
          and (uid := values[2])
          and int(uid) < 1000]
