from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "registration.html")

def register(request):
    errors=Register.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashedpw = bcrypt.hashpw(request.POST
        ['password'].encode(), bcrypt.gensalt()).decode()
        print(request.POST['password'])
        print(hashedpw)
        newUser = Register.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=hashedpw)
        request.session['user']=newUser.id
        return redirect('/success')

def success(request):
    if 'user' in request.session:
        return render(request, "success.html")
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        errors = Register.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            LoginUser=Register.objects.get(email=request.POST['loginemail'])
            request.session['user']=LoginUser.id
            return redirect('/success')
    else:
        redirect('/')

def logout(request):
    del request.session['user'] 
    return redirect('/')


