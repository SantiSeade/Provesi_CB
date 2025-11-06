from django.contrib import admin
from .models import Product, Withdrawal

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'location')

@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'motive', 'created_at')
    list_filter = ('motive', 'created_at')