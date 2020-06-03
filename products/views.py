from django.shortcuts import render
from products.models import *


def product(request, pk):
    products = Product.objects.filter(is_active=True, category__id=pk).order_by('order_sort')
    product_category_list = ProductCategory.objects.filter(is_active=True).order_by('order_sort')
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'products/products.html', locals())
