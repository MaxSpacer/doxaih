from django.contrib import admin
from .models import Callmecontact
from .models import Landpost
# from .models import Mainformcontact

# Register your models here.
#
class LandpostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Landpost._meta.fields]
    # Register the admin class with the associated model
admin.site.register(Landpost, LandpostAdmin)

class CallmecontactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Callmecontact._meta.fields]
admin.site.register(Callmecontact, CallmecontactAdmin)
