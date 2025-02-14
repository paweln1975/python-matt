class UserPermissions:
    pass

class AdminPermissions:
    pass

class Account(UserPermissions, AdminPermissions):
    pass