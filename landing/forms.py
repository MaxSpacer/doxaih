# Django
from django import forms
# Project
from .models import Callmecontact
# from .models import Mainformcontact
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CallmecontactForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Callmecontact
        fields = ['customer_name', 'customer_phone']


# class MainForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
#     class Meta:
#         model = Mainformcontact
#         fields = ['customer_name', 'customer_phone','customer_email']
