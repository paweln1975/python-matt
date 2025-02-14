for row in ADDRESSES:
    email = row.pop('customer')
    customer = Customer.objects.get(email=email)
    address = Address.objects.create(customer=customer, **row)