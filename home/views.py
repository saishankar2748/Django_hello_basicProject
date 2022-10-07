from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'var1':'Sandhya',
        'var2':'Santhosh'
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("about us")

def service(request):
    return HttpResponse("Services provided")

def contact(request):
    return HttpResponse("contact us")