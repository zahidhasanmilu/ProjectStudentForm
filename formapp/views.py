from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    if request.method =="POST":
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        sem=request.POST.get('sem')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if name and dept and sem and email and password:
            contact = Contact(name=name, dept=dept,sem=sem, email=email,password=password)
            contact.save()
        else:
            return  HttpResponse("Please enter all details")

    return render(request,"index.html")