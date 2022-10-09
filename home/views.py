from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# Create your views here.
def index(request):
    context = {
        'var1':'Sandhya',
        'var2':'Santhosh'
    }
   # messages.success(request,"this is success mesg")
    return render(request,'index.html',context)
    # return HttpResponse("This is home page")

def about(request):
    
    return render(request,'about.html')
   # return HttpResponse("about us")

def service(request):
    return render(request,'service.html')
   # return HttpResponse("Services provided")

def contact(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !!')

    return render(request,'contact.html')
    #return HttpResponse("contact us")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username,password)
        
        if user is not None:
            # A backend authenticated the credentials
            print('logged in successful')
            login(request,user)
            return redirect('/contact/')
        else:
            # No backend authenticated the credentials
            print('not logged in ')
            return redirect('/login')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')