from django.http import HttpResponse
from django.shortcuts import render

from . import models

from .models import About
def index(request):
    data = About.objects.all()
    context = {
        'all_data':data
    }
    return render(request,'index.html',context)
def about(request):
    data = About.objects.all()
    context = {
        'all_data':data
    }
    
    return render(request,'admin/about.html',context)
def store(request):
    name = request.POST.get('fname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')
    image = request.FILES.get('image')
    info = [name,dob,phone,desc]

    if(len(name)==0 or len(dob) ==0 or len(phone)==0 or len(desc)==0):
        return HttpResponse("Each field is required")
    else:
        about = models.About()
        rows_count = About.objects.count()
        if(rows_count>=1):

            return HttpResponse("You can not insert more than one value")
        else:

            about.name = name
            about.dob = dob 
            about.phone = phone 
            about.desc = desc 
            about.image = image
            about.save()
            return HttpResponse("You data has been inserted successfully")
        
    # return render(request,'index.html')
