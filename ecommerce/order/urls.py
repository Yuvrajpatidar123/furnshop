from django.urls import path
from . import views
urlpatterns = [
    path('ordersave',views.ordersave, name='ordersave'),
    path('orderdetail',views.orderdetail, name='orderdetail'),
    path('bill/<int:Orderid>',views.bill,name='bill'),
    path('cancle/<int:Order_id>',views.cancle,name='cancle')

]