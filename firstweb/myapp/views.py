from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home(request):
    return render(request,'myapp/home.html')
def Aboutus(request):
    return render(request,'myapp/aboutus.html')
def Contact(request):
    return render(request,'myapp/contact.html')