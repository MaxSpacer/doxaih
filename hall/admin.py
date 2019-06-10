from django.contrib import admin
from .models import Preference


class PreferenceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Preference._meta.fields]
admin.site.register(Preference, PreferenceAdmin)
