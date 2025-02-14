result = (
    Order
    .objects
    .values(
        firstname=F('customer__firstname'),
        lastname=F('customer__lastname'))
    .annotate(
        name=Concat('firstname', Value(' '), 'lastname'),
        orders=Count('customer'))
    .order_by('-orders')
    .values('name', 'orders')
    .first()
)