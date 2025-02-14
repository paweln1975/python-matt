# myproject/shop/api.py
from http import HTTPStatus
from django.views import View
from django.http import JsonResponse
from shop.models import Product

class ProductAPI(View):
    ...

# myproject/urls.py
from django.urls import path

urlpatterns = [
    path('api/v1/shop/product', ProductAPI.as_view()),
]