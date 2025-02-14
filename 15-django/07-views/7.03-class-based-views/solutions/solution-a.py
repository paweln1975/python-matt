from django.views.generic import ListView
from shop.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'shop/product-list.html'
    context_object_name = 'products'