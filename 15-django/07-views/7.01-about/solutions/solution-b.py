# File: shop/views.py
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'shop/index.html'


# File: shop/urls.py
from django.urls import path
from shop.views import IndexView

urlpatterns = [
    path('shop/index', IndexView.as_view(), name='shop-index-cbv'),
]

# File: shop/index.html
"""
Hello World!
"""