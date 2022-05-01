from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from order.models import OrderItem, Order

"""
Extending the administration site with custom views
"""


def order_detail(obj):
    url = reverse('order:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'email', 'address', 'postal_code',
                    'city', 'paid', 'created_on', 'updated',
                    order_detail]

    list_filter = ['paid', 'created_on', 'updated']
    inlines = [OrderItemInline]
