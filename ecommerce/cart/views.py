from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart
# Create your views here.
def add_to_cart(request, product_id):
    # productname = Product.objects.get(id=product_id)
    product = Product.objects.filter(id=product_id)
    for p in product:
        productname = p.product_name
        price = p.price
        image = p.image
        try:
            cart = Cart.objects.get(productname=productname)
            return redirect('cart')
        except:
            cart=Cart(productname=productname, price=price,image=image)
            cart.save()
            return redirect('userhome')
    
def cart(request):
    totalitem = Cart.objects.all().count()
    cart = Cart.objects.all()
    return render(request,'cart.html',{'cart':cart,'totalitem':totalitem})

def remove(request,cart_id):
    c = Cart.objects.get(id = cart_id)
    c.delete()
    return redirect('cart')