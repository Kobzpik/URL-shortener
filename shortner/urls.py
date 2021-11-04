from django.urls import path
from . import views,createurl,result

urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.createurl,name="create"),
     path('<str:url>',views.result,name="result"),

]
