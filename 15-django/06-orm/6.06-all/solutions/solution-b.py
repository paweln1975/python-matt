result = []

for customer in Customer.objects.all():
    result.append(customer.lastname)