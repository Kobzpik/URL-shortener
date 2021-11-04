from django.urls import path
from . import views
from .views import createShortURL,result

urlpatterns = [
    path('',views.home,name="home"),
    path('create/',createShortURL,name="create"),
     path('<str:url>',result,name="result")

]
