
data = []

for user in DATA:
    user = vars(user)
    groups = user.pop('groups')
    groups = [vars(x).values() for x in groups]
    groups = [','.join(map(str,x)) for x in groups]
    user['groups'] = ';'.join(groups)
    data.append(user)

result = pd.DataFrame(data)
