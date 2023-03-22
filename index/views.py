from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import BioData, Results, Courses, Registered, Projects

# Create your views here.
def Home(request):

    if request.method == 'POST':
        dev_no = request.POST.get('dev_no')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=dev_no)
        except Exception as e:
            print('User not found')

        user = authenticate(request, username=dev_no, password=password)

        if user is not None:
            login(request, user)
            return redirect('student-portal')

        else:
            print('User does not exist')

    context = {
        'info': BioData.objects.all()
    }

    return render(request, 'home.html', context)

def StaffLogin(request):
    return render(request, 'staff_login.html')

def StudentPortal(request):
    context = {
        'data': BioData.objects.get(id=1),
    }
    return render(request, 'student_portal.html', context)

def ResultsPage(request):
    if request.method == 'POST':
        #code = request.POST.get(h1)
        #registration = request.POST.get('course')
        #register = Registered(name=code)
        #register.save()
        print('It Works !!!')
    context = {
        'result': Results.objects.get(id=3),
        }
    return render(request, 'results.html', context)

def Registration(request):
    context = {
        'courses': Courses.objects.all().filter(level=300),
    }
    return render(request, 'registration.html', context)

def Project(request):
    context = {
        'projects': Projects.objects.all()
    }
    return render(request, 'projects.html', context)

#def 
