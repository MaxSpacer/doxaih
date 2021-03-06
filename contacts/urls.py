from django.views.generic import ListView
from django.urls import path
from .models import Contacts

app_name = 'contacts'

urlpatterns = [
        path('', ListView.as_view(queryset=Contacts.objects.filter(is_active=True).order_by("order_render"),template_name="contacts/contacts.html"), name='n_contacts'),
]
