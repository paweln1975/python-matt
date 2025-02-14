# myproject/shop/api.py
from http import HTTPStatus
from django.views import View
from django.http import JsonResponse
from shop.models import Product


class ProductAPI(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            data = {'details': 'Product with this pk does not exist'}
            return JsonResponse(status=HTTPStatus.NOT_FOUND, data=data)
        else:
            data = vars(product)
            data.pop('_state')
            return JsonResponse(status=HTTPStatus.OK, data=data)


# myproject/urls.py
from django.urls import path

urlpatterns = [
    path('api/v1/shop/product/<int:pk>', ProductAPI.as_view()),
]