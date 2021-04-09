from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "login.html")

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
        User = Register.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=hashedpw)
        request.session['user']=User.id
        return redirect('/wall')

def login(request):
    if request.method == 'POST':
        errors = Register.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            User=Register.objects.get(email=request.POST['loginemail'])
            request.session['user']=User.id
            return redirect('/wall')
    else:
        redirect('/')

def wall(request):
    if 'user' in request.session:
        context={
            'usermessages': Message.objects.all()
        }
        return render(request, 'wall.html', context)

def message(request):
    if request.method == 'POST':
        errors = Message.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/wall')
        else:    
            newMessage=Message.objects.create(message=request.POST['message'], user=Register.objects.get(id=request.session['user']))
            return redirect('/wall')
    else:
        redirect('/wall')

def comment(request, message_id):
    newComment=Comment.objects.create(comment=request.POST['comment'], message=Message.objects.get(id=message_id), user=Register.objects.get(id=request.session['user']))
    return redirect('/wallmessagecomment')

def wallmessagecomment(request):
    if 'user' in request.session:
        context={
            'usermessages': Message.objects.all()
            }
        return render(request, 'wallmessagecomment.html', context)
    