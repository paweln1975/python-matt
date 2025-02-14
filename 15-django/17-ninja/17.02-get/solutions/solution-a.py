from django.http import HttpRequest
from ninja import Router
from myproject.schemas import NotFoundResponse
from shop.models import Product
from shop.schemas import ProductSchema

router = Router()

@router.get('/product/{pk}', response={
    200: ProductSchema,
    404: NotFoundResponse})
def product_details(request: HttpRequest, pk: int):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return 404, {'data': 'Product not found'}
    else:
        data = vars(product)
        data.pop('_state')
        return 200, data