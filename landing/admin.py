from django.contrib import admin
from .models import Callmecontact, Landpost



# class CallmecontactAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Callmecontact._meta.fields]
# admin.site.register(Callmecontact, CallmecontactAdmin)

class LandpostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Landpost._meta.fields]
admin.site.register(Landpost, LandpostAdmin)
