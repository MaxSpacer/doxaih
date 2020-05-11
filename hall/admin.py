from django.contrib import admin
from .models import Preference

admin.site.site_header = "Администрирование DOXAIH";
admin.site.site_title = "Администрирование DOXAIH";



class PreferenceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Дополнительные настройки', {'fields': ['number_phone','is_active']}),
        # ('Дополнительные настройки', {'fields': ['created']}),
    ]
    # list_display = [field.name for field in Preference._meta.fields]
admin.site.register(Preference, PreferenceAdmin)
