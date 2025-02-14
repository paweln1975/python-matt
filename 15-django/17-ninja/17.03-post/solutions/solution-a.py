from django.http import HttpRequest
from ninja import Router
from myproject.schemas import CreatedResponse, BadRequestResponse
from shop.models import Product
from shop.schemas import ProductSchema


router = Router()


@router.post('/product', response={
    201: CreatedResponse,
    400: BadRequestResponse})
def product_create(request: HttpRequest, product: ProductSchema):
    try:
        Product.objects.create(**product.dict())
        return 201, {'data': 'Product created'}
    except Exception as error:
        return 400, {'data': str(error)}