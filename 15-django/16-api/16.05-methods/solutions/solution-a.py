# myproject/shop/api.py
class ProductListAPI(View):
    def get(self, request, *args, **kwargs):
        products = list(Product.objects.values('pk', 'name', 'ean13', 'price'))
        return JsonResponse(status=HTTPStatus.OK, data=products, safe=False)


# myproject/urls.py
from django.urls import path

urlpatterns = [
    path('api/v1/shop/product', ProductListAPI.as_view()),
]