from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('home2', home2_view, name='home2'),
    path('shop',shop_view , name='shop'),
    path('contact',contact_view , name='contact'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('demo', demo_product_view, name='demo'),
    path('category/<int:category_id>', categories_view, name='category'),
    path('send-email/', send_email_view, name='send_email'),
    path('blog/', blog_view, name='blog'),
    path('about/', about_view, name='about'),
]
