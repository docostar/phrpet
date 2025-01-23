from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from random import shuffle

# Create your views here.
def home_view(request):
    return render(request, 'home/index.html')

def home2_view(request):
    return render(request, 'Petco/index.html')

def shop_view(request):
    return render(request, 'home/base.html')

def demo_product_view(request):
    return render(request, 'home/product_detail.html')

def product_detail(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    # If less than 4 related products, include random products from other categories
    if len(related_products) < 4:
        excluded_ids = [p.id for p in related_products] + [product.id]  # Exclude current product and already related products
        other_products = list(Product.objects.exclude(id__in=excluded_ids))  # Convert to list explicitly
        shuffle(other_products)  # Shuffle for randomness
        related_products = list(related_products) + other_products[:4 - len(related_products)]  # Safely combine lists
    benefits_list = product.benefits.split(",") if product.benefits else []
    return render(request, 'home/products.html', {'product': product, 'benefits_list': benefits_list, 'related_products':related_products})

def categories_view(request,category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'home/category.html',{'categories': categories,'category':category})
