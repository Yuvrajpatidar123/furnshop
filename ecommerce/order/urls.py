from django.urls import path
from . import views
urlpatterns = [
    path('ordersave',views.ordersave, name='ordersave'),
    path('orderdetail',views.orderdetail, name='orderdetail'),
    path('bill/<int:Orderid>',views.bill,name='bill'),
    # path('cart',views.cart, name='cart'),
    # path('minus_cart/<int:cart_id>',views.minus_cart,name='minus_cart'),
    # path('remove/<int:cart_id>',views.remove, name='remove'),
]