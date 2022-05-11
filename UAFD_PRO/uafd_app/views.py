from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'index.html')

def about(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'about.html')

def management(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'management.html')

def aboutsociety(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'aboutsociety.html')

def vision(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'vision.html')

def services(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'services.html')

def activities(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'activities.html')

def recent_activities(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'recent_activities.html')

def upcoming_activities(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'upcoming_activities.html')

def members(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'members.html')

def terms(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'terms.html')

def notifications(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'notifications.html')

def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'contact.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('applicationform')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        aadhar = request.POST['number']
        name = request.POST['name']
        userid = request.POST['userid']
        password = request.POST['password']
        phone = request.POST['phone']
      
        user = User.objects.create_user(username=name,password=password)
        Register.objects.create(user=user, aadhar=aadhar,userid=userid,phone=phone)
        return redirect('login') 
    return render(request,'signup.html', locals())


def logout_view(request):
    logout(request)
    return redirect('login')

def applicationform(request):
    return render(request, 'application_form.html')
    