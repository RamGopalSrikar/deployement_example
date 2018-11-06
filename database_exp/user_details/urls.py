from django.urls import path
from user_details import views

urlpatterns=[
    path('',views.index,name='index'),

]
