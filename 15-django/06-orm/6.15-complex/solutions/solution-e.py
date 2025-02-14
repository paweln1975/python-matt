result = (
    Order
    .objects
    .values(
        firstname=F('customer__firstname'),
        lastname=F('customer__lastname'))
    .annotate(total=Sum('products__price'))
    .order_by('-total')
    .first()
)