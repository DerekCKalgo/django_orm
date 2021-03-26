from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    if request.method == "GET":
        return render(request, "form.html")
    else:
        print("Works!")
        a=Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release'], desc=request.POST['desc'])
        print(a.id)
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
    thisshow=Show.objects.get(id=show_id)
    thisshow.title=request.POST['title']
    thisshow.network=request.POST['network']
    thisshow.release_date=request.POST['release']
    thisshow.desc=request.POST['desc']
    thisshow.save()
    return redirect('/shows/all')