# -*- coding: utf-8 -*-
# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from .forms import CallmecontactForm, MainForm
from .models import Callmecontact, Mainformcontact
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteMessageMixin
from products.models import *


def landing(request):
    product_category_list = ProductCategory.objects.filter(is_active=True)
    return_list = list()
    for item in product_category_list:
        product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category = item).first()
        if product_images:
            return_list.append(product_images)
    return render(request, 'landing/landing.html', {'product_category_list': product_category_list, 'product_image_list': return_list})


class CallmeCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'landing/create_callme.html'
    form_class = CallmecontactForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        if 'referer' in self.request.session:
            referer_id = self.request.session['referer']
            user = User.objects.get(pk=referer_id)
            # form.instance.referal = user.profile
            form.instance.referal = user.profile
        return super(CallmeCreateView, self).form_valid(form)


class MainFormView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'landing/landing.html'
    form_class = MainForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
    success_url = reverse_lazy('main_form')
    # success_url = reverse_lazy('main' + '#id_form_footer')
    # def get_success_url(self):
        # educations_pk=self.kwargs['pk']
    #     return reverse_lazy('main' + '#id_form_footer')

    def form_valid(self, form):
        if 'referer' in self.request.session:
            referer_id = self.request.session['referer']
            user = User.objects.get(pk=referer_id)
            # form.instance.referal = user.profile
            form.instance.referal = user.profile

        return super(MainFormView, self).form_valid(form)