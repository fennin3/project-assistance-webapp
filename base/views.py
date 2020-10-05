from django.shortcuts import render, redirect
from .forms import MessageForm, TestimonyForm
from .models import Project, Testimony


def home(request):
    projects = Project.objects.all()
    testimonies = Testimony.objects.all().order_by('-date')

    try:
        testimonies = testimonies[:3]
    except Exception:
        pass



    try:
        projects = projects[:3]
    except Exception:
        pass

    
    form = MessageForm()


    context = {
        'form':form,
        'projects':projects,
        'testimonies':testimonies,
        
    }

    return render(request,'base/index.html', context)

def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = MessageForm()

    context = {
        'form':form
    }
    return render(request, "base/contact_us.html", context)

def services(request):
    return render(request, 'base/services.html')



def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'base/projects.html', context) 



def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

def testify(request):
    testimonies = Testimony.objects.all()
    if request.method == "POST":
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TestimonyForm()

    context = {
        'form':form,
        'testimonies':testimonies
    }
    return render(request, 'base/testimony.html', context)