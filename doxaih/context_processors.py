from django.template.context_processors import request
from datetime import datetime
from landing.forms import CallmecontactForm
from educations.forms import EducationOrderForm
from orders.models import ProductinBasket
from products.models import ProductImage
from django.contrib import messages

def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
    print(products_in_basket)
    print('products_in_basket')
    products_total_nmb = products_in_basket.count()
    products_in_basket_total_price = 0
    for item in products_in_basket:
        products_in_basket_total_price += item.pb_total_price
    print(products_in_basket_total_price)
    form = CallmecontactForm(request.POST or None)
    popular_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__popular = True)
    return locals()
