from django.contrib import admin
from .models import ContactUs, Product

# Register your models here.
@admin.register(Product)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price')
    list_filter = ('category', 'price', 'quantity')
    search_fields = ('name', 'description')
    ordering = ('category', 'price')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'date',)
	search_fields = ('name', 'email',)
	date_hierarchy = 'date'
