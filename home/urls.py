from django.urls import path
from .views import home_view,shop_view,product_detail,demo_product_view,categories_view,home2_view,contact_view, send_email_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home2', home2_view, name='home2'),
    path('shop',shop_view , name='shop'),
    path('contact',contact_view , name='contact'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('demo', demo_product_view, name='demo'),
    path('category/<int:category_id>', categories_view, name='category'),
    path('send-email/', send_email_view, name='send_email'),
]
