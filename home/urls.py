from django.urls import path
from .views import home_view,shop_view,product_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('shop',shop_view , name='shop'),
    path('product/<int:product_id>/', product_detail, name='product_detail')
]
