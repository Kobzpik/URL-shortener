from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.htm')

def createurl(request):
    pass

def res(request):
    pass