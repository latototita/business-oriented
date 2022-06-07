from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html',{})
def contact(request):
    return render(request,'contact.html',{})
def services(request):
    return render(request,'services.html',{})
