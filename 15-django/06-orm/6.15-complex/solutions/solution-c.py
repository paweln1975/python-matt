result = (
    Order
    .objects
    .values(country=F('customer__address__country'))
    .annotate(count=Count('products__price'))
    .order_by('-count')
    .first()
)