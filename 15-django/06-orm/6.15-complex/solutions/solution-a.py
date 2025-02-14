result = (
    Order.objects
    .filter(customer__gender='female')
    .values('products__price')
    .aggregate(total=Sum('products__price'))
)