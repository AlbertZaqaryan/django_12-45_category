from django.contrib import admin
from .models import Category, Product
# Register your models here.


admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['id', 'name']
    search_fields = ['name']