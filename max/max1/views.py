from django.shortcuts import render
from .max import find_maximum as maxi

def home(request):
    m = maxi()
    return render(request,'index.html',{'param1':m})

# Create your views here.
