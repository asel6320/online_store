from django.contrib import admin

# Register your models here.
from webapp.models import Product, Category

admin.site.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['title', 'category']
    search_fields = ['title', 'price', 'category']
    fields = ['title', 'description', 'category', 'created_at', 'price', 'image_url', 'remainder']
    readonly_fields = ['created_at']
# Register your models here.
admin.site.register(Product, ProductAdmin)