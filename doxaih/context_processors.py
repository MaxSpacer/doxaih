from django.template.context_processors import request
from datetime import datetime
from landing.forms import CallmecontactForm
from educations.forms import EducationOrderForm
from orders.models import ProductinBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
    products_total_nmb = products_in_basket.count()
    form = CallmecontactForm(request.POST or None)
    print('here----')
    print(products_total_nmb)
    return locals()
