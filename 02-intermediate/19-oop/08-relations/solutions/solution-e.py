
class Address:
    def __init__(self, street, city, postcode, region, country):
        self.street = street
        self.city = city
        self.postcode = postcode
        self.region = region
        self.country = country

    def __repr__(self):
        city = self.city
        country = self.country
        return f"Address('{city}', '{country}')"


class User:
    def __init__(self, firstname, lastname, addresses):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses = addresses

    def __repr__(self):
        firstname = self.firstname
        lastname = self.lastname
        addresses = self.addresses
        return f"User('{firstname}', '{lastname}', addresses={addresses})"


def convert(user):
    addresses = user.pop('addresses')
    addresses = [Address(**x) for x in addresses]
    return User(**user, addresses=addresses)


result = map(convert, DATA)
