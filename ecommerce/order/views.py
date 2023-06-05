from django.shortcuts import render,redirect
from cart.models import Cart
from.models import Orderdetails
# Create your views here.
def ordersave(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
    
        cart = Cart.objects.all()
        for c in cart:
            productname = c.productname
            quantity = c.quantity
            price = c.price
            image = c.image
        
        totalprice = quantity*price
        order = Orderdetails(username = name,email = email,mobile = mobile,address = address,productname = productname,quantity = quantity,price = price,image = image,totalprice=totalprice)
        order.save()
        cart.delete()
        totalitem = Cart.objects.all().count()
        return render(request,'cart.html',{'totalitem':totalitem})
        # return redirect('cart')
    else:
        return redirect('cart')
def orderdetail(request):
    orderdetailsitem = Orderdetails.objects.all().count()
    orderdetails = Orderdetails.objects.all()
    totalitem = Cart.objects.all().count()
    return render(request,'orderdetail.html',{'orderdetailsitem':orderdetailsitem,'orderdetails':orderdetails,'totalitem':totalitem})

def cancle(request,Order_id):
    orderdetails = Orderdetails.objects.get(id = Order_id)
    orderdetails.delete()
    return redirect('orderdetail')

def bill(request,Orderid):
    order = Orderdetails.objects.filter(id=Orderid)
    return render(request, 'bill.html', {'order':order[0]})
