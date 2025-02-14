def can_login(func):
    def wrapper(users):
        for member in users:
            if not member['is_staff']:
                username = member["username"]
                raise PermissionError(f'{username} is not a staff')
        return func(users)
    return wrapper