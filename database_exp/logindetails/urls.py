from django.contrib import admin
from django.urls import path
from logindetails import views

urlpatterns = [

    path('',views.index,name='index'),
]
