from django.http import HttpRequest
from ninja import Router
from myproject.schemas import NotFoundResponse
from shop.models import Product
from shop.schemas import ProductSchema


router = Router()

@router.get('/api/v2/shop/product', response={
    200: ProductSchema,
    404: NotFoundResponse})
def product_details(request: HttpRequest, name: str | None = None, barcode: str | None = None):
    product = Product.objects
    if name is not None:
        product = product.filter(name=name)
    if barcode is not None:
        product = product.filter(barcode=barcode)
    try:
        data = product.values('name', 'price', 'barcode')
    except Product.DoesNotExist:
        return 404, {'data': 'Product not found'}
    else:
        data = vars(product)
        data.pop('_state')
        return 200, data