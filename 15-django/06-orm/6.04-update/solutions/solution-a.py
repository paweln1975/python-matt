result = Customer.objects.get(firstname='John', lastname='Doe')
result.firstname = 'Jane'
result.save()