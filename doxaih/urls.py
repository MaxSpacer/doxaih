"""doxaih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from filebrowser.sites import site
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('nested_admin/', include('nested_admin.urls')),
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('', include('landing.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ref/', include('referals.urls')),
    path('posts/', include('modposting.urls')),
    path('events/', include('events.urls')),
    path('educations/', include('educations.urls')),
    path('investions/', include('investions.urls')),
    path('basket_adding/', include('orders.urls')),
    # path('checkout/', include('checkout.urls')),
    path('hall/', include('hall.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('contacts/', include('contacts.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
