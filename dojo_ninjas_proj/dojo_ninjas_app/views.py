from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context={
        'all_dojo':dojo.objects.all()
    }
    return render(request, "dojo_ninjas.html", context)

def dojos(request):
    dojo.objects.create(name=request.POST["name"], city=request.POST["city"], state=request.POST["state"], desc=request.POST["desc"])
    return redirect('/')

def ninj(request):
    ninjas.objects.create(first_name=request.POST["first name"], last_name=request.POST["last name"], dojo=dojo.objects.get(id=(request.POST["choice"])))
    return redirect('/')
