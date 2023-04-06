from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #import messages
from django.contrib.auth.models import User
from .models import contentRegister

# Create your views here.

def login_user(request):
    if request.method == "POST":
        logemail = request.POST.get('logemail')
        password = request.POST.get('logpassword')
        user = authenticate(request, username=logemail, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminPanel')
            else:
                messages.success(request, 'Logged in Successfully')
                return redirect('/')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('/')
    
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out Successfully')
    return redirect('/')

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        emailid = request.POST.get('email')
        password = request.POST.get('password')
        reppassword = request.POST.get('reppassword')
        if password != reppassword:
            return redirect('/')
        user = User.objects.create_user(username, emailid, password)
        user.save()
        messages.success(request, 'User Created Successfully')
        return redirect('/')

    return render(request, 'index.html')

def python(request):
    content = contentRegister.objects.all()
    context = {
        'content':content,
    }
    return render(request, 'pages/pythonCourse.html',context=context)

@xframe_options_sameorigin
def courseContent(request):
    content = contentRegister.objects.all()
    context = {
        'content':content,
    }
    return render(request, 'pages/courseContent.html',context=context)

def editor(request):
    return render(request, 'pages/editor.html')

def exercises(request):
    return render(request, 'pages/exercises.html')

def userAccount(request):
    return render(request, 'pages/userAbout.html')

def adminPanel(request):
    course = contentRegister.objects.all()
    user = User.objects.filter(is_staff=False).values()
    context = {
        'users': user,
        'course':course,
    }
    return render(request, 'pages/adminPanel.html', context)

def chapterContent(request):
    if request.method == "POST":
        chTitle = request.POST.get('ch_title')
        chName = request.POST.get('ch_name')
        chTheory = request.POST.get('ch_theory')
        chVideo = request.FILES['ch_video']
        chExample = request.POST.get('ch_example')
        obj=contentRegister.objects.create(chTitle=chTitle,chName=chName,chTheory=chTheory,chVideo=chVideo,chExample=chExample)
        obj.save()
        messages.success(request, 'Chapter Created Successfully')
        return redirect('adminPanel')
    return redirect('/')

def details(request, id):
    context = {
        'obj': get_object_or_404(contentRegister,pk=id),
    }
    
    return render(request, 'pages/courseContent.html',context=context)

def previousPage(request, id):
    context = {
        'obj': get_object_or_404(contentRegister,pk=id),
    }
    return render(request, 'pages/courseContent.html',context=context)

def nextPage(request, id):
    context = {
        'obj': get_object_or_404(contentRegister,pk=id),
    }
    return render(request, 'pages/courseContent.html',context)