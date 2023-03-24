from django.contrib import admin
from .models import Order, OrderItem, Status, PunkVidachi

class StatusAdmin(admin.ModelAdmin):
    list_display = ['pk','name']

class PunkVidachiAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',
                    'punkt', 'status',
                    'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(PunkVidachi, PunkVidachiAdmin)