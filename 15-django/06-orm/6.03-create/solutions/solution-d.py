result = Customer.objects.bulk_create([
    Customer(firstname='John', lastname='Doe'),
    Customer(firstname='Jane', lastname='Doe'),
])