from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    context={
        'all_course': Course.objects.all()
    }
    return render(request, 'form.html', context)

def submit(request):
    errors=Course.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'], description=request.POST['desc'])
        messages.success(request, "Course successfully updated")
        return redirect('/')

def delete(request, course_id):
    context={
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'course.html', context)

def deletethis(request, course_id):
    a=Course.objects.get(id=course_id)
    a.delete()
    return redirect('/')