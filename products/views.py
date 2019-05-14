from django.shortcuts import render
from products.models import *


def product(request, pk):
    products = Product.objects.filter(is_active=True, category__id=pk)
    product_category_list = ProductCategory.objects.filter(is_active=True)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'products/products.html', locals())
