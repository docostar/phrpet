from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.
def home_view(request):
    return render(request, 'home/index.html')

def shop_view(request):
    return render(request, 'home/base.html')

def demo_product_view(request):
    return render(request, 'home/product_detail.html')

def product_detail(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4] 
    benefits_list = product.benefits.split(",") if product.benefits else []
    return render(request, 'home/products.html', {'product': product, 'benefits_list': benefits_list, 'related_products':related_products})
