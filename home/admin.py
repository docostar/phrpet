from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class ProductImageInline(admin.TabularInline):  # Inline for managing images in Product admin
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'mrp', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'composition', 'benefits')
    inlines = [ProductImageInline]
