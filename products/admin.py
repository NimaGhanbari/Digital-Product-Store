from django.contrib import admin

from .models import Category,Products,File


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ['parent','title','description','is_enable','create_time']
    list_filter = ['is_enable','parent']
    search_fields = ['title']

class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','fil','is_enable','file_type']
    extra = 0
  
@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['title','is_enable','create_time']
    list_filter = ['create_time']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInLineAdmin]

"""@admin.register(File)
class FileInLineAdmin(admin.ModelAdmin):
    list_display = ['title','fil','is_enable','file_type']"""