from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
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