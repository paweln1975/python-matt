from django.shortcuts import render

def index_view(request):
    return render(request, 'shop/index.html')


# File: shop/urls.py
from django.urls import path
from shop.views import index_view

urlpatterns = [
    path('shop/index', index_view, name='shop-index-fbv'),
]

# File: shop/index.html
"""
Hello World!
"""