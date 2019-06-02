from django.forms import ModelForm, Textarea
from .models import Order
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms.widgets import HiddenInput

class OrderForm(PopRequestMixin, CreateUpdateAjaxMixin, ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone','customer_adress','customer_comments','total_price_order','order_session_key']
        widgets = {
            'customer_comments': Textarea(attrs={'cols': 50, 'rows': 2}),
            'customer_adress': Textarea(attrs={'cols': 50, 'rows': 2}),
            'order_session_key': HiddenInput(),
        }
