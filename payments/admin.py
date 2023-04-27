from django.contrib import admin
from .models import Gateway,Payment

@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable']
    
@admin.register(Payment)    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','package','gateway','phone_number','status']
    list_filter = ['status','gateway','package']
    search_fields = ['phone_number']
