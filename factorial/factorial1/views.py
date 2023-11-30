from django.shortcuts import render
from .factorial import find_factorial as ff

def home(request):
    factorial = ff()
    return render(request,'index.html',{'param1':factorial})


# Create your views here.
