from django.contrib import admin
from .models import Order, OrderItem, PaymentUpload
import csv, datetime
from django.http import HttpResponse

# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class PaymentUploadInline(admin.TabularInline):
    model = PaymentUpload

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_price', 'email', 'phone', 'address', 'lga', 'paid', 'created']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline, PaymentUploadInline]
    actions = [export_to_csv]

@admin.register(PaymentUpload)
class PaymentUploadAdmin(admin.ModelAdmin):
    list_display = ['orderItem', 'payment_date', 'amount_paid']
    list_filter = ['payment_date']