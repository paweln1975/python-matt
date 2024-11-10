
def convert(user: dict):
    for i, mission in enumerate(user.pop('groups'), start=1):
        for field,value in mission.items():
            column_name = f'group{i}_{field}'
            user[column_name] = value
    return user


result = map(convert, DATA)
