from django.shortcuts import render
from shop.models import Product


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/product-detail.html', {
        'product': product,
    })