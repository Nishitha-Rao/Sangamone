from django.shortcuts import render
from .min import find_minimum as mm

def home(request):
    m = mm()
    return render(request,'index.html',{'param1':m})
# Create your views here.
