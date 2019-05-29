from django.http import JsonResponse
from .models import ProductinBasket
# from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import OrderForm
from django.contrib import messages


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    numb = data.get("numb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductinBasket.objects.filter(id=product_id).update(pb_is_active=False)
        return_dict["is_delete"] = 'true'
    else:
        new_product, created = ProductinBasket.objects.get_or_create(pb_session_key=session_key, pb_product_id=product_id, pb_is_active=True, defaults={"pb_qty": numb})
        messages.add_message(request, messages.INFO, 'Товар в корзине')
        if not created:
            print ("not created")
            new_product.pb_qty += int(numb)
            new_product.save(force_update=True)

    products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
    products_total_nmb = products_in_basket.count()

    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["product_name"] = item.pb_product.name
        product_dict["price_per_item"] = item.pb_price_per_item
        product_dict["numb"] = item.pb_qty
        product_dict["numb"] = item.pb_qty
        return_dict["products"].append(product_dict)

    return_dict["messages"] = []
    for message in messages.get_messages(request):
        return_dict["messages"].append({
            "level": message.level,
            "message": message.message,
            "extra_tags": message.tags,
    })
    return JsonResponse(return_dict)


class OrderCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'orders/create_order.html'
    form_class = OrderForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
    success_url = reverse_lazy('landing:landing')

    def get_success_url(self):
        # investions_pk=self.kwargs['pk']
        print('safaf')
        return reverse_lazy('landing:landing')


    # def form_valid(self, form):
    #     if 'referer' in self.request.session:
    #         referer_id = self.request.session['referer']
    #         user = User.objects.get(pk=referer_id)
    #         # form.instance.referal = user.profile
    #         form.instance.referal = user.profile
    #     investion = get_object_or_404(Investion,pk=self.kwargs['pk'])
    #     form.instance.investion = investion
    #     return super(MainFormView, self).form_valid(form)
# def checkout(request):
#     products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
#     return render(request, 'checkout/checkout.html', locals())
