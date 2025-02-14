mark = Q(firstname='Mark', lastname='Watney')
melissa = Q(firstname='Melissa', lastname='Lewis')
query = mark | melissa

result = Customer.objects.filter(query)