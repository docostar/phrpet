from django.contrib import admin
from .models import Category, Product, ProductImage, FAQ, Testimonial, Slider


# Change site header and title
admin.site.site_header = "PHR Admin"
admin.site.site_title = "PHR Admin Portal"
admin.site.index_title = "Welcome to PHR Admin"

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

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('question', 'answer')
    ordering = ('-created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'clinic_name', 'doctor_city', 'created_at')  # Fields displayed in the admin list
    list_filter = ('doctor_city', 'created_at')  # Filters for admin interface
    search_fields = ('doctor_name', 'clinic_name', 'doctor_city')  # Searchable fields
    ordering = ('-created_at',)  # Order testimonials by creation date (newest first)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

