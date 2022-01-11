from django.contrib import admin
from .models import Order, OrderItem, PaymentUpload

# Register your models here.
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

@admin.register(PaymentUpload)
class PaymentUploadAdmin(admin.ModelAdmin):
    list_display = ['orderItem', 'payment_date', 'amount_paid']
    list_filter = ['payment_date']