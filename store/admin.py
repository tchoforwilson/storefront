from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>10', 'High'),
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if(self.value() == '<10'):
            return queryset.filter(inventory__lt=10)
        if(self.value() == '>10'):
            return queryset.filter(inventory__gt=10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price','inventory_status', 'collection']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = [ 'first_name__istartswith', 'last_name__istartswith']
    
admin.site.register(models.Collection)
