data = []

for user in DATA:
    user = vars(user)
    for i, group in enumerate(user.pop('groups'), start=1):
        group = vars(group)
        for field,value in group.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    data.append(user)


result = pd.DataFrame(data)