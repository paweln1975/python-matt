result = (
    Order
    .objects
    .values(country=F('customer__address__country'))
    .annotate(total=Sum('product__price'))
    .order_by('-total')
    .first()
)