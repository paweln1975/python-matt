result, was_created = Customer.objects.get_or_create(
    firstname='John',
    lastname='Doe',
)