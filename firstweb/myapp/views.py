from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#M T V {model template views}

def Home(request):
    return render(request,'myapp/home.html')
def Aboutus(request):
    return render(request,'myapp/aboutus.html')
def Contact(request):
    return render(request,'myapp/contact.html')
def Tracking(request):
    tracks = ['ลุง - TA#3215521TH','ลุงสมชาย - TA#321451521TH','สมศรี - TA#3212463621TH']
    context = {'tracks':tracks}
    return render(request,'myapp/tracking.html',context)