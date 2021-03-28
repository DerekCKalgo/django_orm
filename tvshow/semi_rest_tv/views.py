from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import *

def index(request):
    return render(request, "form.html")

def submit(request):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows')
    else:
        a=Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release'], desc=request.POST['desc'])
        print(a.id)
        messages.success(request, "successfully added")
        return redirect('/shows/all')

def allshows(request):
    context={
        'all_shows': Show.objects.all()
    }
    return render(request, "allshows.html", context)

def show(request, show_id):
    print("go to individual show")
    context={
        'show': Show.objects.get(id=show_id)
    }
    return render(request, "show.html", context)

def edit(request, show_id):
    context={
        'show': Show.objects.get(id=show_id)
    }
    return render(request, "edit.html", context)

def delete(request, show_id):
    print("in delete function")
    thisshow=Show.objects.get(id=show_id)
    thisshow.delete()
    return redirect('/shows/all')

def editdata(request, show_id):
    print("in editing database")
    errors=Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            context={
                'show': Show.objects.get(id=show_id)
            }
            return render(request, 'editshow.html', context)
    else:
        thisshow=Show.objects.get(id=show_id)
        thisshow.title=request.POST['title']
        thisshow.network=request.POST['network']
        thisshow.release_date=request.POST['release']
        thisshow.desc=request.POST['desc']
        thisshow.save()
        return redirect('/shows/all')