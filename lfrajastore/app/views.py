from django.http import JsonResponse
from .models import Product


def product_list(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price,
             'file': product.file.url} for product in products]
    return JsonResponse(data, safe=False)
