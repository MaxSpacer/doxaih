

from django.urls import path
from . import views
from django.views.generic import ListView
from .models import Landpost

app_name = 'landing'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('create/', views.CallmeCreateView.as_view(), name='create_callme'),
]
