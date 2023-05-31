from django.shortcuts import render
from .models import Product
# Create your views here.
def userhome(request):
    prod = Product.objects.all()
    return render(request,'userhome.html',{'prod':prod})
def prodview(request,product_id):
    prods = Product.objects.get(id=product_id)
    return render(request,'productview.html',{'prods':prods})
