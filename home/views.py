from django.shortcuts import render,get_object_or_404
from .models import Product,Category,FAQ,Testimonial,Slider
from random import shuffle
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.db.models import Count

# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    faqs = FAQ.objects.filter(is_active=True)  # Fetch only active FAQ
    testimonials = Testimonial.objects.filter(is_active=True)  # Fetch only active testimonials
    sliders = Slider.objects.all()
    return render(request, 'home/index.html',{'categories': categories,'faqs':faqs,'testimonials':testimonials,'sliders':sliders})

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
    benefits_list = product.benefits.split(".") if product.benefits else []
    composition_list = product.composition.split(",") if product.composition else []
    return render(request, 'home/products.html', {'product': product, 'benefits_list': benefits_list, 'related_products':related_products,'composition_list':composition_list})

def categories_view(request,category_id):
    categories = Category.objects.all()
    Category.objects.annotate(product_count=Count('products'))
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'home/category.html',{'categories': categories,'category':category})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Compose email
            subject = f"New Contact Form Submission: {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            from_email = 'matrufinancial@gmail.com'  # Your Gmail address
            recipient_list = ['rahulbusiness2012@gmail.com'] # Replace with the desired recipient email

            try:
                send_mail(
                    subject,
                    full_message,
                    from_email,
                    recipient_list,  
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, f"Failed to send your message: {str(e)}")
                
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


def send_email_view(request):
    subject = 'Hello from Django'
    message = 'Djngo Testing.'
    from_email = 'matrufinancial@gmail.com'  # Your Gmail address
    recipient_list = ['rahulbusiness2012@gmail.com','rokanmitra@gmail.com']  # Change to the recipient's email

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')

def blog_view(request):
    return render(request, 'home/blog.html')

def about_view(request):
    return render(request, 'home/about.html')