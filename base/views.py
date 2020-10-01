from django.shortcuts import render



def home(request):
    return render(request,'base/index.html')

def contact_us(request):
    return render(request, "base/contact_us.html")

def services(request):
    return render(request, 'base/services.html')