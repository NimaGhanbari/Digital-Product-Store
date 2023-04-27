from django.contrib import admin
from .models import Subscription,Package


@admin.register(Package)
class Package(admin.ModelAdmin):
    list_display = ['title','sku','is_enable','price','duration']


@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = ['user','package','created_time','expaire_time']