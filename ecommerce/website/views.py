from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Contact
from cart.models import Cart
# Create your views here.
def index(request):
    # num = Cart.objects.all().count
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def signin(request):
    return render(request,'signin.html')
def contactus(request):
    return render(request,'contactus.html')
def signuppage(request):
    if request.method=='POST':

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        usname = request.POST['username']
        pas = request.POST['password']

        try:
            user=User.objects.get(username=usname)
            return render(request,'signup.html')
            
        except:
            user = User.objects.create_user(first_name = fname,last_name = lname, username = usname, email = email, password = pas)
            user.save()
            return redirect('signin')
    else:
        return render(request,'home.html')

def signinpage(request):
    if request.method=='POST':
        usname = request.POST['username']
        pas = request.POST['password']

        user = auth.authenticate(username=usname,password=pas)
        if user is not None:
            auth.login(request,user)
            return redirect('userhome',)
        else:
            return render(request,'signup.html')
    else:
        return render(request,'home.html')

def userhome(request):
    return render(request,'userhome.html') 
def logout(request):
    auth.logout(request)
    return render(request,'home.html')       
def contactpage(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        comment = request.POST['comment']
        
        contact = Contact(name=name,email=email,mobile=mobile,comment=comment)
        contact.save()
        return redirect('home')
    else:
        return render(request,'home.html')
