from django.http import HttpResponse
from django.shortcuts import render

from . import models

def index(request):
    text = 10+20
    return render(request,'index.html')
def about(request):
    text = 10+20
    return render(request,'admin/about.html')
def store(request):
    name = request.POST.get('fname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')
    info = [name,dob,phone,desc]

    about = models.About()
    about.name = name
    about.dob = dob 
    about.phone = dob 
    about.desc = desc 
    about.save()
    return HttpResponse(request.POST)
    # return render(request,'index.html')
