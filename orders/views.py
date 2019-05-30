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
    # for item in products_in_basket:


    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = list()
    products_in_basket_total_price = 0
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["product_name"] = item.pb_product.name
        product_dict["price_per_item"] = item.pb_price_per_item
        product_dict["numb"] = item.pb_qty
        products_in_basket_total_price += item.pb_total_price
        # product_dict["products_in_basket_total_price"] = item.pb_total_price
        return_dict["products"].append(product_dict)

    return_dict["products_in_basket_total_price"] = products_in_basket_total_price
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
    # success_url = reverse_lazy('landing:landing')

    def get_success_url(self):
        # investions_pk=self.kwargs['pk']
        print('safaf')
        print(self.object.id)
        print(self.object)
        session_key = self.request.session.session_key
        products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
        self.object.save()
        for item in products_in_basket:
            print(item)
            item.pb_order = self.object
            print(item.pb_order)

            item.save()
        # ,args=(self.object.id,)
        # r_id = self.request.session
        # session_key = self.session.session_key
        # print(r_id)
        # products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)

        return reverse_lazy('landing:landing')

    def form_valid(self, form):
        print('prefaf')
        print(self)
        print(form)

        # form.instance.investion = investion

        return super(OrderCreateView, self).form_valid(form)
    # def form_valid(self, form):
    #     if 'referer' in self.request.session:
    #         referer_id = self.request.session['referer']
    #         user = User.objects.get(pk=referer_id)
    #         # form.instance.referal = user.profile
    #         form.instance.referal = user.profile
    #     investion = get_object_or_404(Investion,pk=self.kwargs['pk'])
    #     form.instance.investion = investion
# def checkout(request):
#     products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
#     return render(request, 'checkout/checkout.html', locals())
