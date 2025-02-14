def can_login(field, value):
    def decorator(func):
        def wrapper(users):
            for member in users:
                if member.get(field) != value:
                    name = member["username"]
                    raise PermissionError(f'{name} is not a staff')
            return func(users)
        return wrapper
    return decorator