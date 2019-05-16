from django.template.context_processors import request
from datetime import datetime
from landing.forms import CallmecontactForm
from educations.forms import EducationOrderForm
from orders.models import ProductinBasket
from products.models import ProductImage

def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
    products_total_nmb = products_in_basket.count()
    form = CallmecontactForm(request.POST or None)
    # print(products_in_basket)
    popular_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__popular = True)
    print(popular_products)
    return locals()

def getting_popul_goods(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return locals()
