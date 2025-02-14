from django.http import HttpRequest
from ninja import Router
from ninja.pagination import paginate
from shop.models import Product
from shop.schemas import ProductSchema

router = Router()

@router.get('/products', response=list[ProductSchema])
@paginate
def products_list(request: HttpRequest):
    products = Product.objects.all().values('name', 'price', 'barcode')
    return list(products)