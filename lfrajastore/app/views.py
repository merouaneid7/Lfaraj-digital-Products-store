from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def product_list(request):
    products = Product.objects.all().values(
        'id', 'name', 'description', 'price', 'file')
    products_list = list(products)  # Convert the QuerySet to a list
    return JsonResponse(products_list, safe=False)
