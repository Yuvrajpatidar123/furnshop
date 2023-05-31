from django.urls import path
from . import views
urlpatterns = [
    path('add_to_cart/<int:product_id>',views.add_to_cart, name='add_to_cart'),
    path('cart',views.cart, name='cart'),
    path('remove/<int:cart_id>',views.remove, name='remove'),
]