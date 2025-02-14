result = (
    Order
    .objects
    .values(product_name=F('products__name'))
    .annotate(orders=Count('customer'))
    .order_by('-orders')
    .first()
)