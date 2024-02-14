from django.contrib import admin
from .models import GeneratedSerialNumber

@admin.register(GeneratedSerialNumber)
class GeneratedSerialNumberAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'lots', 'bundle_id', 'serial_number')
    search_fields = ('product_name', 'lots', 'bundle_id', 'serial_number')
