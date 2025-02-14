for row in ORDERS:
    email = row.pop('customer')
    name = row.pop('product')

    customer = Customer.objects.get(email=email)
    products = Product.objects.filter(name=name)

    order = Order.objects.create(customer=customer)
    order.products.set(products)
    order.save()