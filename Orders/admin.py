from django.contrib import admin
from .models import *
import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
    export_to_csv.short_description = 'Export to CSV'

# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billing_first_name', 'billing_last_name', 'email',
    'billing_address_2', 'billing_zip', 'billing_city',
    'timestamp', 'updated']
    list_filter = ['timestamp', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'shipping_first_name', 'shipping_last_name',
    'shipping_address_2', 'shipping_zip', 'shipping_city',
    'timestamp', 'updated']
    list_filter = ['timestamp', 'updated']