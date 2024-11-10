
def convert(user: dict) -> User:
    return User(
        firstname=user['firstname'],
        lastname=user['lastname'],
        addresses=[Address(**x) for x in user['addresses']]
    )

result = map(convert, DATA)


#%% Alternative Solution
from itertools import starmap

def convert(user: dict) -> User:
    addresses = map(dict.values, user.pop('addresses'))
    addresses = starmap(Address, addresses)
    return User(**user, addresses=list(addresses))
