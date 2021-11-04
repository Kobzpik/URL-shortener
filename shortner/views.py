from django.shortcuts import render
from django.http import HttpResponse
from .models import ShortURL

# Create your views here.

def home(request):
    return render(request, 'index.htm')

def result(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'notfound.htm')
    context = {'obj':current_obj[0]}
    return render(request, 'res.htm',context)

def createShortURL(request):
    pass