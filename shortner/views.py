from django.shortcuts import render
from django.http import HttpResponse
from .models import ShortURL
from .form import createNewURL
from datetime import datetime
import random,string

# Create your views here.

def home(request):
    return render(request, 'index.htm')

def result(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'notfound.htm')
    context = {'obj':current_obj[0]}
    return render(request, 'res.htm',context)

#create new short URL
def createShortURL(request):
    if request.method == 'POST':
        form = createNewURL(request.POST) #Create new form
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars =''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) !=0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            
            d=datetime.now()
            s=ShortURL(original_url=original_website,short_url=random_chars,time_date_created=d)

            s.save()
            return render(request, 'urlcreated.htm',{'chars':random_chars})
    
    else:
        form=createNewURL()
        context={'form':form}
        return render(request,'createurl.htm',context)
