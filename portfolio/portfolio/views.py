from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text = 10+20
    return render(request,'index.html')
def about(request):
    text = 10+20
    return render(request,'admin/about.html')
