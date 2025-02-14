from django.views.generic import DetailView
from shop.models import Product


class ProductDetails(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product'